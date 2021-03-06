import unittest
from subprocess import call, check_output, Popen, PIPE, STDOUT
from ez_logger.console_logger import ConsoleLogger


class TestConsoleLogger(unittest.TestCase):

    def setUp(self):
        self.base_python_statement = "import sys;from ez_logger.console_logger import ConsoleLogger;cl=ConsoleLogger();"

    def test_info(self):
        info_log_statement = self.base_python_statement + "cl.info('info');sys.exit(0);"
        output = check_output(
            'python -c "{0}"'.format(info_log_statement),
            shell=True,
            stderr=STDOUT
        )
        self.assertTrue(
            str(output).find('info')
        )

    def test_error(self):
        info_log_statement = self.base_python_statement + "cl.info('error');sys.exit(0);"
        output = check_output(
            'python -c "{0}"'.format(info_log_statement),
            shell=True,
            stderr=STDOUT
        )
        self.assertTrue(
            str(output).find('error')
        )

    def test_debug(self):
        info_log_statement = self.base_python_statement + "cl.info('debug');sys.exit(0);"
        output = check_output(
            'python -c "{0}"'.format(info_log_statement),
            shell=True,
            stderr=STDOUT
        )
        self.assertTrue(
            str(output).find('debug')
        )

    def test_critical(self):
        info_log_statement = self.base_python_statement + "cl.info('critical');sys.exit(0);"
        output = check_output(
            'python -c "{0}"'.format(info_log_statement),
            shell=True,
            stderr=STDOUT
        )
        self.assertTrue(
            str(output) .find('critical')
        )
