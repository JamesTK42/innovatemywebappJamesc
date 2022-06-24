
from flask import Flask
from views import views, render_template

# import views from views file

app = Flask(__name__)
# we instantiate the app object

app.register_blueprint(views)
# we register the views blueprint


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True, port=8000)
    # running app
