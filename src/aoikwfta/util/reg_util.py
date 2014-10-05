# coding: utf-8
"""
File ID: 6cfsMBp
"""

import re

def ext_add_dot(ext):
    """
    |ext| will be added a heading dot if not already has one.
    """
    #/
    if ext.startswith('.'):
        dot_ext = ext
    else:
        dot_ext = '.' + ext

    #/
    return dot_ext

#/ 6kBjx3L
def reg_value_escape(txt):
    """
    Escape |\| and |"| in registry file.
    """
    return txt.replace('\\', r'\\').replace(r'"', r'\"')
    ## '\\' is Python escape for |\|

def hkcr_cls_make_defaulticon(cls, icon):
    """
    cls: HKCR class
    
    icon: icon path
    """
    #/
    res = '[HKEY_CLASSES_ROOT\\{}\\DefaultIcon]\n'.format(
        reg_value_escape(cls)
    )
    ## |\\| is Python escape for |\|
    ## |{}| is Python |format| function's placeholder
    ## |\n| is Python escape for newline
    
    #/
    icon_esc = reg_value_escape(icon)
    
    #/
    res += '@="{}"\n'.format(
        icon_esc
    )
    ## |@| in reg file means default field
    ## |"| in reg file quotes a value
    ## |{}| is Python |format| function's placeholder
    ## |\n| is Python escape for newline
    
    #/
    return res

#/ 5kjCjsn
def hkcr_cls_make_shell_command(cls, cmd_key, cmd_val):
    """
#/ For exmaple
If
 cls = 'aoikwfta.txt'
 cmd_key = 'open'
 cmd_val = '"D:\Software\Dev\IDE\Notepad++\0\dst\notepad++.exe" "%1" %*'
then result reg txt is:
---
[HKEY_CLASSES_ROOT\aoikwfta.txt\shell\open\command]
@="\"D:\\Software\\Dev\\IDE\\Notepad++\\0\\dst\\notepad++.exe\" \"%1\" %*"
---

Note at code 8fapUBz, |cmd_val|'s char |\| and |"| are escaped
 because the two chars are special chars in reg file.
    """
    
    #/
    res_txt = '[HKEY_CLASSES_ROOT\{}\shell\{}\command]\n'.format(
        cls,
        cmd_key,
    )

    #/ 8fapUBz
    cmd_val_esc = reg_value_escape(cmd_val)
    
    res_txt += '@="{}"\n'.format(cmd_val_esc)

    #/
    return res_txt

def hkcr_cls_make_shell_command_default(cls, cmd_key):
    #/
    res = '[HKEY_CLASSES_ROOT\\{}\\shell]\n@="{}"\n'.format(
        reg_value_escape(cls),
        reg_value_escape(cmd_key)
    )
    ## |\\| is Python escape for |\|
    ## |{}| is Python |format| function's placeholder
    ## |\n| is Python escape for newline
    ## |@| in reg file means default field name
    ## |"| in reg file quotes a value
    ## |{}| is python |format| function's placeholder
    ## |\n| is python escape for newline

    #/
    return res

def hkcr_cls_make_attr(cls, attr, val):
    """
    #/ 2nDvjL6
    #/ Escape
    |cls| will be escaped using |reg_value_escape| (6kBjx3L).
    |attr| will be escaped using |reg_value_escape| (6kBjx3L).
    |val| will be escaped using |reg_value_escape| (6kBjx3L).
    """
    #/
    res = '[HKEY_CLASSES_ROOT\\{}]\n'.format(
        reg_value_escape(cls),
    )
    ## |\\| is python escape
    ## |{}| is python |format| function's substitute placeholder
    ## |\n| is python escape

    #/
    attr_esc = reg_value_escape(attr)
    
    val_esc = reg_value_escape(val)
    
    #/
    if attr_esc == '@':
        res += '{}="{}"\n'.format(
            attr_esc,
            val_esc,
        )
    else:
        res += '"{}"="{}"\n'.format(
            attr_esc,
            val_esc,
        )
    ## |"| in reg file quotes a val (Note it is not part of the val)
    ## |{}| is Python |format| function's placeholder
    ## |\n| is Python escape for newline
    
    #/
    return res

def hkcr_ext_make_attr(ext, attr, val):
    """
    #/
    |ext| will be added a heading dot if not already has one.
    
    #/
    See code 2nDvjL6 for how arguments are escaped.
    """
    #/ 8eiICAX
    dot_ext = ext_add_dot(ext)
    
    #/
    return hkcr_cls_make_attr(cls=dot_ext, attr=attr, val=val)

def hkcr_ext_make_attr_dft(ext, cls):
    """
    #/
    A file extension class' default attribute specifies its associated file type class.
    
    #/
    |ext| will be added a heading dot if not already has one.
    See code 8eiICAX.
    
    #/
    See code 2nDvjL6 for how arguments are escaped.
    """
    return hkcr_ext_make_attr(
        ext=ext,
        attr='@',
        val=cls,
    )

def hkcr_ext_make_attr_contenttype(ext, val):
    """
    #/
    |ext| will be added a heading dot if not already has one.
    See code 8eiICAX.
    
    #/
    See code 2nDvjL6 for how arguments are escaped.
    """
    
    return hkcr_ext_make_attr(
        ext=ext,
        attr='Content Type',
        val=val,
    )

def hkcr_ext_make_attr_perceivedtype(ext, val):
    """
    #/
    |ext| will be added a heading dot if not already has one.
    See code 8eiICAX.
    
    #/
    See code 2nDvjL6 for how arguments are escaped.
    """
    
    return hkcr_ext_make_attr(
        ext=ext,
        attr='PerceivedType',
        val=val,
    )

def hkcr_ext_make_shellnew(ext, shellnew_info):
    """
    |ext| will be added a heading dot if not already has one.
    
    #/
    File type class must have attr |FriendlyTypeName|.
    Otherwise menu item will not show.
    """
    #/
    dot_ext = ext_add_dot(ext)
    
    #/
    shellnew_type = shellnew_info.keys()[0]
    
    #/
    if shellnew_type == 'NullFile':
        attr_val = ''
    elif shellnew_type == 'FileName':
        attr_val = shellnew_info[shellnew_type]
    else:
        assert False

    #/
    res_txt = '[HKEY_CLASSES_ROOT\{}\ShellNew]\n"{}"="{}"\n'.format(
        reg_value_escape(dot_ext),
        reg_value_escape(shellnew_type),
        reg_value_escape(attr_val),
    )
    
    #/
    return res_txt

def hkcr_ext_remove_shellnew(ext):
    """
    #/
    |ext| will be added a heading dot if not already has one.
    """
    #/
    dot_ext = ext_add_dot(ext)

    #/
    res_txt = '[-HKEY_CLASSES_ROOT\{}\ShellNew]\n'.format(dot_ext)
    
    #/
    return res_txt
