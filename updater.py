import atoma
import requests


def get_repos_list(filename):
    if not filename:
        raise Exception("Invalid filename")

    with open(filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    return content


def create_url(repo_name):
    return 'https://github.com/' + repo_name + '/releases.atom'


def main():
    response = requests.get('http://lucumr.pocoo.org/feed.atom')
    feed = atoma.parse_atom_bytes(response.content)
    print(feed)


if __name__ == '__main__':
    main()
