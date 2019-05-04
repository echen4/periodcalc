#!/usr/bin/env python
from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import sys

import os

app = Flask(__name__)
app.debug=True
app.secret_key = 'S3CR3T'


# initial page
@app.route('/', methods=['POST', 'GET'])
def main_page():
    if request.method == "GET" or request.method == "POST":
        return render_template('index.html', title="Food Mood: Welcome")
        

# pick location + add cuisine choices        
@app.route('/calculate', methods=['POST', 'GET'])
def pickLocation():
    if request.method == "GET":
        return render_template('location.html', title="Food Mood: Input")
    else:
        return render_template('location.html', title="Food Mood: Input")
        

# show restaurant result        
@app.route('/result', methods=['POST', 'GET'])
def calculate():
    if request.method == "GET":
        return render_template('location.html', title="Food Mood: Result")
    else:
        # keep track if all inputs are valid
        success = True

        # obtain form inputs
        try:
            pad = int(request.form['pad'])
            tampon = int(request.form['tampon'])
            liner = int(request.form['liner'])
            period = int(request.form['period'])
            year = int(request.form['year'])
            if pad < 0 or tampon < 0 or liner < 0 or period < 0 or year < 0:
                success = False
        except ValueError:
            success = False


        if success: # if successfully accessed yelp
            pad_price = 0.20
            tampon_price = 0.19
            liner_price = 0.04

            lifetime = period * year * 42
            daily_price = (pad * pad_price) + (tampon * tampon_price) + (liner * liner_price)
            total_price = daily_price * lifetime

            pad_use = pad * lifetime
            tampon_use = tampon * lifetime
            liner_use = liner * lifetime


            return render_template('result.html', tprice=total_price, pcount=pad_use,
                                    tcount=tampon_use, lcount=liner_use,
                                    title="Your Period Calculator Results")
        else: # if unable to get results
            flash("There was an error. Please make sure your inputs are valid")
            return redirect(url_for("main_page"))
        

'''
Script to launch app in debug mode
'''
if __name__ == '__main__':
    app.debug = True
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
