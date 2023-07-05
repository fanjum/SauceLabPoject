"""
Implementing Logging mechanism for TestFramework
"""

import logging
import os


class Logger:
    """
    Returning logger instance.
    """

    def get_logger(self, module_name):
        """
        Instantiate logger object and attach file handler.
        :param module_name:
        :return:
        """
        logger = logging.getLogger(module_name)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        script_path = os.path.dirname(
            os.path.abspath(__file__))  # Dir name of current file i.e. //Test_Automation/TestFramework/Helper
        user_path = os.path.split(script_path)[0]  # Up one level i.e. //Test_Automation/TestFramework
        log_file_path = os.path.join(user_path, 'Log', module_name + '.robot.log')
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
