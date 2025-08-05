from flask import Flask, render_template, request, redirect, session, url_for
from connection import CONNECTION

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def home():
    return redirect('/login')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        try:
            username = request.form['username']
            password = request.form['password']

            conn = CONNECTION
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (username, password))
                user = cursor.fetchone()

            if user:
                session['user'] = username
                session['role'] = user.get('role', 'user')
                return redirect('/dashboard')
            else:
                error = 'Invalid credentials'
        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template('login.html', error=error)


@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        return redirect('/login')
    with CONNECTION.cursor() as cursor:
        cursor.execute("SELECT * FROM clients")
        clients = cursor.fetchall()
    success = session.pop('insert_success', None)
    return render_template('dashboard.html', clients=clients, success=success)


@app.route('/insert', methods=['POST'])
def insert():
    data = request.form
    with CONNECTION.cursor() as cursor:
        cursor.execute("INSERT INTO clients (First_Name, Last_name, age) VALUES (%s, %s, %s)",
                       (data['First_Name'], data['Last_name'], data['age']))
    CONNECTION.commit()
    session['insert_success'] = True
    return redirect('/dashboard')


@app.route('/delete/<int:id>')
def delete(id):
    if 'role' not in session or session['role'] != 'admin':
        return "Unauthorized", 403

    with CONNECTION.cursor() as cursor:
        cursor.execute("DELETE FROM clients WHERE id=%s", (id,))
    CONNECTION.commit()
    return redirect('/dashboard')

@app.route('/update/<int:id>', methods=['POST'])
def update(id):
    if 'role' not in session or session['role'] != 'admin':
        return "Unauthorized", 403
    
    data = request.form
    with CONNECTION.cursor() as cursor:
        cursor.execute("""
            UPDATE clients SET First_Name=%s, Last_name=%s, age=%s WHERE id=%s
        """, (data['First_Name'], data['Last_name'], data['age'], id))
    CONNECTION.commit()
    return redirect('/dashboard')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        First_Name = request.form.get('First_Name')
        Last_name = request.form.get('Last_name')
        age = request.form.get('age')

        with CONNECTION.cursor() as cursor:
            cursor.execute("""
                INSERT INTO clients (First_Name, Last_name, age)
                VALUES (%s, %s, %s)
            """, (First_Name, Last_name, age))
        CONNECTION.commit()
        #CONNECTION.close()
        return redirect('/dashboard')
    
    return render_template('form.html')


@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect('/login')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
