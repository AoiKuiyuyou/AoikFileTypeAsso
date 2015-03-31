[:var_set('', """
#/ Compile command
aoikdyndocdsl -s README.src.md -n aoikdyndocdsl.ext.all::nto -g README.md
""")
]\
[:var_set('cfg1', 'https://github.com/AoiKuiyuyou/AoikFileTypeAssoDemo/blob/0.1/src/config_example.yaml')]\
[:var_set('cfg2', 'https://github.com/AoiKuiyuyou/AoikFileTypeAssoDemo/blob/0.1/src/config_example2.yaml')]\
[:var_set('aoikfiletypeassodemo', 'https://github.com/AoiKuiyuyou/AoikFileTypeAssoDemo')]\
[:HDLR('heading', 'heading')]\
# AoikFileTypeAsso
Creates Windows Registry files (i.e. **.reg** files) to change file type
 association settings, including
- **Shell commands:**  
Which command is run when you double click a **.txt** file.  
What commands are available when you right click a **.txt** file.
- **Icon:**  
What icon is used for **.txt** file type.
- **New menu:**  
Which file types are available in the **New** menu when you right click a blank
 area.

Tested working with:
- Windows 7, 8
- Python 2.7+, 3.2+

## Table of Contents
[:toc(beg='next', indent=-1)]

## How it works
Under Windows Registry's key **HKEY_CLASSES_ROOT**, there are
 **file type extension** keys and **file type class** keys.
 
A **file type extension** key's name starts with a dot, e.g.
 **HKEY_CLASSES_ROOT\\.txt\**.

A **file type class** key's name not starts with a dot, e.g.
 **HKEY_CLASSES_ROOT\txtfile\**.

Each **file type extension** (e.g. **.txt**) is associated with one
 **file type class** (e.g. **txtfile**).

Multiple **file type extensions** (e.g. **.txt** and **.log**) can be associated
 with the same **file type class** (e.g. **txtfile**).

Some settings, such as **New** menu, are specified per **file type extension**.

Some other settings, such as shell commands, are specified per
 **file type class**, not per **file type extension**. This is because different
 **file type extensions** may be handled by the same commands, as in the case
 for **.txt** and **.log**.

What AoikFileTypeAsso does is generate registry file data that associates
 **file type extensions** (e.g. **.txt**) with your own **file type classes**
 (e.g. **aoikfiletypeasso.txt**), and change settings of these
 **file type extensions** and **file type classes**. After importing the
 generated registry file data to Windows Registry, the changes will take effect.

## Program Setup
[:tod()]

### Setup of PyYAML
Run
```
pip install PyYAML
```

