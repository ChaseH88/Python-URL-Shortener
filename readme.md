# Url Shortener

## Installing
```
pip install Flask
```


## Running

**Production Mode**
```
flask --app main.py run
```

**Debug Mode**
```
flask --app main.py --debug run
```

## Usage

To create a new short url, send a `GET` request to the index `/` page with a `url` query parameter.

```
http://localhost:5000/?url=https://www.google.com
```

You will receive a text response with a 5 character short url. To use the short url, send a `GET` request to the code route handler. See the example below.

```
http://localhost:5000/XruQw
```

Assuming the code is valid, you will be redirected to the original url.