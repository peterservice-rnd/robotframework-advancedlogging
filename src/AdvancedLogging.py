# -*- coding: utf-8 -*-

from os.path import join as path_join, normpath
from platform import platform

from robot.libraries.BuiltIn import BuiltIn
from robot.libraries.OperatingSystem import OperatingSystem
from robot.running.context import EXECUTION_CONTEXTS
from robot.utils import is_bytes


class AdvancedLogging(object):
    """
    Creating additional logs when testing.
    If during the test you want to add any additional information in the file, then this library
    provide a hierarchy of folders and files for logging.
    Folder hierarchy is created as follows: "output_dir/test_log_folder_name/Test_Suite/Test_Suite/Test_Case/file.log".
    Log files and folders are not removed before the test, and overwritten of new files.

     == Dependency: ==
    | robot framework | http://robotframework.org |
    -------

    When initializing the library, you can define two optional arguments
    | *Argument Name*      |  *Default value*  | *Description*                                                 |
    | output_dir           |  ${OUTPUT_DIR}    | The directory in which create the folder with additional logs |
    | test_log_folder_name |  Advanced_Logs    | Name of the folder from which to build a hierarchy of logs    |
    -------

    == Example: ==
    | *Settings*  |  *Value*           | *Value*  |  *Value*        |
    | Library     |  AdvancedLogging   | C:/Temp  |   LogFromServer |
    | Library     |  SSHLibrary        |          |                 |

    | *Test cases*              | *Action*                  | *Argument*             |  *Argument*            |
    | Example_TestCase          | ${out}=                   | Execute Command        |  grep error output.log |
    |                           | Write advanced testlog    | error.log              |  ${out}                |
    =>\n
    File C:/Temp/LogFromServer/TestSuite name/Example_TestCase/error.log  with content from variable ${out}
    """

    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, output_dir=None, test_log_folder_name='Advanced_Logs'):
        """ Initialisation

        *Args*:\n
            _output_dir_: output directory.\n
            _test_log_folder_name_: name for log folder
        """
        self.os = OperatingSystem()
        self.bi = BuiltIn()

        self.output_dir = output_dir
        self.test_log_folder_name = test_log_folder_name
        self.win_platform = 'Windows' in platform()

    def _get_suite_names(self):
        """
        Get List with the current suite name and all its parents names

        *Returns:*\n
            List of the current suite name and all its parents names
        """
        suite = EXECUTION_CONTEXTS.current.suite
        result = [suite.name]
        while suite.parent:
            suite = suite.parent
            result.append(suite.name)
        return reversed(result)

    @property
    def _suite_folder(self):
        """ Define variables that are initialized by a call 'TestSuite'

        *Returns:*\n
            Path to suite folder.
        """
        output = self.output_dir

        if self.output_dir is None:
            output = self.bi.get_variable_value('${OUTPUT_DIR}')

        suite_name = path_join(*self._get_suite_names())

        if self.win_platform:
            # Look at MSDN knowledge base: https://msdn.microsoft.com/en-us/library/aa365247(VS.85).aspx#maxpath
            long_path_support_prefix = '\\\\?\\'
            output = long_path_support_prefix + output

        suite_folder = path_join(output,
                                 self.test_log_folder_name,
                                 suite_name)

        return normpath(suite_folder)

    def write_advanced_testlog(self, filename, content, content_encoding='UTF-8'):
        """ Inclusion content in additional log file

        *Args:*\n
        _filename_ - name of log file;
        _content_ - content for logging;
        _content_encoding_ - encoding of content (if it's in bytes).

        *Returns:*\n
             Path to filename.

        *Example*:\n
        | Write advanced testlog   | log_for_test.log  |  test message |
        =>\n
        File ${OUTPUT_DIR}/Advanced_Logs/<TestSuite name>/<TestCase name>/log_for_test.log with content 'test message'
        """
        if is_bytes(content):
            content = content.decode(content_encoding)
        test_name = self.bi.get_variable_value('${TEST_NAME}', default='')
        log_file_path = path_join(self._suite_folder, test_name, filename)
        self.os.create_file(log_file_path, content)
        return normpath(log_file_path)

    def create_advanced_logdir(self):
        """ Creating a folder hierarchy for TestSuite

        *Returns:*\n
             Path to folder.

        *Example*:\n
        | *Settings* | *Value* |
        | Library    |        AdvancedLogging |
        | Library    |       OperatingSystem |

        | *Test Cases* | *Action* | *Argument* |
        | ${ADV_LOGS_DIR}=   | Create advanced logdir            |                |
        | Create file        | ${ADV_LOGS_DIR}/log_for_suite.log |   test message |
        =>\n
        File ${OUTPUT_DIR}/Advanced_Logs/<TestSuite name>/log_for_suite.log with content 'test message'
        """
        test_name = self.bi.get_variable_value('${TEST_NAME}', default='')
        log_folder = path_join(self._suite_folder, test_name)
        old_log_level = BuiltIn().set_log_level("ERROR")
        self.os.create_directory(log_folder)
        BuiltIn().set_log_level(old_log_level)
        return normpath(log_folder)
