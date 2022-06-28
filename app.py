from flask import Flask
import mysql.connector
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



def optellen():
    return 6 + 14

@app.route("/")
@cross_origin()
def hello_world():
    return "<p>Hello, World!</p>" + str(optellen())


@app.route("/andereingang")
@cross_origin()
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