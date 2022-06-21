from flask import render_template, Blueprint, request

views = Blueprint("views", __name__)

# view  in this instance is a blueprint


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/shop")
def shop():
    return render_template("shop.html")


@views.route("/login")
def login():
    return render_template("login.html")
