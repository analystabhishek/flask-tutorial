from flask import Flask
from os import name
from uuid import UUID

app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page"

#integer route

@app.route('/user/<int:id>')
def users(id):
    return f" User ID {id} to the User Page"


#float route
@app.route('/price/<float:amount>')
def price(amount):
    return f"Price is {amount} to the User Page"

#string route
@app.route('/username/<string:name>')
def username(name):
    return f"Username is {name} to the User Page"

#file path
@app.route('/file/<path:filepath>')
def file(filepath):
    return f"File path is {filepath} to the User Page"

#uuid route
@app.route('/student/<uuid:user_id>')
def student(user_id):
    return f"Student ID is {user_id} to the User Page"

if __name__ == '__main__':
    app.run(debug=True)