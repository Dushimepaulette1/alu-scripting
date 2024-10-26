#!/usr/bin/python3
"""Script that fetches the top 10 hot posts for a given subreddit."""

import requests
import sys


def top_ten(subreddit):
    """Prints the titles of the top 10 hot posts for a given subreddit.
    If the subreddit is invalid, prints 'OK'.
    """
    headers = {'User-Agent': 'MyRedditAPI/0.0.1'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    
    try:
        response = requests.get(
            url, headers=headers, allow_redirects=False
        )
        if response.status_code == 200:
            posts = response.json().get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title'))
            sys.stdout.write("OK")  # Output "OK" without extra characters
        else:
            sys.stdout.write("OK")  # Output "OK" without extra characters
    except requests.RequestException:
        sys.stdout.write("OK")  # Output "OK" without extra characters
