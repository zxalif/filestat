========
filestat
========

.. _filestat: https://github.com/zxalif/filestat/
.. _MIT: https://choosealicense.com/licenses/mit/

filestat_ A command line library for file monitoring.

    :Authors: Alif Jahan
    :Version: 0.2 of 05/05/2019

**contents**
    - `Install`_
    - `Command`_
    - `Import`_
    - `User Info`_
    - `Group Info`_
    - `File`_

-----------
`Install`_
-----------

pip
===

To install `filestat` using pip

.. code-block:: bash

    $ pip install filestat

git
===

To install filestat using ``git`` just clone the repo

.. code-block:: bash

    $ git clone https://github.com/zxalif/filestat.git
    $ cd filestat
    $ pip install -e .

===========
`Command`_
===========

Using command line

.. code-block:: bash

    $ python3 -m filestat -f filename.py
    Name:	filename.py
    Owner:	alif
    Group:	alif
    Size:	1045 bytes
    Update Time: 	Sunday, May 05, 2019 10:50:11.640795 PM
    Last Access:	Sunday, May 05, 2019 10:50:15.200863 PM
    Permissions:	644
    Readable: 	True
    Writable:   True
    Executable:     False

==========
`Import`_
==========

.. code-block:: python

    >>> import filestat
    >>> # or
    >>> from filestat import utils
    >>> # or
    >>> from filestat.utils import *


==============
`User Info`_
==============

``get_user_name()`` return current user name

.. code-block:: python

    >>> from filestat import utils
    >>> utils.get_user_name()
    'alif'
    >>> help(utils.get_user_name)
    Help on function get_user_name in module filestat.utils:

    get_user_name() -> str
        Return current user name.


        Returns:
            str -- current user name

    >>>

==============
`Group Info`_
==============

``get_group_name(user)`` Return group name of current or given user user.

.. code-block:: python

    >>> from filestat import utils
    >>> utils.get_group_name('alif')
    'alif'
    >>>

By default the ``user`` parameter is ``None``. If no argument pass through the function then the function returns group name of current user.

.. code-block:: python

    >>> from filestat import utils
    >>> utils.get_group_name()
    'alif'
    >>>


==============
`File`_
==============

``get_permissions(name)`` function returns permission in octal as int. It takes file name as parameter.

.. code-block:: python

    >>> from filestat import utils
    >>> utils.get_permissions('file_name.py')
    755
    >>>

If the file doesn't exists the function return ``FileNotFoundError``.

``get_last_access_time(name)`` function returns last access date time of a give file name.

.. code-block:: python

    >>> from filestat import utils
    >>> utils.get_last_access_time('file_name.py')
    'Thursday, May 09, 2019 11:03:35.743453 PM'
    >>>

``creation_time(name)`` function return modification date time of a file or created date time.

.. code-block:: python

    >>> from filestat import utils
    >>> utils.creation_time('file_name.py')
    'Thursday, May 08, 2019 01:33:43.712453 PM'
    >>>

``get_owner_info(name)`` return the owner name of given file name.

.. code-block:: python

    >>> from filestat import utils
    >>> utils.get_owner_info('file_name.py')
    'alif'
    >>>

``get_group_info(name)`` function return group name that belongs to the file.

.. code-block:: python

    >>> from filestat import utils
    >>> utils.get_group_info('file_name.py')
    'alif'
    >>>

``check_owner(owner, fp_name)`` that check a owner is belongs to file or not. That requires two parameter ``owner`` name and ``fp_name`` the file name.

.. code-block:: python

    >>> from filestat import utils
    >>> utils.check_owner('alif','file_name.py')
    True
    >>>

``check_group(owner, fp_name)`` that check a group is belongs to file or not. That requires two parameter ``owner`` name and ``fp_name`` the file name.

.. code-block:: python

    >>> from filestat import utils
    >>> utils.check_group('alif','file_name.py')
    True
    >>>

``readable(fp_name)``, ``writable(fp_name)`` and ``executable(fp_name)`` return ``True/False`` if a file able read, write or executable by the current user.

.. code-block:: python

    >>> from filestat import utils
    >>> utils.readable('file_name.py')
    True
    >>> utils.writable('file_name.py')
    True
    >>> utils.executable('file_name.py')
    False
    >>>
