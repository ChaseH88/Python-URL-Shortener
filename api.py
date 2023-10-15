from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def main():
    key = request.args.get('key', default=None, type=str)

    return {
        "key": key
    }

if __name__ == "__main__":
    app.run(debug=True)
