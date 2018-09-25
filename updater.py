import atoma
import requests
import slack
from datetime import datetime, timedelta, timezone

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
    return parsed_atom_feed.entries


def is_datetime_in_last_24h(release_datetime):
    return datetime.now(timezone.utc) - timedelta(hours=24) <= release_datetime


def retrieve_releases_in_last_24h(parsed_atom_feeds):
    entries = list(map(get_entries_from_parsed_atom_feed, parsed_atom_feeds))
    return filter(lambda x: is_datetime_in_last_24h(x.updated), entries[0])


def main():
    repos_list = get_repos_list(REPOS_FILENAME)
    urls = map(create_url, repos_list)
    atom_feeds = map(get_atom_feed, urls)
    parsed_atom_feeds = map(lambda x: atoma.parse_atom_bytes(x), atom_feeds)
    releases_last_24h = list(retrieve_releases_in_last_24h(parsed_atom_feeds))

    versions_list = list(map(lambda x: x.title.value, releases_last_24h))

    print(versions_list)

    slack.send_slack_message('New versions released: ' + ', '.join(versions_list))

if __name__ == '__main__':
    main()
