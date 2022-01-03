from flask import render_template
from flask import request
from flask import Flask 
from random import sample
import random


app = Flask(__name__)


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == "POST":
        password_length = int(request.form['length'])
        characters = "!@#$%^&**()_+"
        numbers = '1234567890'
        small_letters = "qwertyuioplkjhgfdsazxcvbnm"
        upper_case = "QWERTYUIOPASDFGHJKLMNBVCXZ"
        prep = characters + numbers + small_letters + upper_case
        if password_length > 30:
            message = "can't generate password more than 30 characters"
            return render_template("index.html", message=message)
        else:
            passwd = ''.join(random.sample(prep, k=password_length))
            return render_template("index.html",password=passwd)

    return render_template("index.html")



if __name__ == "__main__":
    app.run(debug=True)

