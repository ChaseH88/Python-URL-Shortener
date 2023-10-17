from flask import request, redirect
from utils import generate_random_string
from store import key_value_store

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
    
def redirect_to_url(key):
    for original_url, stored_key in key_value_store.items():
        if stored_key == key:
            return redirect(original_url)
    return "Invalid URL"