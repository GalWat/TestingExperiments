import random, string


def random_word(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def random_text(count=2, length=10):
    return " ".join([random_word(length) for _ in range(count)])
