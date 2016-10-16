import sys
from subprocess import call, Popen

def snipe_import_exceptions(exctype, value, traceback):
    ''' Function to monkeypatch excepthook that looks
        for ImportError and attempts to install the
        missing package.
    '''
    if exctype == ImportError:
        package = str(value).rsplit(None, 1)[-1]
        abort = install_module(package)
        if not abort:
            # restart the script that encountered the
            # ImportError
            call(['python', sys.argv[0]])
    else:
        sys.__excepthook__(exctype, value, traceback)

sys.excepthook = snipe_import_exceptions

def install_module(package):
    ''' Function that makes a system call to pip
        install a package
    '''
    proc = Popen(['sudo', 'pip', 'install', package])
    output = proc.communicate()
    result = proc.returncode
    return result
