from flask import Flask
app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return "<h1>Home Page</h1>Hello, World! Welcome to the Flask tutorial!"


@app.route('/about')
def about():
    return "<h1>About Page<h1>\n</h1>Welcome to the about page."


if __name__ == "__main__":
    app.run(debug=True)
