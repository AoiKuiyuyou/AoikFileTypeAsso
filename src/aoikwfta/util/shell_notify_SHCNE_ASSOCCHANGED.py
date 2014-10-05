# coding: utf-8
"""
File ID: 8zFo0Aj
"""

import sys

def main():
    #/
    print >> sys.stderr, '#/ Send shell change notification, to make changes take effect.'
        
    try:
        import win32com.shell.shell as shell
        import win32com.shell.shellcon as shellcon
    except ImportError:
        print >> sys.stderr, 'Error:'
        print >> sys.stderr, 'Importing |win32com| failed.'
        print >> sys.stderr, 'Please install |pywin32|.'
        dl_url = r'http://sourceforge.net/projects/pywin32/files/pywin32/'
        print >> sys.stderr, 'Download is available at {}.'.format(dl_url)
        return 1
        
    #/
    shell.SHChangeNotify(
        shellcon.SHCNE_ASSOCCHANGED,
        shellcon.SHCNF_IDLIST,
        None,
        None,
    )
    
    print >> sys.stderr, 'Ok'
    
    #/
    return 0
   
if __name__ == '__main__':
    sys.exit(main())
    