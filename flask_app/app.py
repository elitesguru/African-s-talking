from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'  # Update with your MySQL username
app.config['MYSQL_PASSWORD'] = 'root'  # Update with your MySQL password
app.config['MYSQL_DB'] = 'Create_Account'

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        reg_no = request.form['reg_no']
        phone = request.form['phone']
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO user_app(username, regno, phone, email, password) VALUES (%s, %s, %s, %s, %s)", (name, reg_no, phone, email, password))
        mysql.connection.commit()
        cur.close()
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
