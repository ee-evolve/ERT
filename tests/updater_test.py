import unittest
import updater


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


if __name__ == '__main__':
    unittest.main()
