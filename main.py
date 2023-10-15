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

    if len(url) == 5:
      for key, value in key_value_store.items():
        if value == url:
          print("Redirecting to: ", key)
          return redirect(key)

    if url is not None and url not in key_value_store:
        key_value_store[url] = generate_random_string(5)

    return key_value_store[url]

if __name__ == "__main__":
    app.run(debug=True)
