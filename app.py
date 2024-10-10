from Food_Delivery_App import app
from Food_Delivery_App import db
from flask import render_template

@app.route('/')
def index():
    return render_template('base.html')



if __name__=="__main__":
    
    app.run(debug=True)