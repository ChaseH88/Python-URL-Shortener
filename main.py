from flask import Flask, request

app = Flask(__name__)

key_value_store = {}

@app.route("/")
def main():
    url = request.args.get('url', default=None, type=str)

    if url is not None:
        key_value_store[url] = ""

    return {
        "url": url,
        "key_value_store": key_value_store
    }

if __name__ == "__main__":
    app.run(debug=True)
