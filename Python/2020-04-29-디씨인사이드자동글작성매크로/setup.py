from cx_Freeze import setup, Executable
# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])
import sys
base = 'Win32GUI' if sys.platform=='win32' else None
executables = [
    Executable('DCXMacro.py', base=base)
]
setup(
    name='DCXMacro',
    version = '1.0.0',
    author = "XeroSoftware",
    description = 'DCINSIDE write macro program',
    options = dict(build_exe = buildOptions),
    executables = executables
)