import urllib.request
import os
import json


def send_slack_message(message):
    '''
    Send slack message
    '''
    try:
        slack_webhook = os.environ["SLACK_WEBHOOK"]
    except KeyError as er:
        print("Please set %s environment variable" % (er))
        raise

    data = { 'username': 'ERT', 'attachments': [{'color': 'green', 'text': message, "mrkdwn": "true"}]}

    req = urllib.request.Request(slack_webhook)
    req.add_header('Content-Type', 'application/json')

    try:
        response = urllib.request.urlopen(req, json.dumps(data).encode('utf8'))
    except Exception as e:
        if hasattr(e, 'reason'):
            print('Reason:', e.reason)
        if hasattr(e, 'code'):
            print('Error code:', e.code)