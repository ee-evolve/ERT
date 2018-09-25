import atoma
import requests

REPOS_FILENAME = ''

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



def main():
    repos_list = get_repos_list(REPOS_FILENAME)
    urls = map(create_url, repos_list)
    response = requests.get(url)
    feed = atoma.parse_atom_bytes(response.content)
    print(feed)


if __name__ == '__main__':
    main()
