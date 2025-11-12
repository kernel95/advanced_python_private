# app.py
#use flask framework for application

from flask import Flask, render_template, g
from web_dao import WebDao

app = Flask(__name__)
DB_FILE = "C:\\Users\\kelme\\Desktop\\python_advanced_qualcomm\\member_database.db"

#everytime I make a request then I want to close the DB
@app.teardown_appcontext
def close_db(error=None):
    print("closing database")
    db = g.pop("db", None)
    if db is not None:
        db.close()


@app.get("/members")
def members():
    dao = WebDao(DB_FILE)
    members = dao.get_all()
    #print(members)
    #return "<h1> it works </h1>"
    return render_template("members.html", 
                           heading="Member List",
                           members=members)

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
