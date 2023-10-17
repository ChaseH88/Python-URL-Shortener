from flask import Flask, request, redirect
import random
import string

app = Flask(__name__)

key_value_store = {}

def generate_random_string(length=5):
    letters = string.ascii_letters + string.digits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

@app.route("/")
def main():
    url = request.args.get('url', default=None, type=str)
    
    if url is not None:
        if url not in key_value_store and len(url) > 0:
            key_value_store[url] = generate_random_string(5)
            return key_value_store[url]
        elif url in key_value_store:
            return key_value_store[url]
        else:
            return "Invalid URL"
    else:
        return "No URL provided"

@app.route("/<key>")
def redirect_to_url(key):
    for original_url, stored_key in key_value_store.items():
        if stored_key == key:
            return redirect(original_url)
    return "Invalid URL"

if __name__ == "__main__":
    app.run(debug=True)
