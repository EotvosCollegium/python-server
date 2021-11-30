from flask import Flask, request, send_from_directory

app = Flask(__name__, static_url_path='')

@app.route('/pow/<int:value>')
def pow(value):
    return str(value * value)

@app.route('/concat/<text>')
def concat(text):
  return text + text

@app.route("/")
def index():
    return send_from_directory("", "index.html")

if __name__ == "__main__":
    app.run()