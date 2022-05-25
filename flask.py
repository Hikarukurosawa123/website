from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!\n"

    #can insert code by using the {code file_name} comand  


    #git init     -> initialize a local Git repository and create a first commit  
    #git add . 
    #git commit -m "Initial commit"