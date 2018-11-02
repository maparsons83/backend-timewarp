import random
import uuid

def count_key(key):
    score = 0
    for char in key:
        score += ord(char)
    return score


def generate_key():
    while True:
        key = str(uuid.uuid4())
        if count_key(key) == 2041:
            break
    return key

key = generate_key()

def validate_key(key):
    if count_key(key) == 2041 and key[14] == '4':
        return True
    else:
        return False


if __name__ == '__main__':
    """Good key test"""
    if validate_key(key) == True:
        print(key, ': is valid')

    """Bad key test"""
    if validate_key('2e106301-48b3-4425-9766-602739c194c9') == False:
        print('2e106301-48b3-4425-9766-602739c194c8 is not a valid key')

        
     