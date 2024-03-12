#!/usr/bin/python3
"""
Unnitest for console
"""

import unittest
from console import HBNBCommand
from models.base_model import BaseModel
from unittest.mock import patch
from models import storage
from io import StringIO


class TestConsole(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.console = HBNBCommand()

    def setUp(self):
        self.console.preloop()

    def tearDown(self):
        self.console.postloop()

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, mock_stdout, command):
        self.console.onecmd(command)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_all_commands(self):
        storage.reset()

        # Testing Create
        expected_output = "f1r57-1n574nc3\n"
        self.assert_stdout(expected_output, "create BaseModel")
        objct = storage.all()['BaseModel.f1r57-1n574nc3']

        # Testing Show
        expect_output = str(objct) + '\n'
        self.assert_stdout(expect_output, "show BaseModel {}".format(objct.id))

        # Testing Destroy
        self.assert_stdout("", "destroy BaseModel {}".format(objct.id))
        self.assertNotIn(objct, storage.all().values())

        # Testing All
        objct1 = BaseModel()
        objct2 = BaseModel()
        expected_output = "[{}, {}]\n".format(str(objct1), str(objct2))
        self.assert_stdout(expected_output, "all BaseModel")

        # Testing Update
        self.assert_stdout(
            "",
            'update BaseModel {} name "New Name"'.format(objct1.id)
        )
        updated_obj = storage.all()['BaseModel.' + objct1.id]
        self.assertEqual(updated_obj.name, "New Name")

    def test_invalid_commands(self):
        storage.reset()

        # Testing Invalid show command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "show InvalidClass")

        # Testing Invalid create command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "create InvalidClass")

        # Testing Invalid destroy command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "destroy InvalidClass")

        # Testing Invalid update command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "update InvalidClass")

        # Testing Invalid all command
        expected_output = "** class doesn't exist **\n"
        self.assert_stdout(expected_output, "all InvalidClass")

    def test_empty_line_quit_commands(self):
        # Testing Empty line
        expected_output = ""
        self.assert_stdout(expected_output, "")

    def test_help_commands(self):
        # Testing help command
        expected_output = "Quit command to exit the program\n"
        self.assert_stdout(expected_output, "help quit")

        # Testing Quit command
        self.assertTrue(self.console.onecmd("quit"))


if __name__ == '__main__':

    unittest.main()
