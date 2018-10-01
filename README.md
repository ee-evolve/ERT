# ERT aka Evolve/EqualExperts/Elephant Release Tracker (pick your fav)

Get notified of new releases to your favorite github projects via slack.

## Architecture

The [updater.py](updater.py) checks each midnight for new releases based on the content of the [configuration file](repos.txt) and sends a notification via slack.

We're currently running this scheduled job via circleci, please see [circleci config](.circleci/config.yml) for further details.

## Usage

Feel free to clone/fork the repo, update the `repos.txt` and in circleci add a new environment variable called `SLACK_WEBHOOK`.

## Contributing and testing

Tests are run as part of the build, locallyy you can try and run the dockerbuild.

```
docker build -t ert:0.1 .
```

Contributions are welcome, feel free to open a PR, the project is still under heavy development.
