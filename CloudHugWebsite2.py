import time

from tokens import *

from flask import Flask, render_template
app = Flask(__name__)

from azure.storage import TableService, Entity, QueueService

myaccount = getAccount()
mykey = getKey()

table_service = TableService(account_name=myaccount, account_key=mykey)
queue_service = QueueService(account_name=myaccount, account_key=mykey)


        
#@app.route("/")
#def home():
#    print 'here'
#    return render_template('base.html')  

while True:
    x = eval(getMessage())
    type(x)
    print getMessage()

#@app.route("/")
#def hello():
#    print getMessage() 
#    return str(getMessage())



if __name__ == "__main__":
    app.run()