### Setup of PyWin32
Use an installer from [here](http://sourceforge.net/projects/pywin32/files/pywin32/).
- Choose the latest build version  (e.g. Build 219 on 2014-05-04).
- Make sure the installer matches with your Python version, e.g. **amd64-py2.7**
   if you are using a **Python 2.7 x64** version.
   
### Setup of AoikFileTypeAsso
Run
```
pip install git+https://github.com/AoiKuiyuyou/AoikFileTypeAsso
```

### Find entry program
If the installation is via pip, or you have run the **setup.py** in the local
 repo dir, then a command named **aoikfiletypeasso** should be available from
 command line. Run
```
aoikfiletypeasso
```

And because the package has been installed to system package dir, it's
also runnable via module name
```
python -m aoikfiletypeasso.main
```

Anyway, if command **aoikfiletypeasso** is not available, you can still run the
 entry program directly. Go to the local repo dir. Run
```
python src/aoikfiletypeasso/main/aoikfiletypeasso.py
```
- No requirement on working dir, the entry program can be run anywhere as
   long as the path is correct.
- No need to configure **PYTHONPATH** because the entry program supports
  [package bootstrap](https://github.com/AoiKuiyuyou/AoikProjectStart-Python#package-bootstrap).

## Program Usage
Command **aoikfiletypeasso** takes a config file path as argument.

The syntax of the config file is very simple:
- [config_example.yaml]([:var('cfg1')]) is a minimum example.  
- [config_example2.yaml]([:var('cfg2')]) is a practical example.  

See config demos [here]([:var('aoikfiletypeassodemo')]).

See config syntax [here]([:hd_url('config_syntax')]).

Given a config file, command **aoikfiletypeasso** generates registry file data.

Run
```
aoikfiletypeasso -c config_example.yaml -i
```
- `-c` specifies the config file.
- `-i` means import the registry file data to Windows Registry, and send an
 update message to Windows desktop environment to make the changes take effect.
 Note option **-i** requires Administrator privileges.

Without option **-i** the registry file data is written to stdout, e.g.
```
aoikfiletypeasso -c config_example.yaml
```

You can import the registry file to Windows Registry manually
```
aoikfiletypeasso -c config_example.yaml > a.reg

regedit a.reg
```

If you are importing a registry file to Windows Registry manually, some changes
 e.g. icon change, will not take effect immediately. You need to send an update
 message to Windows desktop environment by running
```
python -m aoikfiletypeasso.sac
# or
python src/aoikfiletypeasso/sac.py
```

Use option **-O** to delete subkey **OpenWithProgids**. This prevents Windows
 showing a list of alternative programs.
```
aoikfiletypeasso -c config_example.yaml -i -O
```

## Config Syntax
[:hd_to_key('config_syntax')]\
See config demos [here]([:var('aoikfiletypeassodemo')]).

Syntax:
```
var_d:
## This key is required.
## It contains a list of user-defined variables.
## These variables are intended for substitution for values of key |ext_s|'s subkeys.
## For example, for key |open: TXT_OPEN_CMD|,
## if |TXT_OPEN_CMD| is a variable defined in |var_d|,
## it will be replaced with the corresponding value in |var_d|.
## The purpose of this substitution is to minimize repeating contents.

  #/ User-defined variables
  TXT_OPEN_CMD: '"D:\Software\Dev\IDE\Notepad++\0\dst\notepad++.exe" "%1" %*'
  TXT_ICON_PATH: D:\SoftwareData\FileType\TXT\Icon\0.ico
  TXT_SHELLNEW_PATH: D:\SoftwareData\FileType\TXT\ShellNew\0.txt

  #/ Special variables
  _EXT_CLS_PREFIX: aoikfiletypeasso.
  ## It specifies a common prefix for inferring key |cls|'s value.
  ## For example, with |_EXT_CLS_PREFIX: aoikfiletypeasso.| and |ext: txt|,
  ##  if |cls| is not present, it is inferred |cls: aoikfiletypeasso.txt|.
  ## See code 4eQzSKE and 4q34lgt.
  ##
  ## This key is optional.
  ## If not present, |_EXT_CLS_PREFIX| defaults to |aoikfiletypeasso.| (note the tailing dot).
  
  _SHELLNEW_REMOVE_UNSPECIFIED: 0
  ## It specifies whether remove |ShellNew| key of a file extension class
  ##  if key |new| is not specified in config.
  ## Values should be 0 or 1, default is 0. 
  ## By default, not remove unspecified |ShellNew| key.
  ## As a result, existing |ShellNew| key may have undesirable effects.
  
ext_d:
## This key is required.
## It contains a list of "ext" items, each specifies settings for one "file type extension".
  
  txt:
    ## Key |txt| specifies the "file type extension" to be ".txt".
    ##
    ## This key is required.
    ##
    ## The heading dot is auto added so no need to write |.txt|.
  
    extct: text/plain
    ## Key |extct| specifies the "ContentType" of a "file type extension".
    ##
    ## This key is optional.
    ## If not present, "ContentType" registry key is not produced.

    extpt: text
    ## Key |extpt| specifies the "PerceivedType" of a "file type extension".
    ##
    ## This key is optional.
    ## If not present, "PerceivedType" registry key is not produced.
  
    cls: aoikfiletypeasso.txt
    ## Key |cls| specifies the "file type class" of a "file type extension".
    ##
    ## This key is optional.
    ## If not present, it is inferred.
    ## See code 4q34lgt.
    ## For example, with |_EXT_CLS_PREFIX: aoikfiletypeasso.| and |ext: txt|,
    ##  it is inferred |cls: aoikfiletypeasso.txt|

    clsftn: plain text file
    ## Key |clsftn| specifies the "FriendlyTypeName" of a "file type class".
    ##
    ## This key is optional.
    ## If not present, it defaults to key |cls|'s computed value.
    ## See code 3i3jMU7.

    open: TXT_OPEN_CMD
    ## Key |open| specifies shell command |open| of a "file type class".
    ## It is syntax sugar for key |cmd_s| below.
    ##
    ## This key is optional.

    edit: TXT_OPEN_CMD
    ## Key |edit| specifies shell command |edit| of a "file type class".
    ## It is syntax sugar for key |cmd_s| below.
    ##
    ## This key is optional.

    cmd_s:
      open: TXT_OPEN_CMD
      edit: TXT_OPEN_CMD
    ## Key |cmd_s| specifies shell commands of a "file type class".
    ##
    ## This key is optional.
  
    icon: TXT_ICON_PATH
    ## Key |icon| specifies the icon file of a "file type class".
    ##
    ## This key is optional.
  
    new:
    new: TXT_SHELLNEW_PATH
    ## Key |new| specifies the new file of a "file type extension".
    ##
    ## This key is optional.
    ##
    ## If key |new| is present but has no value,
    ##  an empty file will be used as new file.
    ## Instead, you can specify the path of the new file.
```
