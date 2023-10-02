from flask import Flask
from flask import render_template, request
from datetime import datetime
from . import app, get_nimes

@app.route('/', methods=['GET', 'POST'])
def newnorknimes():
    if request.method == 'POST':
        yearmonth = request.form['nimes-month']
    else:
        yearmonth = datetime.now().strftime("%Y-%m")

    nimeslist = get_nimes(yearmonth)
    nimescount = len(nimeslist)
    
    return render_template('nimes.html', yearmonth=yearmonth, nimescount=nimescount, nimeslist=nimeslist)