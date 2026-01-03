import unittest
from get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):

    def test_current_directory(self):
        print("\nget_files_info('calculator', '.'):")
        result = get_files_info("calculator", ".")
        print(result)

        self.assertIsInstance(result, str)
        self.assertNotIn("Error:", result)

    def test_pkg_directory(self):
        print("\nget_files_info('calculator', 'pkg'):")
        result = get_files_info("calculator", "pkg")
        print(result)

        self.assertIsInstance(result, str)
        self.assertNotIn("Error:", result)

    def test_outside_directory_bin(self):
        print('\nget_files_info("calculator", "/bin"):')
        result = get_files_info("calculator", "/bin")
        print(result)

        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))

    def test_outside_directory_parent(self):
        print('\nget_files_info("calculator", "../"):')
        result = get_files_info("calculator", "../")
        print(result)

        self.assertIsInstance(result, str)
        self.assertTrue(result.startswith("Error:"))


if __name__ == "__main__":
    unittest.main()
