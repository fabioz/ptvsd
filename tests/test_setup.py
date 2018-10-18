import os.path
import unittest

from setup import iter_vendored_files


class IterVendoredFilesTests(unittest.TestCase):

    def test_all(self):
        filenames = set(iter_vendored_files())

        self.assertEqual(filenames, VENDORED)


VENDORED = {file.replace('/', os.path.sep) for file in [
    'pydevd/pydev_run_in_console.py',
    'pydevd/setup_cython.py',
    'pydevd/pydev_app_engine_debug_startup.py',
    'pydevd/pydevd_tracing.py',
    'pydevd/pydev_pysrc.py',
    'pydevd/pydevconsole.py',
    'pydevd/pydevd.py',
    'pydevd/pydev_coverage.py',
    'pydevd/pydevd_file_utils.py',
    'pydevd/pydevd_attach_to_process/attach_linux_x86.so',
    'pydevd/pydevd_attach_to_process/attach_pydevd.py',
    'pydevd/pydevd_attach_to_process/attach_amd64.dll',
    'pydevd/pydevd_attach_to_process/_test_attach_to_process.py',
    'pydevd/pydevd_attach_to_process/attach_linux_amd64.so',
    'pydevd/pydevd_attach_to_process/attach_x86.dll',
    'pydevd/pydevd_attach_to_process/_always_live_program.py',
    'pydevd/pydevd_attach_to_process/attach_x86.dylib',
    'pydevd/pydevd_attach_to_process/_check.py',
    'pydevd/pydevd_attach_to_process/README.txt',
    'pydevd/pydevd_attach_to_process/add_code_to_python_process.py',
    'pydevd/pydevd_attach_to_process/attach_x86_64.dylib',
    'pydevd/pydevd_attach_to_process/attach_script.py',
    'pydevd/pydevd_attach_to_process/_test_attach_to_process_linux.py',
    'pydevd/pydevd_attach_to_process/dll/attach.h',
    'pydevd/pydevd_attach_to_process/dll/python.h',
    'pydevd/pydevd_attach_to_process/dll/attach.cpp',
    'pydevd/pydevd_attach_to_process/dll/stdafx.h',
    'pydevd/pydevd_attach_to_process/dll/compile_dll.bat',
    'pydevd/pydevd_attach_to_process/dll/stdafx.cpp',
    'pydevd/pydevd_attach_to_process/dll/targetver.h',
    'pydevd/pydevd_attach_to_process/winappdbg/module.py',
    'pydevd/pydevd_attach_to_process/winappdbg/event.py',
    'pydevd/pydevd_attach_to_process/winappdbg/process.py',
    'pydevd/pydevd_attach_to_process/winappdbg/thread.py',
    'pydevd/pydevd_attach_to_process/winappdbg/disasm.py',
    'pydevd/pydevd_attach_to_process/winappdbg/textio.py',
    'pydevd/pydevd_attach_to_process/winappdbg/sql.py',
    'pydevd/pydevd_attach_to_process/winappdbg/util.py',
    'pydevd/pydevd_attach_to_process/winappdbg/crash.py',
    'pydevd/pydevd_attach_to_process/winappdbg/registry.py',
    'pydevd/pydevd_attach_to_process/winappdbg/breakpoint.py',
    'pydevd/pydevd_attach_to_process/winappdbg/search.py',
    'pydevd/pydevd_attach_to_process/winappdbg/compat.py',
    'pydevd/pydevd_attach_to_process/winappdbg/window.py',
    'pydevd/pydevd_attach_to_process/winappdbg/interactive.py',
    'pydevd/pydevd_attach_to_process/winappdbg/__init__.py',
    'pydevd/pydevd_attach_to_process/winappdbg/system.py',
    'pydevd/pydevd_attach_to_process/winappdbg/debug.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/shlwapi.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/kernel32.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/advapi32.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/__init__.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/psapi.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/defines.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/user32.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/dbghelp.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/version.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/peb_teb.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/context_amd64.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/shell32.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/ntdll.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/wtsapi32.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/context_i386.py',
    'pydevd/pydevd_attach_to_process/winappdbg/win32/gdi32.py',
    'pydevd/pydevd_attach_to_process/winappdbg/plugins/__init__.py',
    'pydevd/pydevd_attach_to_process/winappdbg/plugins/do_symfix.py',
    'pydevd/pydevd_attach_to_process/winappdbg/plugins/README',
    'pydevd/pydevd_attach_to_process/winappdbg/plugins/do_exchain.py',
    'pydevd/pydevd_attach_to_process/winappdbg/plugins/do_example.py',
    'pydevd/pydevd_attach_to_process/winappdbg/plugins/do_exploitable.py',
    'pydevd/pydevd_attach_to_process/linux/gdb_threads_settrace.py',
    'pydevd/pydevd_attach_to_process/linux/compile_mac.sh',
    'pydevd/pydevd_attach_to_process/linux/Makefile',
    'pydevd/pydevd_attach_to_process/linux/lldb_prepare.py',
    'pydevd/pydevd_attach_to_process/linux/compile_so.sh',
    'pydevd/pydevd_attach_to_process/linux/python.h',
    'pydevd/pydevd_attach_to_process/linux/attach_linux.c',
    'pydevd/pydevd_attach_to_process/linux/lldb_threads_settrace.py',
    'pydevd/_pydev_bundle/_pydev_imports_tipper.py',
    'pydevd/_pydev_bundle/_pydev_getopt.py',
    'pydevd/_pydev_bundle/pydev_umd.py',
    'pydevd/_pydev_bundle/fix_getpass.py',
    'pydevd/_pydev_bundle/pydev_is_thread_alive.py',
    'pydevd/_pydev_bundle/pydev_ipython_console.py',
    'pydevd/_pydev_bundle/_pydev_jy_imports_tipper.py',
    'pydevd/_pydev_bundle/pydev_imports.py',
    'pydevd/_pydev_bundle/pydev_override.py',
    'pydevd/_pydev_bundle/pydev_monkey.py',
    'pydevd/_pydev_bundle/pydev_localhost.py',
    'pydevd/_pydev_bundle/pydev_log.py',
    'pydevd/_pydev_bundle/pydev_ipython_console_011.py',
    'pydevd/_pydev_bundle/_pydev_tipper_common.py',
    'pydevd/_pydev_bundle/pydev_monkey_qt.py',
    'pydevd/_pydev_bundle/_pydev_log.py',
    'pydevd/_pydev_bundle/_pydev_filesystem_encoding.py',
    'pydevd/_pydev_bundle/pydev_versioncheck.py',
    'pydevd/_pydev_bundle/__init__.py',
    'pydevd/_pydev_bundle/_pydev_completer.py',
    'pydevd/_pydev_bundle/pydev_import_hook.py',
    'pydevd/_pydev_bundle/pydev_console_utils.py',
    'pydevd/_pydev_bundle/_pydev_calltip_util.py',
    'pydevd/pydevd_plugins/jinja2_debug.py',
    'pydevd/pydevd_plugins/django_debug.py',
    'pydevd/pydevd_plugins/__init__.py',
    'pydevd/pydevd_plugins/extensions/README.md',
    'pydevd/pydevd_plugins/extensions/__init__.py',
    'pydevd/pydevd_plugins/extensions/types/pydevd_plugin_numpy_types.py',
    'pydevd/pydevd_plugins/extensions/types/__init__.py',
    'pydevd/pydevd_plugins/extensions/types/pydevd_helpers.py',
    'pydevd/pydevd_plugins/extensions/types/pydevd_plugins_django_form_str.py',
    'pydevd/_pydev_runfiles/pydev_runfiles_coverage.py',
    'pydevd/_pydev_runfiles/pydev_runfiles_nose.py',
    'pydevd/_pydev_runfiles/pydev_runfiles_parallel.py',
    'pydevd/_pydev_runfiles/pydev_runfiles_pytest2.py',
    'pydevd/_pydev_runfiles/pydev_runfiles.py',
    'pydevd/_pydev_runfiles/pydev_runfiles_parallel_client.py',
    'pydevd/_pydev_runfiles/__init__.py',
    'pydevd/_pydev_runfiles/pydev_runfiles_xml_rpc.py',
    'pydevd/_pydev_runfiles/pydev_runfiles_unittest.py',
    'pydevd/pydevd_concurrency_analyser/pydevd_concurrency_logger.py',
    'pydevd/pydevd_concurrency_analyser/pydevd_thread_wrappers.py',
    'pydevd/pydevd_concurrency_analyser/__init__.py',
    'pydevd/_pydev_imps/_pydev_xmlrpclib.py',
    'pydevd/_pydev_imps/_pydev_execfile.py',
    'pydevd/_pydev_imps/_pydev_SimpleXMLRPCServer.py',
    'pydevd/_pydev_imps/_pydev_saved_modules.py',
    'pydevd/_pydev_imps/_pydev_sys_patch.py',
    'pydevd/_pydev_imps/_pydev_inspect.py',
    'pydevd/_pydev_imps/_pydev_SocketServer.py',
    'pydevd/_pydev_imps/_pydev_BaseHTTPServer.py',
    'pydevd/_pydev_imps/__init__.py',
    'pydevd/_pydev_imps/_pydev_pkgutil_old.py',
    'pydevd/_pydev_imps/_pydev_uuid_old.py',
    'pydevd/_pydevd_frame_eval/pydevd_frame_eval_cython_wrapper.py',
    'pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.c',
    'pydevd/_pydevd_frame_eval/pydevd_modify_bytecode.py',
    'pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.pyx',
    'pydevd/_pydevd_frame_eval/__init__.py',
    'pydevd/_pydevd_frame_eval/pydevd_frame_eval_main.py',
    'pydevd/_pydevd_frame_eval/pydevd_frame_evaluator.pxd',
    'pydevd/_pydevd_frame_eval/pydevd_frame_tracing.py',
    'pydevd/pydev_ipython/inputhookpyglet.py',
    'pydevd/pydev_ipython/inputhookgtk3.py',
    'pydevd/pydev_ipython/inputhookqt5.py',
    'pydevd/pydev_ipython/inputhookglut.py',
    'pydevd/pydev_ipython/matplotlibtools.py',
    'pydevd/pydev_ipython/inputhookqt4.py',
    'pydevd/pydev_ipython/inputhookwx.py',
    'pydevd/pydev_ipython/__init__.py',
    'pydevd/pydev_ipython/qt_loaders.py',
    'pydevd/pydev_ipython/inputhook.py',
    'pydevd/pydev_ipython/README',
    'pydevd/pydev_ipython/version.py',
    'pydevd/pydev_ipython/qt_for_kernel.py',
    'pydevd/pydev_ipython/inputhooktk.py',
    'pydevd/pydev_ipython/qt.py',
    'pydevd/pydev_ipython/inputhookgtk.py',
    'pydevd/_pydevd_bundle/pydevd_vm_type.py',
    'pydevd/_pydevd_bundle/pydevd_additional_thread_info_regular.py',
    'pydevd/_pydevd_bundle/pydevd_reload.py',
    'pydevd/_pydevd_bundle/pydevd_trace_dispatch_regular.py',
    'pydevd/_pydevd_bundle/pydevd_cython.pyx',
    'pydevd/_pydevd_bundle/pydevd_collect_try_except_info.py',
    'pydevd/_pydevd_bundle/pydevd_extension_utils.py',
    'pydevd/_pydevd_bundle/pydevd_stackless.py',
    'pydevd/_pydevd_bundle/pydevd_constants.py',
    'pydevd/_pydevd_bundle/pydevd_frame_utils.py',
    'pydevd/_pydevd_bundle/pydevd_dont_trace_files.py',
    'pydevd/_pydevd_bundle/pydevd_frame.py',
    'pydevd/_pydevd_bundle/pydevd_xml.py',
    'pydevd/_pydevd_bundle/pydevd_extension_api.py',
    'pydevd/_pydevd_bundle/pydevd_comm.py',
    'pydevd/_pydevd_bundle/pydevd_comm_constants.py',
    'pydevd/_pydevd_bundle/pydevd_kill_all_pydevd_threads.py',
    'pydevd/_pydevd_bundle/pydevd_traceproperty.py',
    'pydevd/_pydevd_bundle/pydevd_command_line_handling.py',
    'pydevd/_pydevd_bundle/pydevd_io.py',
    'pydevd/_pydevd_bundle/pydevd_dont_trace.py',
    'pydevd/_pydevd_bundle/pydevd_trace_dispatch.py',
    'pydevd/_pydevd_bundle/pydevd_signature.py',
    'pydevd/_pydevd_bundle/pydevd_import_class.py',
    'pydevd/_pydevd_bundle/pydevd_custom_frames.py',
    'pydevd/_pydevd_bundle/pydevd_additional_thread_info.py',
    'pydevd/_pydevd_bundle/pydevd_exec.py',
    'pydevd/_pydevd_bundle/pydevd_vars.py',
    'pydevd/_pydevd_bundle/pydevd_exec2.py',
    'pydevd/_pydevd_bundle/pydevd_cython_wrapper.py',
    'pydevd/_pydevd_bundle/pydevd_plugin_utils.py',
    'pydevd/_pydevd_bundle/pydevconsole_code_for_ironpython.py',
    'pydevd/_pydevd_bundle/pydevd_process_net_command.py',
    'pydevd/_pydevd_bundle/pydevd_resolver.py',
    'pydevd/_pydevd_bundle/pydevd_utils.py',
    'pydevd/_pydevd_bundle/pydevd_console.py',
    'pydevd/_pydevd_bundle/pydevd_referrers.py',
    'pydevd/_pydevd_bundle/pydevd_cython.c',
    'pydevd/_pydevd_bundle/pydevd_breakpoints.py',
    'pydevd/_pydevd_bundle/__init__.py',
    'pydevd/_pydevd_bundle/pydevd_trace_api.py',
    'pydevd/_pydevd_bundle/pydevd_save_locals.py',
    'pydevd/pydev_sitecustomize/sitecustomize.py',
    'pydevd/pydev_sitecustomize/__not_in_default_pythonpath.txt',
]}
