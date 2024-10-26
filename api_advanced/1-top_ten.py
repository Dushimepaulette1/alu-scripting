#!/usr/bin/python3
"""Script that fetches the titles of the first 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit.
    
    If the subreddit does not exist, print None.
    """
    headers = {'User-Agent': 'MyAPI/0.0.1'}
    subreddit_url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        json_data = response.json().get('data', {}).get('children', [])
        if json_data:
            for post in json_data:
                print(post.get('data', {}).get('title'))
            print("OK")  # Print "OK" after printing the titles if the subreddit exists
        else:
            print("OK")  # Print "OK" if no posts are available
    else:
        print("None")  # Print "None" if the subreddit does not exist
