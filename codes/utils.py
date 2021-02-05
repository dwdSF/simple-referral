import random
import string


def code_generator(size=6, chars=string.ascii_uppercase + string.digits):
    ''' The function generates a random string of both letters and numbers.
    Used for SMS codes and invite codes.'''

    return ''.join(random.choice(chars) for _ in range(size))
