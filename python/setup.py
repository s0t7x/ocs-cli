from distutils.core import setup
import py2exe

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console = [{'script': "decompress.py"}, {'script': "compress.py"}],
    zipfile = None,
)