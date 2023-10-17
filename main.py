from flask import Flask
from routes import main, redirect_to_url

app = Flask(__name__)

app.add_url_rule('/', 'main', main)
app.add_url_rule('/<key>', 'redirect_to_url', redirect_to_url)

if __name__ == "__main__":
    app.run(debug=True)
