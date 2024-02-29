# This code is from ChatGPT

import secrets
import string

def generate_random_string(length=32):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))
