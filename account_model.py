import string
from dataclasses import dataclass

@dataclass(frozen=True)
class account_model:
    user_name: string
    password: string

    def __init__(self, user_name, password):
        account_model.user_name = user_name
        account_model.password = password


def user_name():
    return account_model.user_name

def password():
    return account_model.password