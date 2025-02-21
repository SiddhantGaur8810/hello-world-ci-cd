import unittest
from app import hello_world

class TestHelloWorld(unittest.Testcase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello, World")

if __name__ == "__main__":
    unittest.main()        