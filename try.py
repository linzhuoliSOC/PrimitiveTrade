# coding=utf-8
from flask import Flask, render_template, request, redirect, url_for
import pymysql


app = Flask(__name__)
@app.route('/',methods=['GET','POST'])
def getAnumber():
	number=0
	if request.method=="POST":
		number=int(request.form.get("number"))  
		#this is the key step of getting input, "number" is the "name" of the text input field

	return render_template('getNumber.html', postedNum=number)



if __name__ == '__main__':
	app.debug=True
	app.run()