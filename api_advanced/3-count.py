#!/usr/bin/python3
"""comment"""
import requests


def count_words(subreddit, word_list, after="", total_words={}):
    """"comments"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=100" \
        .format(subreddit)
    header = {'User-Agent': 'Mozilla/5.0'}
    param = {'after': after}
    response = requests.get(url, headers=header, params=param)

    if response.status_code != 200:
        return

    response_json = response.json()
    after = response_json.get('data').get('after')
    has_next = after is not None
    hot_titles = []
    words = [word.lower() for word in word_list]

    if len(total_words) == 0:
        total_words = {word: 0 for word in words}

    hot_articles = response_json.get('data').get('children')
    [hot_titles.append(article.get('data').get('title'))
     for article in hot_articles]

    # loop through all titles
    for i in range(len(hot_titles)):
        for title_word in hot_titles[i].lower().split():
            for word in words:
                if word.lower() == title_word:
                    total_words[word] = total_words.get(word) + 1

    if has_next:
        return count_words(subreddit, word_list, after, total_words)
    else:

        total_words = dict(filter(lambda item: item[1] != 0,
                                  total_words.items()))

        total_words = sorted(total_words.items(),
                             key=lambda item: item[1],
                             reverse=True)

        for i in range(len(total_words)):
            print("{}: {}".format(total_words[i][0],
                                  total_words[i][1]))
