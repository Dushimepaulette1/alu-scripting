#!/usr/bin/python3
"""Fetch and display the top 10 hot posts of a given subreddit."""
import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts listed for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        
    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        # Check for successful status code and valid JSON response
        if response.status_code == 200:
            json_data = response.json().get('data', {}).get('children', [])
            if json_data:
                for post in json_data:
                    print(post.get('data', {}).get('title'))
            else:
                print(None)
        else:
            print(None)
    except (requests.RequestException, ValueError):
        print(None)
