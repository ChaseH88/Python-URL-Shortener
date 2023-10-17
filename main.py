from flask import Flask
from routes import main, redirect_to_url, serve_ui

app = Flask(__name__)

app.add_url_rule('/', 'main', serve_ui)
app.add_url_rule('/<key>', 'redirect_to_url', redirect_to_url)
app.add_url_rule('/ui', 'serve_ui', main)

if __name__ == "__main__":
    app.run(debug=True)
