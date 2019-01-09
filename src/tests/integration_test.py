""" src/tests/test_subscribers.py"""
from ..app import create_app, db
import unittest
import json


class GlobalConfigTest(unittest.TestCase):
    """TemplateGroup Test Case"""

    def setUp(self):
        """Test Setup"""
        self.app = create_app("test")
        self.client = self.app.test_client
        self.globalconfig = {
            "globalConfigDefaultValue": "HELLO1",
            "globalConfigFullPath": "HELLO1",
            "globalConfigIsActive": True,
            "globalConfigName": "HELLO1",
            "globalConfigPath": "HELLO1",
            "globalConfigType": "HELLO1",
            "globalConfigUuid": "2",
            "opsCodeAutoId": "2",
            "loggedInUser": "sudhirk"

        }

        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_get_globalconfig(self):
        """ test globalconfig getAll """
        res = self.client().post('/globalconfig', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.globalconfig))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/globalconfig', headers={'Content-Type': 'application/json'})
        self.assertEqual(res.status_code, 200)

    def test_globalconfig_creation(self):
        """ test globalconfig creation """
        res = self.client().post('/globalconfig', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.globalconfig))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)

    def test_globalconfig_update(self):
        """ Test Update globalconfig """
        res = self.client().post('/globalconfig', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.globalconfig))
        json_data = json.loads(res.data)
        res = self.client().put('/globalconfig/' + str(1),
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(self.globalconfig))
        self.assertEqual(res.status_code, 200)

    def test_delete_globalconfig(self):
        """ Test globalconfig soft Delete """
        res = self.client().post('/globalconfig', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.globalconfig))
        json_data = json.loads(res.data)

        res = self.client().delete('/globalconfig/' + str(1),
                                   headers={'Content-Type': 'application/json'},
                                   data=json.dumps(dict(loggedInUser="sudhirkk")))
        self.assertEqual(res.status_code, 200)

    def tearDown(self):
        """ Tear Down"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
