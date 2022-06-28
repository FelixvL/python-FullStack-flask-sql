from flask import Flask
import mysql.connector


app = Flask(__name__)

def optellen():
    return 6 + 14

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>" + str(optellen())


@app.route("/andereingang")
def tweedefunctie():
    mydb = mysql.connector.connect(
        host="localhost",  #port erbij indien mac
        user="root",
        password="",
        database="fotodatabase"
    )
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM foto")

    myresult = mycursor.fetchall()
    naamfotograaf = ""
    for x in myresult:
        print(x[1])
        naamfotograaf = x[1]


    print("hier print ik iets")
    return '{"naamf":"'+naamfotograaf+'"}'