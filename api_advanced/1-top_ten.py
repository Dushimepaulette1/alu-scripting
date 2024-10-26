#!/usr/bin/python3
"""Script that fetches the top 10 hot posts for a given subreddit."""

import requests


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints 'None'.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title'))
            else:
                print("None")
        else:
            print("None")
    except requests.RequestException:
        print("None")
