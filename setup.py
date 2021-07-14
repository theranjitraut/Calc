import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\Ranjit\AppData\Local\Programs\Python\Python38-32\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\Ranjit\AppData\Local\Programs\Python\Python38-32\tcl\tk8.6"

executables = [cx_Freeze.Executable("calc.py", base=base, icon="1.ico")]


cx_Freeze.setup(
    name = "Calc",
    options = {"build_exe": {"packages":["tkinter","parser"], "include_files":["1.ico",'tcl86t.dll','tk86t.dll']}},
    version = "0.01",
    description = "Tkinter Application",
    executables = executables
    )
