import unittest
from triplayacc import parser
from syntax import *

class MyTestCase(unittest.TestCase):
    def test_simple_if_statement(self):
        input_code = "if (true) then 1 else 0"
        ast = parser.parse(input_code)
        expected_output = IF(CONST(True), CONST(1), CONST(0))
        #print(str(ast))
        #print(str(expected_output))
        self.assertEqual(str(ast), str(expected_output))


if __name__ == '__main__':
    unittest.main()
