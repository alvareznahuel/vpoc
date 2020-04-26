#!/usr/bin/python3
from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class MessagesList(Resource):
    def get(self):
        return {'messages': [ 
                    {'status': 'REC READ', 'timestamp': '19/05/25,18:43:51-12', 'content': 'DE MOVISTAR: Recibimos un pago de 70,73. Si abonaste el total de tu factura y tu linea esta interrumpida, espera 2hs y apaga/prende el celular para reestablece#', 'phoneNumber': '3235', 'id': '12'},
                    {'status': 'REC READ', 'timestamp': '19/06/22,19:13:22-12', 'content': 'Ya tenes 200MB hasta las 0hs x$18. Si los superas, tenes automaticamente otros 200MBx$18 Para Baja responde NO y navega a velocidad minima', 'phoneNumber': '772', 'id': '13'},
                    {'status': 'REC READ', 'timestamp': '20/03/31,08:21:50-12', 'content': 'Hola', 'phoneNumber': '01159598800', 'id': '14'},
                    {'status': 'REC READ', 'timestamp': '20/03/31,10:20:14-12', 'content': 'Holaaaa!', 'phoneNumber': '01167695041', 'id': '15'}
                ]}
    def post(self):
        json_data = request.get_json(force=True)
        print('Phone number: ' + json_data['phoneNumber'])
        print('Message text: ' + json_data['messageText'])
        return {'status ': 201, 'message': 'Message send.'},201

class Messages(Resource):
    def get(self, message_id):
        return {'status': 'REC READ', 'timestamp': '19/05/25,18:43:51-12', 'content': 'DE MOVISTAR: Recibimos un pago de 70,73. Si abonaste el total de tu factura y tu linea esta interrumpida, espera 2hs y apaga/prende el celular para reestablece#', 'phoneNumber': '3235', 'id': '12'}

api.add_resource(MessagesList, '/messages')
api.add_resource(Messages, '/messages/<string:message_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)