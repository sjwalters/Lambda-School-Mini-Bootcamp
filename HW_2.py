from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Set your initial route at / to return 'Hello World'
# Modified to render an html page
@app.route('/')
def index():
    return render_template('home.html')

# Build a route called /birthday that returns your birthday as a string
@app.route('/birthday')
def birthday():
    return 'November 14 1984'

# Build a route called /greeting that accepts a parameter called name
# The route should return a string that says 'Hello <name>'
@app.route('/greeting/<name>') # Why do I need the right angle brackets?
def greeting(name):
    return "Hello " + name + '!'

# Extra Credit: Create a route called sum that adds two parameters together and returns them.
@app.route('/sum/<int:addend1>/<int:addend2>')
def sum(addend1, addend2):
    return str(addend1 + addend2)

# Create a route that performs subtraction and multiplication
@app.route('/subtract/<int:num1>/<int:num2>')
def subtract(num1, num2):
    return str(num1 - num2)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1,num2):
    return str(num1 * num2)

# And we will throw in division for fun
@app.route('/divide/<int:num1>/<int:num2>')
def divide(num1, num2):
    return str(num1 / num2)

#Create a route called /favoritefoods that returns a list of your favorite foods.
@app.route('/favoritefoods')
def favorite_foods():
    food = ['soup', 'seafood', 'sweats', 'steak' ]
    return jsonify(food)
