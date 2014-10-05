# AoikWinFileTypeAsso
A console program that creates Windows Registry files (i.e. **.reg** files) to change file type association settings.

Tested working with:
- Windows  
- Python 2.7+, 3.2+

[Package on PyPI](https://pypi.python.org/pypi/AoikWinFileTypeAsso)

## Contents
- [What is AoikWinFileTypeAsso](#what-is-aoikwinfiletypeasso)
- [How to install](#how-to-install)
- [How to use](#how-to-use)
- [Which versions of Windows are supported](#which-versions-of-windows-are-supported)  
- [Why AoikWinFileTypeAsso is useful](#why-aoikwinfiletypeasso-is-useful) 
- [What AoikWinFileTypeAsso does technically](#what-aoikwinfiletypeasso-does-technically) 
- [How to read the funny source code](#how-to-read-the-funny-source-code) 

##What is AoikWinFileTypeAsso
AoikWinFileTypeAsso is a console program that creates Windows Registry files (i.e. ".reg" files) to change file type association settings, including
- **Shell commands:**  
Which command is run when you double click a ".txt" file.  
What commands are available when you right click a ".txt" file.
- **Icon:**  
What icon is used for ".txt" file type.
- **New menu:**  
Which file types are available in the "New" menu when you right click a blank area.

For more details, see
- [Why AoikWinFileTypeAsso is useful](#why-aoikwinfiletypeasso-is-useful) 
- [What AoikWinFileTypeAsso does technically](#what-aoikwinfiletypeasso-does-technically) 

## How to install
AoikWinFileTypeAsso has dependency on **pyyaml** and **pywin32**.
   
- For pyyaml it will be auto installed when installing via pip.
   
- For pywin32 you need to download an installer.  
(Don't worry, the process is straightforward, as detailed below.)
 
### Install pywin32
Download an installer from [here](http://sourceforge.net/projects/pywin32/files/pywin32/).

- Choose the latest build version  (e.g. Build 219 on 2014-05-04).

- Make sure the installer matches with your CPU and Python version,  
e.g. **amd64-py2.7** if you are using an **x64 CPU** and **Python 2.7**.
   
### Install AoikWinFileTypeAsso
Run
```
pip install AoikWinFileTypeAsso
```
or
```
pip install git+https://github.com/AoiKuiyuyou/AoikWinFileTypeAsso
```

## How to use
### Find the command
After installation via pip, a command **aoiwfta** should be available on console.

### Prepare a config file
Command **aoiwfta** takes a config file path as argument.

The syntax of the config file is very simple.
- [config_example.yaml](https://github.com/AoiKuiyuyou/AoikWinFileTypeAsso/blob/master/src/aoikwfta/config_example.yaml) is a minimum example to get started.  
- [config_example2.yaml](https://github.com/AoiKuiyuyou/AoikWinFileTypeAsso/blob/master/src/aoikwfta/config_example2.yaml) is a practical example that has settings for more file types.  
- [config_syntax.txt](https://github.com/AoiKuiyuyou/AoikWinFileTypeAsso/blob/master/src/aoikwfta/config_syntax.txt) is a detailed syntax listing.

These files are located in AoikWinFileTypeAsso's package dir **aoiwfta**.  
You can find the package dir path by running:
```
python -c "import os.path; import aoikwfta; print os.path.dirname(aoikwfta.__file__)"
```

#### Caveats
Modify these config files with your own correct settings before running the command to import data to Windows Registry.

### Run the command
Given a config file, command **aoiwfta** produces registry file data.

By default it writes registry file data to stdout:
```
aoiwfta config_example.yaml
```

You can redirect stdout to create a registry file:
```
aoiwfta config_example.yaml > a.reg
```

Then you can import the registry file to Windows Registry:
```
regedit a.reg
```

After importing a registry file to Windows Registry,  
some changes, e.g. icon change, will not take effect immediately.  
You need to update Windows shell by running:
```
python -m aoikwfta.util.shell_notify_change
```

The creating-importing-updating 3 steps above is indeed too much typing.  
Instead, use the **-i** option to do the 3 steps in one shot.
```
aoiwfta config_example.yaml -i
```
   
## Which versions of Windows are supported
Tested working on Windows 7.

**NOT TESTED** on other versions.

Should work (but again, **NOT TESTED**) on other versions of Windows where the same registry mechanism is used to control file type association settings.
  
## Why AoikWinFileTypeAsso is useful
Windows' file type association settings are internally controlled via Windows Registry.  
These settings are usually changed in the following ways:
- Manually editing Windows Registry
- Windows has provided a tool, i.e. Control Panel's "Default Programs"
- Many application programs, e.g. media players, have provided settings to change these settings, so that related file types can be handled by themselves.
- Many Windows optimization programs have provided tools to change these settings.
   
These ways have the following drawbacks:

1. **Limited in functionality**  
  The tool provided by Windows is limited in functionality.  
  Can only add a default program, not other shell commands.  

  Application programs only provide settings for related file types to use their own programs.  
  Can not change settings for arbitrary file types.

2. **Large amount of work**  
  Windows optimization programs are able to change settings for arbitrary file types.  
  But to change settings for dozens of file types, large amount of work is required.  
  The work is time-consuming and boring.

3. **Lacking in backup mechanism**  
  Had the tool you use not provided backup mechanism, you have to re-do the work again each time file type association settings are changed undesirably, e.g. overridden by another application, or after a Windows re-installation.
   
AoikWinFileTypeAsso has overcome the drawbacks above.

1. **Flexible in functionality**  
  Can change settings for arbitrary file types.

  Have covered conmmonly used settings, e.g. shell commands, icon, and "New" menu.

2. **Minimum amount of work**  
  Use a config file to specify all the settings.

  The config file is in YAML format, with very concise syntax. ([config_example.yaml](https://github.com/AoiKuiyuyou/AoikWinFileTypeAsso/blob/master/src/aoikwfta/config_example.yaml))

  Specifying settings for dozens of file types is a breeze. ([config_example2.yaml](https://github.com/AoiKuiyuyou/AoikWinFileTypeAsso/blob/master/src/aoikwfta/config_example2.yaml))
 
3. **Easy backup mechanism**  
  Your config file is all you need to back up.
    
  Each time file type association settings are changed undesirably,  
  e.g. overridden by another application, or after a Windows re-installation,  
  re-run the command will recover your preferred settings in a second.
   
## What AoikWinFileTypeAsso does technically
Some knowledge about Windows Registry's mechanism for file type association will help you better understand what AoikWinFileTypeAsso does.
 
In Windows Registry's HKEY_CLASSES_ROOT, there are **"file type extension"** keys and
 **"file type class"** keys.
 
"File type extension" keys' name starts with a dot, e.g. |HKEY_CLASSES_ROOT\\.txt\|.  
"File type class" keys' name not starts with a dot, e.g. |HKEY_CLASSES_ROOT\txtfile\|.

Each "file type extension" (e.g. |.txt|) is associated with one "file type class" (e.g. |txtfile|).  
Multiple "file type extensions" (e.g. |.txt| and |.log|) can be associated with a single "file type class" (e.g. |txtfile|).

Some settings, such as "New" menu, are specified per "file type extension".

Some other settings, such as shell commands, are specified per "file type class", not per "file type extension". This is because different "file type extensions" may be handled by the same commands specified by a single "file type class", as in the case for |.txt| and |.log|.

What AoikWinFileTypeAsso does is produce registry file data that associates
 "file type extensions" (e.g. |.txt|) with your own "file type classes" (e.g. |aoikwfta.txt|), and change settings
 of these "file type extensions" and "file type classes". After importing the
 registry file data to Windows Registry, the changes will take effect.

## How to read the funny source code
For developers interested in reading the source code,  
Here is a flowchart ([.png](/doc/dev/main.png?raw=true), [.svg](/doc/dev/main.svg?raw=true), or [.graphml](/doc/dev/main.graphml?raw=true)) that has recorded key steps of the program.  
![Image](/doc/dev/main.png?raw=true)

The flowchart is produced using free graph editor [yEd](http://www.yworks.com/en/products_yed_download.html).

If you want to copy the text in the graph, it's recommended to download the [.svg](/doc/dev/main.svg?raw=true) file and open it locally in your browser. (For security reason, Github has disabled rendering of SVG images on the page.)

The meaning of the shapes in the flowchart should be straightforward.  
One thing worth mentioning is isosceles trapezium means sub-steps.

The most useful feature of the flowchart is, for each step in it,
there is a 7-character ID.  
This ID can be used to locate (by text searching) the code that implements a step.  
This mechanism has two merits:

1. It has provided **precise** (locating precision is line-level)
  and **fast** (text searching is fast) mapping from doc to code, which is
  very handy for non-trivial project.

  Without it you have to rely on developers' memory to recall the code locations (*Will you recall them after several months, precise and fast?*).

2. It has provided **precise** (unique ID) and **concise** (7-character long) names
  for each steps of a program, which is very handy for communicating between
  members of a development team.

  Without it describing some steps of a program between team members tends to be unclear.
