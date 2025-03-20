#!/usr/bin/python3
""" Get the titles of the first 10 hot posts for a given subreddit."""
import requests

def top_ten(subreddit):
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            json_data = response.json()
            posts = json_data.get('data').get('children')
            if posts:
                for i in range(min(10, len(posts))):
                    print(posts[i].get('data').get('title'))
            else:
                print(None)
        except (ValueError, AttributeError, KeyError, TypeError):
            print(None)
    else:
        print(None)
