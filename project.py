from flask import Flask
app = Flask(__name__)


# DB Session maker 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
# Create session and connect to DB
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
@app.route('/hello')
def HelloWord():
    return "Hello World"


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
