from flask import  render_template, redirect, url_for, flash, request
from Food_Delivery_App import app


@app.route('/')
def index():
    return redirect(url_for('customers.rest'))

if __name__=="__main__":
    app.run(debug=True)