import unittest
from run_python_file import run_python_file

class TestRunPythonFile(unittest.TestCase):

    def test_run_python_file(self):
        print("\nrun_python_file('calculator', 'main.py'):")
        result = run_python_file("calculator", "main.py")
        print(result)
        self.assertIsInstance(result, str)
        self.assertIn("Usage", result)  # Expect usage instructions

    def test_run_python_file_args(self):
        print("\nrun_python_file('calculator', 'main.py', ['3 + 5']):")
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)
        self.assertIsInstance(result, str)
        # Could contain STDOUT or STDERR, but should include the result of the calculation
        self.assertTrue("STDOUT" in result or "STDERR" in result)

    def test_run_python_file_test(self):
        print("\nrun_python_file('calculator', 'tests.py'):")
        result = run_python_file("calculator", "tests.py")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue("No output produced" in result or "STDOUT" in result or "STDERR" in result)

    def test_run_python_file_error(self):
        print("\nrun_python_file('calculator', '../main.py'):")
        result = run_python_file("calculator", "../main.py")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))

    def test_run_python_file_nonexist(self):
        print("\nrun_python_file('calculator', 'nonexistent.py'):")
        result = run_python_file("calculator", "nonexistent.py")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))

    def test_run_python_file_lorem(self):
        print("\nrun_python_file('calculator', 'lorem.txt'):")
        result = run_python_file("calculator", "lorem.txt")
        print(result)
        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))

if __name__ == "__main__":
    unittest.main()
