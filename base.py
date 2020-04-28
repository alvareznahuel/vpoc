#Importing sqlalchemy
from flask_sqlalchemy import SQLAlchemy
#Instantiating sqlalchemy object
db = SQLAlchemy()
#Creating database class
class Suits(db.Model):
    #Creating field/columns of the database as class variables
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True, nullable=False)
    image = db.Column(db.String(250), unique=True, nullable=False)
    def __init__(self, name, image):                   
        self.name = name
        self.image = image
    #Method to show data as dictionary object
    def json(self):        
        return {'Name': self.name, 'Image': self.image}        
    #Method to find the query movie is existing or not
    @classmethod    
    def find_by_name(cls, name):        
        return cls.query.filter_by(name=name).first()
    #Method to save data to database
    def save_to(self):        
        db.session.add(self)        
        db.session.commit()
    #Method to delete data from database
    def delete_(self):        
        db.session.delete(self)        
        db.session.commit()