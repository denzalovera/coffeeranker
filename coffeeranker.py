import os
from app import create_app

'''
created by: denz 04/27/2017
'''
config_name = os.getenv('FLASK_CONFIG')
app = create_app(config_name)

if __name__ == '__main__':
    app.run()

# TODO: can't run db_migration missing library 'mysql-python'
# we need to move to a Linux virtualenv for project,
# easiest way to install this is through a linux box, have to setup scotch as new virtualenv.