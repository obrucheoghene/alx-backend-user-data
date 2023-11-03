#!/usr/bin/env python3
"""
Encrypting passwords Module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    Encrypting passwords
    """
    encoded = password.encode()
    hashed = bcrypt.hashpw(encoded, bcrypt.gensalt())

    return hashed


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    Check valid password
    """
    valid = False
    encoded = password.encode()
    if bcrypt.checkpw(encoded, hashed_password):
        valid = True
    return valid
