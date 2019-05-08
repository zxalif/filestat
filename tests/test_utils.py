import unittest
from filestat import utils
import getpass as _getpass
import pwd as _pwd
import grp as _grp


class _Files:
    file_name = 'test_utils.py'
    file_that_not_exists = 'the_file.py'


class TestUser(unittest.TestCase):
    def test_user_name(self):
        self.assertEqual(utils.get_user_name(), _getpass.getuser())

    def test_group_name(self):
        self.assertEqual(utils.get_group_name(), self._group())

    def _group(self):
        user = utils.get_user_name()
        group_id = _pwd.getpwnam(user).pw_gid
        return _grp.getgrgid(group_id).gr_name


class TestGetSize(unittest.TestCase, _Files):

    def test_get_size(self):

        self.assertIsInstance(utils.get_size(self.file_name), int)

    def test_get_size_file_error(self):
        with self.assertRaises(FileNotFoundError):
            utils.get_size(self.file_that_not_exists)


class TestGetPermissions(unittest.TestCase, _Files):

    def test_get_size(self):

        self.assertIsInstance(utils.get_permissions(self.file_name), int)

    def test_get_size_file_error(self):
        with self.assertRaises(FileNotFoundError):
            utils.get_permissions(self.file_that_not_exists)


class TestAccessTime(unittest.TestCase, _Files):

    def test_get_size(self):

        self.assertIsInstance(utils.get_last_access_time(self.file_name), str)

    def test_get_size_file_error(self):
        with self.assertRaises(FileNotFoundError):
            utils.get_last_access_time(self.file_that_not_exists)


class TestCreateTime(unittest.TestCase, _Files):

    def test_get_size(self):

        self.assertIsInstance(utils.creation_time(self.file_name), str)

    def test_get_size_file_error(self):
        with self.assertRaises(FileNotFoundError):
            utils.creation_time(self.file_that_not_exists)


class TestOwnerInfo(unittest.TestCase, _Files):

    def test_get_size(self):

        self.assertIsInstance(utils.get_owner_info(self.file_name), str)

    def test_get_size_file_error(self):
        with self.assertRaises(FileNotFoundError):
            utils.get_owner_info(self.file_that_not_exists)


class TestGroupInfo(unittest.TestCase, _Files):

    def test_get_size(self):

        self.assertIsInstance(utils.get_group_info(self.file_name), str)

    def test_get_size_file_error(self):
        with self.assertRaises(FileNotFoundError):
            utils.get_group_info(self.file_that_not_exists)


class TestOwner(unittest.TestCase, _Files):

    def test_get_size(self):

        self.assertIsInstance(utils.check_owner(_getpass.getuser(), self.file_name), bool)


class TestGroup(unittest.TestCase, _Files):

    def test_get_size(self):

        self.assertIsInstance(utils.check_group(utils.get_group_name(), self.file_name), bool)
