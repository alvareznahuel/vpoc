#Import necessary packages
from flask import Flask
from flask_restful import Resource, reqparse, Api 
#Instantiate a flask object 
app = Flask(__name__)
#Instantiate Api object
api = Api(app)
#Setting the location for the sqlite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
#Adding the configurations for the database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True 
#Import necessary classes from base.py
from base import Suits, db
#Link the app object to the Movies database 
db.init_app(app)
app.app_context().push()
#Create the databases
db.create_all() 
#Creating a class to create get, post, put & delete methods
class SuitsById(Resource):
    #Instantiating a parser object to hold data from message payload
    parser = reqparse.RequestParser()                      
    parser.add_argument('name', type=str, required=False, help='Suit name')    
    parser.add_argument('image', type=str, required=False, help='Suit image URL')    
    #Creating the get method
    def get(self, name):        
        item = Suits.find_by_name(name)        
        if item:            
            return item.json()        
        return {'Message': 'Suit is not found'}        
    #Creating the put method
    def put(self, name):        
        args = SuitsById.parser.parse_args()        
        item = Suits.find_by_name(name)        
        if item:            
            item.collection = args['collection']            
            item.save_to()            
            return {'Movie': item.json()}        
        item = Suits(name, args['image'])        
        item.save_to()        
        return item.json()
    #Creating the delete method
    def delete(self, name):        
        item  = Suits.find_by_name(name)        
        if item:            
            item.delete_()            
            return {'Message': '{} has been deleted from records'.format(name)}        
        return {'Message': '{} is already not on the list'.format(name)}
        
#Creating a class to get all the movies from the database.
class AllSuits(Resource):    
    #Instantiating a parser object to hold data from message payload
    parser = reqparse.RequestParser()                      
    parser.add_argument('name', type=str, required=False, help='Suit name')    
    parser.add_argument('image', type=str, required=False, help='Suit image URL')    
    #Defining the get method
    def get(self):        
        return {'Suits': list(map(lambda x: x.json(), Suits.query.all()))}    
    #Creating the post method
    def post(self):                
        args = AllSuits.parser.parse_args()
        if Suits.find_by_name(args['name']):            
            return {' Message': 'Suit with the name {} already exists'.format(args['name'])}  
        item = Suits(args['name'], args['image'])        
        item.save_to()        
        return item.json()

#Adding the URIs to the api
api.add_resource(AllSuits, '/api/v1/suits')
api.add_resource(SuitsById, '/api/v1/suits/<string:name>') 
if __name__=='__main__':        
    #Run the applications
    app.run()