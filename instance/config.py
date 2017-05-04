from coffee_utils import keygen

# create a random keygen of length 8
SECRET_KEY = keygen.generate_password(8)

# connect to vagrant mysql database address: 192.168.33.10/24
# format: 'mysql://username:password@localhost/db_name'
SQL_ALCHEMY_DATABASE_URI = 'mysql://cr_admin:admin@192.168.33.10/coffeeranker'
