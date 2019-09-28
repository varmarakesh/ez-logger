from ez_logger.tenant_logger import TenantLogger
import unittest
import glob
import os


class TestTenantLogger(unittest.TestCase):

    def setUp(self):
        pass

    def test_tenant_logger_default_log(self):
        file = 'tenant.log'
        tenant = 'c01'
        logger = TenantLogger(log_file=file)
        logger.info('hello', 'c01')
        file_content = open(file).read()
        self.assertTrue(
            file_content.find('hello') != -1
        )
        self.assertTrue(
            file_content.find(tenant) != -1
        )

    def tearDown(self):
        files = glob.glob("*.log")
        for file in files:
            os.remove(file)

