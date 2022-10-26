import random
import string


def get_random_string(length: int = 12, only_letters: bool = False):
    chars = string.ascii_letters
    if not only_letters:
        chars = chars + string.punctuation + string.digits
    result_str = ''.join(random.choice(chars) for i in range(length))
    return result_str
