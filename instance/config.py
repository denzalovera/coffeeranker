from coffee_utils import keygen
SECRET_KEY = keygen(8)

DB_ENGINE = 'mysql'
DB_USER = 'cr_admin'
DB_PASSWORD = 'admin'
IP_ADDR = '192.168.33.10'
DB = 'coffeeranker'

SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}/{}'.format(DB_ENGINE, DB_USER, DB_PASSWORD, IP_ADDR, DB)
