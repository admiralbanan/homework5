import unittest
from file_manager import read_balance, save_balance, read_history, save_history, save_directory_contents

class TestFileManager(unittest.TestCase):

    def test_read_balance(self):
        save_balance(100.0)
        self.assertEqual(read_balance(), 100.0)

    def test_read_history(self):
        save_history([('еда', 50)])
        self.assertEqual(read_history(), [('еда', 50)])

    def test_save_directory_contents(self):
        save_directory_contents()
        with open('listdir.txt', 'r') as f:
            content = f.read()
        self.assertTrue('files:' in content)
        self.assertTrue('dirs:' in content)

if __name__ == '__main__':
    unittest.main()
