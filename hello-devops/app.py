from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, CI/CD!"

@app.route('/status')
def get_status():
    return "waw a status endpoint so cooll"

if __name__ == "__main__":
    app.run()
