from flask import Flask
from routes import make_short_url, redirect_to_url, serve_home_page

app = Flask(__name__)

app.add_url_rule('/', 'main', serve_home_page)
app.add_url_rule('/<key>', 'redirect_to_url', redirect_to_url)
app.add_url_rule('/ui', 'serve_home_page', make_short_url)

if __name__ == "__main__":
    app.run(debug=True)
