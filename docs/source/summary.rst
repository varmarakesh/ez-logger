Quick Reference
---------------

console logging::

   from ez_logger.console_logger import ConsoleLogger
   logger = ConsoleLogger()
   logger.error('some error occurred')

file logging::

   from ez_logger.file_logger import FileLogger
   logger = FileLogger(
      log_file='test.log',
      log_dir='/tmp'
   )
   logger.error('some error occurred')