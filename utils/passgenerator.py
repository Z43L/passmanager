import random
import string


def generate_password(lent, caracteres, numbers, uppercase, lowercase):
    all_chars = ""
    if caracteres:
        all_chars += string.punctuation
    if numbers:
        all_chars += string.digits
    if uppercase:
        all_chars += string.ascii_uppercase
    if lowercase:
        all_chars += string.ascii_lowercase

    password = ''.join(random.choice(all_chars) for _ in range(lent))
    return password

