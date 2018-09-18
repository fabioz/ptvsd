from _pydevd_bundle.pydevd_io import IORedirector


def test_io_redirector():

    class MyRedirection1(object):
        pass

    class MyRedirection2(object):
        pass

    # Check that we don't fail creating the IORedirector if the original
    # doesn't have a 'buffer'.
    IORedirector(MyRedirection1(), MyRedirection2(), wrap_buffer=True)


class DummyWriter(object):

    __slots__ = ['commands', 'command_meanings']

    def __init__(self):
        self.commands = []
        self.command_meanings = []

    def add_command(self, cmd):
        from _pydevd_bundle.pydevd_comm import ID_TO_MEANING
        meaning = ID_TO_MEANING[str(cmd.id)]
        self.command_meanings.append(meaning)
        self.commands.append(cmd)


def test_debug_console():
    from _pydev_bundle.pydev_console_utils import DebugConsoleStdIn
    from pydevd import PyDB
    from tests_python.test_tracing_on_top_level import DummyWriter

    class OriginalStdin(object):

        def readline(self):
            return 'read'

    original_stdin = OriginalStdin()

    py_db = PyDB(set_as_global=False)
    py_db.writer = DummyWriter()
    debug_console_std_in = DebugConsoleStdIn(py_db, original_stdin)
    assert debug_console_std_in.readline() == 'read'

    assert py_db.writer.command_meanings == ['CMD_INPUT_REQUESTED', 'CMD_INPUT_REQUESTED']

