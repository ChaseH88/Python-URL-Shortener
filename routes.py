from flask import request, redirect
from utils import generate_random_string
from store import store

def main():
    url = request.args.get('url', default=None, type=str)

    if url is not None:
        if store.getKey(url) is None and len(url) > 0:
            key = generate_random_string(5)
            store.add(url, key)
            return key
        elif store.getKey(url) is not None:
            return store.getKey(url)
        else:
            return "Invalid URL"
    else:
        return "No URL provided"

def redirect_to_url(key):
    store_data = store.getStore()
    for original_url, stored_key in store_data.items():
        if stored_key == key:
            return redirect(original_url)
    return "Invalid URL"
