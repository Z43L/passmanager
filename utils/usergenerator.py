import random
import string


def user_generator(lent, numbers, uppercase, lowercase):
    all_chars = ""
    if numbers:
        all_chars += string.digits
    if uppercase:
        all_chars += string.ascii_uppercase
    if lowercase:
        all_chars += string.ascii_lowercase

    user = ''.join(random.choice(all_chars) for _ in range(lent))
    return user

