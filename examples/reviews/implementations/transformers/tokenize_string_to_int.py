import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

non_word = re.compile("\\W")


def transform_python(sample, args):
    text = sample["col"].lower()
    token_index_list = []

    stop_words = set(stopwords.words("english"))

    for token in non_word.split(text):
        if len(token) == 0:
            continue
        if token in stop_words:
            continue
        token_index_list.append(0)
        if len(token_index_list) == args["max_len"]:
            break

    for i in range(args["max_len"] - len(token_index_list)):
        token_index_list.append(1)

    return token_index_list
