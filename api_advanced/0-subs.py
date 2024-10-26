#!/usr/bin/python3
""""Comments"""
import requests as req


def number_of_subscribers(subreddit):
    """Comments"""
    redit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = req.get(redit_url, headers={"User-Agent": "Mozilla/5.0"})

    if response.status_code != 200:
        return 0

    response_json = response.json()
    return response_json.get("data").get("subscribers")
