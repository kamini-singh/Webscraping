from flask import Flask, request, render_template
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)  

@app.route('/index', methods =["GET", "POST"])
def home():
    return render_template("index.html")

@app.route('/fetch', methods =["GET", "POST"])
def weather():
    search= request.form.get("city_name")
    soup= BeautifulSoup(requests.get(f"https://www.google.com/search?q=weather+in+{search}").content, "html.parser")
    city = soup.find("span",class_="BNeawe tAd8D AP7Wnd").text
    temp= soup.find("div", class_="BNeawe iBp4i AP7Wnd").text
    details= soup.find("div",class_="BNeawe tAd8D AP7Wnd").text
    return render_template("index.html", city=city, temp=temp, details=details)
  

app.run()