import unittest
import os
import sys

from sympy.polys.benchmarks.bench_galoispolys import shoup_poly

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.append(PROJECT_PATH)

from src.python.common.config_load import LoadEnvVars
from src.python.common import config_load

class UnitTests(unittest.TestCase):

    @staticmethod
    def config_load_test():
        LoadEnvVars('src/test/resources/test.conf')
        test_conf_var = config_load.os.getenv('TEST_CONF_VAR')
        print("test_conf_var: ", test_conf_var)
        assert test_conf_var == '10', f"should be 10, got: "+ test_conf_var

    @staticmethod
    def data_schema_test():
        pass

    @staticmethod
    def data_splitter_test():
        pass


if __name__ == '__main__':
    UnitTests.config_load_test()
    UnitTests.data_schema_test()
    UnitTests.data_splitter_test()