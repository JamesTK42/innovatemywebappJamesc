from flask import render_template, Blueprint, request

views = Blueprint("views", __name__)

# view  in this instance is a blueprint


@views.route("/")
def home():
    return render_template("index.html")


@views.route("/whois")
def about():
    return render_template("about.html")


@views.route("/links")
def links():
    return render_template("links.html")


@views.route("/shop")
def shop():
    return render_template("shop.html")


@views.route("/login")
def login():
    return render_template("login.html")


@views.route("/item1")
def item1():
    return render_template("item1.html")


@views.route("/item3")
def item3():
    return render_template("item3.html")


@views.route("/item4")
def item4():
    return render_template("item4.html")


@views.route("/item5")
def item5():
    return render_template("item5.html")


@views.route("/item6")
def item6():
    return render_template("item6.html")


@views.route("/item7")
def item7():
    return render_template("item7.html")


@views.route("/item8")
def item8():
    return render_template("item8.html")


@views.route("/item9")
def item9():
    return render_template("item9.html")


@views.route("/item10")
def item10():
    return render_template("item10.html")


@views.route("/item2")
def item2():
    return render_template("item2.html")
