from ez_logger.file_logger import FileLogger
import unittest
import glob
import os


class TestFileLogger(unittest.TestCase):

    def setUp(self):
        pass

    def test_file_logger_default_log(self):
        logger = FileLogger()
        logger.info('hello')
        file_content = open("app.log").read()
        self.assertTrue(
            file_content.find('hello') != -1
        )

    def test_file_logger_console_log_false(self):
        logger = FileLogger(console_logging=False)
        logger.info('hello')
        file_content = open("app.log").read()
        self.assertTrue(
            file_content.find('hello') != -1
        )

    def test_file_logger_name(self):
        logger = FileLogger(name='test', console_logging=False)
        logger.info('hello')
        file_content = open("test.log").read()
        self.assertTrue(
            file_content.find('hello') != -1
        )

    def test_file_logger_log_file(self):
        logger = FileLogger(name='test', log_file='test1.log', console_logging=False)
        logger.info('hello')
        file_content = open("test1.log").read()
        self.assertTrue(
            file_content.find('hello') != -1
        )

    def test_file_logger_log_file_directory(self):
        logger = FileLogger(name='test', log_file='test1.log', log_dir='/tmp', console_logging=False)
        logger.info('hello')
        file_content = open("/tmp/test1.log").read()
        self.assertTrue(
            file_content.find('hello') != -1
        )
        os.remove('/tmp/test1.log')

    def test_file_logger_error_level(self):
        logger = FileLogger(log_level='error')
        logger.error('hello')
        file_content = open("app.log").read()
        self.assertTrue(
            file_content.find('hello') != -1
        )
        self.assertTrue(
            file_content.find('ERROR') != -1
        )

    def tearDown(self):
        files = glob.glob("*.log")
        for file in files:
            os.remove(file)

