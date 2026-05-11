from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__, static_folder='templates/static')

# DATABASE CONNECTION
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="food_ordering"
)

cursor = db.cursor(dictionary=True)

# LOGIN PAGE
@app.route('/')
def login():
    return render_template('login.html')

# SIGNUP PAGE
@app.route('/signup')
def signup():
    return render_template('signup.html')

# REGISTER
@app.route('/register', methods=['POST'])
def register():

    username = request.form['username']
    password = request.form['password']

    sql = "INSERT INTO users(username,password) VALUES(%s,%s)"
    values = (username,password)

    cursor.execute(sql, values)
    db.commit()

    return redirect('/')

# CHECK LOGIN
@app.route('/checklogin', methods=['POST'])
def checklogin():

    username = request.form['username']
    password = request.form['password']

    sql = "SELECT * FROM users WHERE username=%s AND password=%s"

    values = (username,password)

    cursor.execute(sql, values)

    user = cursor.fetchone()

    if user:
        return redirect('/home')
    else:
        return "Invalid Login"

# HOME PAGE
@app.route('/home')
def home():

    cursor.execute("SELECT * FROM foods")
    foods = cursor.fetchall()

    return render_template('home.html', foods=foods)

# CART PAGE
@app.route('/cart')
def cart():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)