from string import ascii_letters, digits
from random import choice

chars = ascii_letters + digits + '.,?!&%$#'

def generate_password():
    s = ''
    for i in range(15):
        s += choice(chars)
    return s

def main(func):
    password = generate_password()
    print(password)

if __name__ == '__main__':
    main(generate_password)