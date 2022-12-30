import os
import datetime
import decimal
#import pandas as pd
import tablib

from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

#from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True
'''
# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd
'''
@app.route("/")
def index():
    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("index.html")


@app.route("/tools")
def tools():
    #open(bosniak.xlsx) as rows
    return render_template("tools.html")

dataset = tablib.Dataset()

@app.route("/tools/aspects")
def aspects():
    with open(os.path.join(os.path.dirname(__file__),'tools/aspects.csv')) as f:
        dataset.csv = f.read()
    data = dataset.html
    return render_template("/tools/aspects.html", data=data)

@app.route("/tools/fisher")
def fisher():
    with open(os.path.join(os.path.dirname(__file__),'tools/fisher.csv')) as f:
        dataset.csv = f.read()
    data = dataset.html
    return render_template("/tools/fisher.html", data=data)

@app.route("/tools/fleischner")
def fleischner():
    with open(os.path.join(os.path.dirname(__file__),'tools/fleischner.csv')) as f:
        dataset.csv = f.read()
    data = dataset.html
    return render_template("/tools/fleischner.html", data=data)

@app.route("/tools/lungrads")
def lungrads():
    with open(os.path.join(os.path.dirname(__file__),'tools/lungrads.csv')) as f:
        dataset.csv = f.read()
    data = dataset.html
    return render_template("/tools/lungrads.html", data=data)

@app.route("/tools/atlanta")
def atlanta():
    with open(os.path.join(os.path.dirname(__file__),'tools/atlanta.csv')) as f:
        dataset.csv = f.read()
    data = dataset.html
    #table = pd.DataFrame.from_csv("data/atlanta.csv")
    return render_template("/tools/atlanta.html", data=data)

@app.route("/tools/bosniak")
def bosniak():
    with open(os.path.join(os.path.dirname(__file__),'tools/bosniak.csv')) as f:
        dataset.csv = f.read()
    data = dataset.html
    return render_template("/tools/bosniak.html", data=data)

@app.route("/tools/hinchey")
def hinchey():
    with open(os.path.join(os.path.dirname(__file__),'tools/hinchey.csv')) as f:
        dataset.csv = f.read()
    data = dataset.html
    return render_template("/tools/hinchey.html", data=data)

@app.route("/tools/cistospancreaticos")
def cistospancreaticos():
    with open(os.path.join(os.path.dirname(__file__),'tools/cistospancreaticos.csv')) as f:
        dataset.csv = f.read()
    data = dataset.html
    return render_template("c/tools/istospancreaticos.html", data=data) 

@app.route("/reports", methods=["GET", "POST"])
def reports():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
    
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("reports.html")

@app.route("/reports/frasesrx")
def frasesrx():
    return render_template("/reports/frasesrx.html")

@app.route("/reports/frasesmmg")
def frasesmmg():
    return render_template("/reports/frasesmmg.html")

@app.route("/reports/frasesus")
def frasesus():
    return render_template("/reports/frasesus.html")

@app.route("/reports/frasestc")
def frasestc():
    return render_template("/reports/frasestc.html")

@app.route("/reports/frasesrm")
def frasesrm():
    return render_template("/reports/frasesrm.html")

@app.route("/courses", methods=["GET", "POST"])
def courses():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
    
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("courses.html")

@app.route("/classes", methods=["GET", "POST"])
def classes():
    """Buy shares of stock"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
    
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("classes.html")

@app.route("/about")
def about():
    # User reached route via GET (as by clicking a link or via redirect)
    return render_template("about.html")

'''
def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
'''

@app.errorhandler(400)
def handle_400_error(_error):
    """Return a http 400 error to client"""
    return make_response(jsonify({'error': 'Misunderstood'}), 400)


@app.errorhandler(401)
def handle_401_error(_error):
    """Return a http 401 error to client"""
    return make_response(jsonify({'error': 'Unauthorised'}), 401)


@app.errorhandler(404)
def handle_404_error(_error):
    """Return a http 404 error to client"""
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.errorhandler(500)
def handle_500_error(_error):
    """Return a http 500 error to client"""
    return make_response(jsonify({'error': 'Server error'}), 500)


if __name__ == '__main__':

    PARSER = argparse.ArgumentParser(
        description="Seans-Python-Flask-REST-Boilerplate")

    PARSER.add_argument('--debug', action='store_true',
                        help="Use flask debug/dev mode with file change reloading")
    ARGS = PARSER.parse_args()

    PORT = int(os.environ.get('PORT', 5000))

    if ARGS.debug:
        print("Running in debug mode")
        CORS = CORS(APP)
        APP.run(host='0.0.0.0', port=PORT, debug=True)
    else:
        APP.run(host='0.0.0.0', port=PORT, debug=False)