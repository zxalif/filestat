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
