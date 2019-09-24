import unittest
from karr_lab_aws_manager.config import config

class TestConfig(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.credentialsFile = config.credentialsFile()
        cls.credentialsFileX = config.credentialsFile(credential_path = 'some_nonsense', config_path='some_nonsense')
        cls.credentialsUser = config.credentialsUser()

    def test_file_config(self):
        self.assertEqual(self.credentialsFile.AWS_SHARED_CREDENTIALS_FILE, '~/.wc/third_party/aws_credentials')
        self.assertEqual(self.credentialsFile.AWS_CONFIG_FILE, '~/.wc/third_party/aws_config')
        self.assertEqual(self.credentialsFileX.AWS_SHARED_CREDENTIALS_FILE, "/some_nonsense")
        self.assertEqual(self.credentialsFileX.AWS_CONFIG_FILE, "/some_nonsense")

    def test_user_config(self):
        self.assertEqual(self.credentialsUser.access_key, 'TESTKEYID')