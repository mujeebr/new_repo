from flask import Flask, render_template
from urllib.parse import quote as url_quote
import os
import random

app = Flask(__name__)

# List of image URLs (no need to add '/images/')
images = [
    "https://raw.githubusercontent.com/manifoldailearning/mlops-with-aws-datascientists/main/Section-11-Docker/images/image1.gif",
    "https://raw.githubusercontent.com/manifoldailearning/mlops-with-aws-datascientists/main/Section-11-Docker/images/image2.gif",
    "https://raw.githubusercontent.com/manifoldailearning/mlops-with-aws-datascientists/main/Section-11-Docker/images/image3.gif",
    "https://raw.githubusercontent.com/manifoldailearning/mlops-with-aws-datascientists/main/Section-11-Docker/images/image4.gif",
    "https://raw.githubusercontent.com/manifoldailearning/mlops-with-aws-datascientists/main/Section-11-Docker/images/image5.gif"
]

@app.route("/")
def index():
    # Pick a random image URL directly from the list
    src = random.choice(images)
    return render_template("index.html", url=src)

if __name__ == "__main__":
    # Set host and port for Flask app
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
