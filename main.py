from wsgiref import simple_server
from flask import Flask
import os


app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def index():
    return "App is successfully deployed"

port = int(os.getenv("PORT", 5001))

if __name__ == "__main__":
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host, port=port, app=app)
    httpd.serve_forever()