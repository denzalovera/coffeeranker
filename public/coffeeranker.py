import os
from app import create_app

'''
created by: denz 04/27/2017
'''
config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

#TODO: fix department module backend and frontend

if __name__ == '__main__':
    app.run()
