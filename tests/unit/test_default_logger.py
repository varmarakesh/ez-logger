from ez_logger.default_logger import DefaultLogger
import unittest


class TestDefaultLogger(unittest.TestCase):

    def setUp(self):
        pass

    def test_default_logger(self):
        logger = DefaultLogger()
        self.assertIsNotNone(logger.logger)

    def tearDown(self):
        pass
