from flask import Flask, render_template, url_for
import requests 

app = Flask(__name__)


@app.route('/')
def index():
    x = requests.get("https://meme-api.com/gimme")
    title = x.json()["title"] 
    url = x.json()["url"]
    author = x.json()["author"]
    print("THIS ISISI: ",title, url, author)
    return render_template("index.html", title = title, url=url, author=author) 


if __name__ == '__main__':
    app.run(debug=True)
