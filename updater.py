import atoma
import requests
from datetime import datetime, timedelta

REPOS_FILENAME = 'repos.txt'

def get_repos_list(filename):
    if not filename:
        raise Exception("Invalid filename")

    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def create_url(repo_name):
    return 'https://github.com/' + repo_name + '/releases.atom'


def get_atom_feed(url):
    return requests.get(url).content


def get_entries_from_parsed_atom_feed(parsed_atom_feed):
    return parsed_atom_feed['entries']


def is_datetime_in_last_24h(release_datetime):
    return datetime.now() - timedelta(hours=24) <= release_datetime


def main():
    repos_list = get_repos_list(REPOS_FILENAME)
    urls = list(map(create_url, repos_list))
    atom_feeds = list(map(get_atom_feed, urls))
    parsed_atom_feeds = map(lambda x: atoma.parse_atom_bytes(x), atom_feeds)

    print(list(parsed_atom_feeds))

if __name__ == '__main__':
    main()
