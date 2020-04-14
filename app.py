# app.py - a minimal flask api using flask_restful
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    return 'V3.0 of helloworld in a Docker container!'

class hello(Resource):
    def get(self):
        return {'message': 'hello world'}

api.add_resource(hello, '/hello')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
