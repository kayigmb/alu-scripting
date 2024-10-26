#!/usr/bin/python3
"""Comment"""
import requests as req


def recurse(subreddit, hot_list=[], after=None):
    """returns"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = req.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"},
        params={"after": after},
        allow_redirects=False,
    )
    if res.status_code == 200:
        data = res.json().get("data")
        if data is not None:
            children = data.get("children")
            if children is not None:
                for child in children:
                    hot_list.append(child.get("data").get("title"))
                after = data.get("after")
                if after is not None:
                    return recurse(subreddit, hot_list, after)
                else:
                    return hot_list
        else:
            return hot_list
    return None
