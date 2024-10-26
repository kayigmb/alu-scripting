#!/usr/bin/python3
"""Comment"""
import requests as req


def top_ten(subreddit):
    """ "top ten"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    res = req.get(url, headers={"User-Agent": "Mozilla/5.0"})

    if res.status_code != 200:
        print(None)

    json_response = res.json()
    posts = json_response.get("data").get("children")
    [print(post.get("data").get("title")) for post in posts]
