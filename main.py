#!/usr/bin/env python3.6
from user import User
from credentials import Credetials

def create_user(first_name, last_name, username, password):
    return User(first_name, last_name, username, password)
