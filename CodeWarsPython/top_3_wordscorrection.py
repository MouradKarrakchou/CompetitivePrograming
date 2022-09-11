import re
from collections import Counter
from re import Pattern


def top_3_words(text):
    re.match("[a-z]",)
    c = Counter(re.findall(r"[']*[a-z][a-z']*",  text.lower()))
    return [w for w,_ in c.most_common(3)]

def top_3_wordsv2(text):
    re_non_valid = re.compile('[^a-z\' ]')
    re_chars = re.compile('[a-z]')
    text = text.lower()
    text = ' '.join([x for x in re_non_valid.sub(' ',text).split() if re_chars.search(x)])
    words = {}
    top = {}                    # Dictionary with no more than 3 words
    for word in text.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
        top[word] = words[word] # Add the new word to the top
        if len(top) > 3:        # If the top is too big remove the worst word
            top.pop(min(top, key=top.get))
    return sorted(top, key=top.get, reverse=True)