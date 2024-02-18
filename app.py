from flask import Flask
app = Flask(__name__)

# Setting Hello from Flask file
@app.route('/')
def hello():
    return 'Hello from Flask!'
