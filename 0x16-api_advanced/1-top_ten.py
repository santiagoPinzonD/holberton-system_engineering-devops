#!/usr/bin/python3
""" file with function that return 10 top
"""

import requests


def top_ten(subreddit):
    """Write a function that queries the Reddit API and prints
        the titles of the first 10 hot posts listed for a given subreddit."""
    URL = "https://www.reddit.com/r/{}/hot.json?limit=10"
    headers = {'User-Agent': 'URL'}
    response = requests.get(URL.format(subreddit), headers=headers)
    post = response.json().get('data')
    children = post.get('children')
    for posts in children:
        print(posts.get('data').get('title'))
