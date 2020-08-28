from flask import Flask ,request
import jwt
import datetime
import uuid

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissecretkey'
app.config['PUBLIC_KEY'] = 'thisispublickey'
public_id=str(uuid.uuid4())
token=jwt.encode({'public_id':public_id,'exp':datetime.datetime.utcnow() + datetime.timedelta(seconds=30)},app.config['SECRET_KEY'])
    

@app.route("/")
@app.route("/creditcardapp/")
def creditcard():
    #public_id=str(uuid.uuid4())
    #token=jwt.encode({'public_id':public_id,'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=60)},app.config['SECRET_KEY'])
    return ('Credit Card module ' + token.decode('UTF-8'))


if __name__ == "__main__":
    app.run()

    