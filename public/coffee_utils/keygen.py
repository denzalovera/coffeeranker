"""
created by: denz 04/28/2017
"""
import random


def generate_password(passwd_length):
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_-+,:;<>[]{}'
    passwd = ""

    for i in range(passwd_length):
        index = random.randrange(len(alphabet))
        passwd = passwd + alphabet[index]

    return passwd
