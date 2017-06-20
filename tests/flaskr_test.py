import os
import flaskr
import unittest
import tempfile
"""
Testing Skeleton
this is based on: http://flask.pocoo.org/docs/0.12/testing/
we still need to modify parts of the skeleton to work on our application.

created by: Denz 06/20/2017
"""
class FlaskrTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
        flaskr.app.testing = True
        self.app = flaskr.app.test_client()
        with flaskr.app.app_context():
            flaskr.init_db()

    def tearDown(self):
        os.close(self.db_fd)
        os.unlink(flaskr.app.config['DATABASE'])

if __name__ == '__main__':
    unittest.main()