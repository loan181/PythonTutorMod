"""
Forward any file into a PythonTutor visualisation window.

By default the file "script.py" is loaded, but you can precise another file path as the first argument of this script
The server should already be launch before run this script to work correctly.

Created by Loan
"""

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote
from webbrowser import open_new_tab
from sys import argv

DEFAULT_FILE_TO_FORWARD = "script.py"
BOTTLE_SERVER = "http://localhost:8003/visualize.html#mode=edit&code="

file_to_forward = DEFAULT_FILE_TO_FORWARD
if len(argv) == 2:
	file_to_forward = argv[1]

open_new_tab(BOTTLE_SERVER + quote(open(file_to_forward).read()))
