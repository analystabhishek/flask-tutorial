from flask import Flask

app=Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Home Page"

#static route

@app.route('/users')
def users():
    return "Welcome to the User Page"


#dynamic route
@app.route('/user/<name>')
def user(name):
    return f"Welcome {name} to the User Page"


#Multiple dynmaic routes
@app.route("/student/<name>/<course>")
def student(name, course):
    return f"Welcome {name} is learning {course} course"


if __name__ == '__main__':
    app.run(debug=True)