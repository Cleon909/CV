from flask import render_template, request, url_for
from application import app, db
from application.models import PageView
from flask_sqlalchemy import SQLAlchemy


@app.route('/', methods = ['GET'])
@app.route('/cv', methods = ['GET'])
def index():
    number_of_visitors = PageView.query.count()
    return render_template ('cv.html', visits = number_of_visitors)

@app.route('/regs', methods= {'GET'})
def regs():
    return render_template('regs.html')

@app.route('/securities', methods= {'GET'})
def secs():
    return render_template('securities.html')

@app.route('/derivatives', methods= {'GET'})
def derivs():
    return render_template('derivs.html')