# coding: utf-8
"""
File ID: 8zFo0Aj
"""

import sys

def main():
    #/
    sys.stderr.write('#/ Send shell change notification, to make changes take effect.\n')
        
    try:
        import win32com.shell.shell as shell
        import win32com.shell.shellcon as shellcon
    except ImportError:
        sys.stderr.write(r"""Error:
Importing |win32com| failed.
Please install |pywin32|.
Download is available at http://sourceforge.net/projects/pywin32/files/pywin32/
""")
        
        return 1
        
    #/
    shell.SHChangeNotify(
        shellcon.SHCNE_ASSOCCHANGED,
        shellcon.SHCNF_IDLIST,
        None,
        None,
    )
    
    sys.stderr.write('OK\n')
    
    #/
    return 0
   
if __name__ == '__main__':
    sys.exit(main())
    