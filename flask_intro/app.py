# app.py
#use flask framework for application

from flask import Flask, render_template

app = Flask(__name__)

#use decorator
@app.get("/")
def home():

    title = "Professional Training Homepage"
    colours = ["red", "green", "blue"]
    #return render_template("index.html") #html code here for web
    return render_template(
        "index.html", 
        title=title ,
        colours=colours
    ) #html code here for web

@app.get("/about")
def about():
    title="About Us"
    return render_template(
        "index.html",
        title=title,
        colours=[]
    )

#there is also a template engine

if __name__ == "__main__":

    app.run(debug=True)
