import unittest
import updater
import datetime
from mock import *

# mock_datetime = Mock()
# mock_datetime.return_value = datetime(2018, 5, 10, 10, 0, 0)

class UpdaterTest(unittest.TestCase):

    EMPTY_REPOS_LIST_FILENAME = 'resources/empty_repos_list.txt'
    REPOS_LIST_FILENAME = 'resources/repos_list.txt'

    def test_empty_file_parsing(self):
        repos_list = updater.get_repos_list(self.EMPTY_REPOS_LIST_FILENAME)
        self.assertListEqual(repos_list, [])

    def test_file_parsing(self):
        repos_list = updater.get_repos_list(self.REPOS_LIST_FILENAME)
        self.assertListEqual(repos_list, ['containous/traefik'])

    def test_url_generation(self):
        url = updater.create_url('test/demo')
        self.assertEqual(url, 'https://github.com/test/demo/releases.atom')

    @patch.object(updater, 'datetime', Mock(wraps=datetime.datetime))
    def test_release_is_25h_old(self):
        updater.datetime.now.return_value = datetime.datetime(2018, 5, 10, 10, 0, 0)
        self.assertFalse(updater.is_datetime_in_last_24h(datetime.datetime(2018, 5, 9, 9, 0, 0)))

    @patch.object(updater, 'datetime', Mock(wraps=datetime.datetime))
    def test_release_is_23h_old(self):
        updater.datetime.now.return_value = datetime.datetime(2018, 5, 10, 10, 0, 0)
        self.assertTrue(updater.is_datetime_in_last_24h(datetime.datetime(2018, 5, 9, 11, 0, 0)))

    @patch.object(updater, 'datetime', Mock(wraps=datetime.datetime))
    def test_release_is_24h_old(self):
        updater.datetime.now.return_value = datetime.datetime(2018, 5, 10, 10, 0, 0)
        self.assertTrue(updater.is_datetime_in_last_24h(datetime.datetime(2018, 5, 9, 10, 0, 0)))


if __name__ == '__main__':
    unittest.main()
