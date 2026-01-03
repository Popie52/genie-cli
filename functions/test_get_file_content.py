import unittest
from get_file_content import get_file_content


class TestFileContent(unittest.TestCase):

    def test_file_content_main(self):
        print("\nget_file_content('calculator', 'main.py'):")
        result = get_file_content("calculator", "main.py")
        print(result)

        # Basic sanity checks
        self.assertIsInstance(result, str)
        self.assertFalse(
            result.startswith("Error: Cannot read") or
            result.startswith("Error: File not found")
        )

    def test_file_content_pkg_file(self):
        print("\nget_file_content('calculator', 'pkg/calculator.py'):")
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)

        self.assertIsInstance(result, str)
        self.assertFalse(
            result.startswith("Error: Cannot read") or
            result.startswith("Error: File not found")
        )

    def test_file_content_outside_directory(self):
        print("\nget_file_content('calculator', '/bin/cat'):")
        result = get_file_content("calculator", "/bin/cat")
        print(result)

        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))

    def test_file_content_does_not_exist(self):
        print("\nget_file_content('calculator', 'pkg/does_not_exist.py'):")
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        print(result)

        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))


if __name__ == "__main__":
    unittest.main()
