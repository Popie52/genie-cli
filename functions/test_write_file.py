import unittest
from write_file import write_file  # Import the function we just wrote

class TestWriteFile(unittest.TestCase):

    def test_write_lorem_txt(self):
        print("\nwrite_file_content('calculator', 'lorem.txt', 'wait, this isn\\'t lorem ipsum'):")
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)

        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Successfully") or result.startswith("Error:"))

    def test_write_pkg_morelorem_txt(self):
        print("\nwrite_file_content('calculator', 'pkg/morelorem.txt', 'lorem ipsum dolor sit amet'):")
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)

        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Successfully") or result.startswith("Error:"))

    def test_write_outside_directory(self):
        print("\nwrite_file_content('calculator', '/tmp/temp.txt', 'this should not be allowed'):")
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)

        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))

if __name__ == "__main__":
    unittest.main()
