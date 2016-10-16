import sys
import subprocess

def snipe_import_exceptions(exctype, value, traceback):
    if exctype == ImportError:
        module = str(value).split(" ")[-1:][0]
        install_module(module)
    else:
        sys.__excepthook__(exctype, value, traceback)

sys.excepthook = snipe_import_exceptions

def install_module(module):
    print "installing module", module
    subprocess.call("sudo pip install %s" %module, shell=True)

