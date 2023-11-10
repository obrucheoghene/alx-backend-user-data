#!/usr/bin/env python3
"""
Module for authentication
"""


from typing import List, TypeVar
from flask import request


class Auth:
    """Auth
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """require_auth

        Args:
                path (str): _description_
                excluded_paths (List[str]): _description_

        Returns:
                bool: _description_
        """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
                    return False

        return True

    def authorization_header(self, request=None) -> str:
        """authorization_header

        Args:
                request (_type_, optional): _description_. Defaults to None.

        Returns:
                str: _description_
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')

        if header is None:
            return None

        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """current_user
        """

        return None
