import unittest
from filemanager import create_folder, delete_file_folder, copy_file_folder, list_folders, list_files

class TestFileManager(unittest.TestCase):

    def test_create_folder(self):
        create_folder('test_folder')
        self.assertTrue(os.path.exists('test_folder'))

    def test_delete_folder(self):
        delete_file_folder('test_folder')
        self.assertFalse(os.path.exists('test_folder'))

    def test_copy_folder(self):
        create_folder('test_folder')
        copy_file_folder('test_folder', 'test_folder_copy')
        self.assertTrue(os.path.exists('test_folder_copy'))

    def test_list_folders(self):
        result = list_folders()
        self.assertIn('test_folder', result)

    def test_list_files(self):
        result = list_files()
        self.assertIn('test_file.txt', result)

if __name__ == '__main__':
    unittest.main()
