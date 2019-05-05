#!/usr/bin/python3

import os as _os
from datetime import datetime as _datetime
import pwd as _pwd
import grp as _grp


def get_size(name: str) -> int:
    """A function that return file size in bytes and other format."""
    try:
        stats = _os.stat(name)
    except FileNotFoundError:
        raise FileNotFoundError(f'{name} this file does not exists, make sure you input correct file name.')
    except Exception:
        raise
    return stats.st_size


def get_permissions(name: str) -> oct:
    """A function that return file permission in octal"""
    try:
        stats = _os.stat(name)
    except FileNotFoundError:
        raise FileNotFoundError(f'{name} this file does not exists, make sure you input correct file name.')
    except Exception:
        raise

    return oct(stats.st_mode)[-3:]  # return the last three digits


def get_last_access_time(name: str) -> str:
    """A function that return last access of a file in python datetime 'Sunday, May 05, 2019 06:54:41.533611 PM'"""
    try:
        stats = _os.stat(name)
    except FileNotFoundError:
        raise FileNotFoundError(f'{name} this file does not exists, make sure you input correct file name.')
    except Exception:
        raise

    return _datetime.fromtimestamp(stats.st_atime).strftime("%A, %B %d, %Y %I:%M:%S.%f %p")


def creation_time(name: str) -> str:
    """Function return last modification date or the creation date."""

    try:
        stats = _os.stat(name)
    except FileNotFoundError:
        raise FileNotFoundError(f'{name} this file does not exists, make sure you input correct file name.')
    except Exception:
        raise

    return _datetime.fromtimestamp(stats.st_mtime).strftime("%A, %B %d, %Y %I:%M:%S.%f %p")


def get_owner_info(name: str) -> str:
    """A function that return owner name of a file"""
    try:
        stats = _os.stat(name)
    except FileNotFoundError:
        raise FileNotFoundError(f'{name} this file does not exists, make sure you input correct file name.')
    except Exception:
        raise
    owner = _pwd.getpwuid(stats.st_uid)
    return owner.pw_name


def get_group_info(name: str) -> str:
    """A function that return group info of a file"""
    try:
        stats = _os.stat(name)
    except FileNotFoundError:
        raise FileNotFoundError(f'{name} this file does not exists, make sure you input correct file name.')
    except Exception:
        raise
    group = _grp.getgrgid(stats.st_uid)
    return group.gr_name


def check_owner(owner: str, fp_name: str) -> bool:
    """A function that cross check file owner name"""

    confirm = False
    try:
        if get_owner_info(fp_name) == owner:
            confirm = True
    except Exception:
        raise

    return confirm


def check_group(owner: str, fp_name: str) -> bool:
    """A function that cross check file group name"""

    confirm = False
    try:
        if get_group_info(fp_name) == owner:
            confirm = True
    except Exception:
        raise

    return confirm
