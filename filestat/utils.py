#!/usr/bin/python3

import os as _os
from datetime import datetime as _datetime
import pwd as _pwd
import grp as _grp
import getpass as _getpass


def get_user_name() -> str:
    """Return current user name.


    Returns:
    str -- current user name"""

    return _getpass.getuser()


def get_group_name(user: str = None) -> str:
    """Retun current group name of current user.


    Keyword arguments:
    user(str) -- user name search to be in group (default None)

    Returns:
    str -- group of current given user"""

    if user is None:
        user = get_user_name()
    group_id = _pwd.getpwnam(user).pw_gid

    return _grp.getgrgid(group_id).gr_name


def get_size(name: str) -> int:
    """A function that return file size in bytes.


    Keyword arguments:
    name -- the file name

    Returns:
    int -- file size in bytes"""

    try:
        stats = _os.stat(name)
    except FileNotFoundError:
        raise FileNotFoundError(f'{name} this file does not exists, make' \
                                     ' sure you input correct file name.')
    except Exception:
        raise

    return stats.st_size


def get_permissions(name: str) -> int:
    """A function that return file permission in octal as int.


    Keyword arguments:
    name -- the file name to be test

    Returns:
    int -- file permission in oct"""

    try:
        stats = _os.stat(name)
    except FileNotFoundError:
        raise FileNotFoundError(f'{name} this file does not exists, make' \
                                     ' sure you input correct file name.')
    except Exception:
        raise

    return int(oct(stats.st_mode)[-3:])


def get_last_access_time(name: str) -> str:
    """A function that return last access date time of a file.


    Keyword arguments:
    name -- the file name to be test

    Returns:
    str -- date time of last access"""

    try:
        stats = _os.stat(name)
    except FileNotFoundError:
        raise FileNotFoundError(f'{name} this file does not exists, make'\
                                ' sure you input correct file name.')
    except Exception:
        raise
    time_stamp = _datetime.fromtimestamp(stats.st_atime)

    return time_stamp.strftime("%A, %B %d, %Y %I:%M:%S.%f %p")


def creation_time(name: str) -> str:
    """Function return last modification date time or the creation date time.


    Keyword arguments:
    name -- the file name

    Returns:
    str -- file creation date time"""

    try:
        stats = _os.stat(name)
    except FileNotFoundError:
        raise FileNotFoundError(f'{name} this file does not exists, make'\
                                ' sure you input correct file name.')
    except Exception:
        raise
    time_stamp = _datetime.fromtimestamp(stats.st_mtime)

    return time_stamp.strftime("%A, %B %d, %Y %I:%M:%S.%f %p")


def get_owner_info(name: str) -> str:
    """A function that return owner name of a file


    Keyword arguments:
    name -- the file name to be test

    Returns:
    str -- file owner name"""

    try:
        stats = _os.stat(name)
    except FileNotFoundError:
        raise FileNotFoundError(f'{name} this file does not exists, make'\
                                ' sure you input correct file name.')
    except Exception:
        raise
    owner = _pwd.getpwuid(stats.st_uid)

    return owner.pw_name


def get_group_info(name: str) -> str:
    """A function that return group info of a file

    Keyword arguments:
    name(str) -- the file name

    Returns:
    str -- group name of a file"""

    try:
        stats = _os.stat(name)
    except FileNotFoundError:
        raise FileNotFoundError(f'{name} this file does not exists, make' \
                                ' sure you input correct file name.')
    except Exception:
        raise
    group = _grp.getgrgid(stats.st_uid)

    return group.gr_name


def check_owner(owner: str, fp_name: str) -> bool:
    """A function that cross check file owner name


    Keyword arguments:
    owner(str) -- owner name
    fp_name(str) -- the file name

    Returns:
    bool -- True/False"""

    confirm = False
    try:
        if get_owner_info(fp_name) == owner:
            confirm = True
    except FileNotFoundError:
        raise FileNotFoundError(f'{fp_name} this file does not exists, make' \
                                ' sure you input correct file name.')
    except Exception:
        raise

    return confirm


def check_group(owner: str, fp_name: str) -> bool:
    """A function that cross check file group name


    Keyword arguments:
    owner(str) -- the group name
    fp_name(str) -- the file name

    Returns:
    bool -- True/Fale"""

    confirm = False
    try:
        if get_group_info(fp_name) == owner:
            confirm = True
    except FileNotFoundError:
        raise FileNotFoundError(f'{fp_name} this file does not exists, make' \
                                ' sure you input correct file name.')
    except Exception:
        raise

    return confirm


def readable(fp_name: str) -> bool:
    """Function that return a file readable or not


    Keyword arguments:
    fp_name(str) -- the file name

    Returns:
    bool -- True/False"""

    confirm = False
    try:
        if _os.access(fp_name, _os.R_OK):
            confirm = True
    except FileNotFoundError:
        raise FileNotFoundError(f'{fp_name} this file does not exists, make' \
                                ' sure you input correct file name.')
    except Exception:
        raise

    return confirm


def writable(fp_name: str) -> bool:
    """Function return boolean about the file writable or not!


    Keyword arguments:
    fp_name(str) -- the file name

    Returns:
    bool -- True/False"""

    confirm = False
    try:
        if _os.access(fp_name, _os.W_OK):
            confirm = True
    except FileNotFoundError:
        raise FileNotFoundError(f'{fp_name} this file does not exists, make' \
                                ' sure you input correct file name.')
    except Exception:
        raise

    return confirm


def executable(fp_name: str) -> bool:
    """Function return boolean about the file executable or not!


    Keyword arguments:
    fp_name(str) -- the file name

    Returns:
    bool -- True/False"""

    confirm = False

    try:
        if _os.access(fp_name, _os.X_OK):
            confirm = True
    except FileNotFoundError:
        raise FileNotFoundError(f'{fp_name} this file does not exists, make'\
                                ' sure you input correct file name.')
    except Exception:
        raise

    return confirm
