# coding: utf-8
"""
File ID: 3wTuD8j
"""

#/ 7pMHmqY: PYTHONPATH bootstrap
## Note this module must be imported before importing other aoikwfta modules.
import aoikwfta_ppbs #@UnusedImport

from aoikwfta.cmd_const import CMD_RET_CODE_V_IMPORTING_TO_REGISTRY_FAILED
from aoikwfta.cmd_const import CMD_RET_CODE_V_IMPORTING_TO_REGISTRY_OK
from aoikwfta.cmd_const import CMD_RET_CODE_V_IMPORTING_WIN32COM_FAILED
from aoikwfta.cmd_const import CMD_RET_CODE_V_OPENING_CONFIG_FILE_FAILED
from aoikwfta.cmd_const import CMD_RET_CODE_V_PARSING_CONFIG_FILE_FAILED
from aoikwfta.cmd_const import CMD_RET_CODE_V_PRODUCING_REGISTRY_DATA_OK
from aoikwfta.config_const import CFG_K_EXT_INFO_D
from aoikwfta.config_const import CFG_K_VAR_D
from argparse import ArgumentParser
import aoikwfta.core as core
import os
import subprocess
import sys
import tempfile
import yaml

#/
if sys.version_info[0] == 2:
    reload(sys)
    sys.setdefaultencoding('utf-8') #@UndefinedVariable

#/
def stdout_write_bytes(bytes):
    if sys.version_info[0] > 2:
        sys.stdout.buffer.write(bytes)
    else:
        sys.stdout.write(bytes)
        
def main():
    #/ 2uYwk0a
    parser = ArgumentParser(prog='PROG')
    
    #/ 3ul8tSI
    parser.add_argument('config', help='A YAML config file path')
    
    #/ 5fsCVk2
    parser.add_argument('-i', '--import',
        dest='import_to_reg',
        action='store_true',
        help='Import to Windows Registry')
    
    #/
    parser.add_argument('-O',
        dest='owp_remove',
        action='store_true',
        help='Remove key "OpenWithProgids".')
    
    #/ 4hnADY0
    args_obj = parser.parse_args()
    #/ 4e0PxM6
    ## Exit here if arguments are incorrect
    
    #/ 5i6GFQ8
    config_file_path = args_obj.config
    
    try:
        #/ 6tY207f
        with open(config_file_path, mode='rb') as config_file_obj:
            #/ 8g0anQk
            try:
                dict_obj = yaml.load(config_file_obj)
            except Exception:
                
                #/ 4u4Bhxf
                sys.stderr.write('#/ Error\n')
                sys.stderr.write('Parsing config file failed.\n')
                
                #/ 2axbv0h
                return CMD_RET_CODE_V_PARSING_CONFIG_FILE_FAILED
            
    except Exception:
        #/ 3s9B4lm
        sys.stderr.write('#/ Error')
        sys.stderr.write('Reading config file failed.')
        
        #/ 9cqrvjt
        return CMD_RET_CODE_V_OPENING_CONFIG_FILE_FAILED
       
    #/
    var_d = dict_obj[CFG_K_VAR_D]
    
    ext_info_s = dict_obj[CFG_K_EXT_INFO_D]
    
    #/ 2iPQrhI
    res_txt = core.config_parse(ext_info_s, var_d,
        owp_remove=args_obj.owp_remove,
    )
    
    res_txt_utf8 = res_txt.encode('utf8') if sys.version_info[0] > 2 else res_txt
    
    #/ 4p6J0rK
    import_to_reg = args_obj.import_to_reg
    
    if not import_to_reg:
        #/ 7xyc66b
        stdout_write_bytes(b'REGEDIT4\n')
        stdout_write_bytes(res_txt_utf8)
        
        #/ 7mHikdk
        return CMD_RET_CODE_V_PRODUCING_REGISTRY_DATA_OK
    
    #/ 2jkggbB
    assert import_to_reg
    
    sys.stderr.write('#/ Import to Windows Registry\n')
         
    reg_file_path = None
    
    ret_code = None
    
    try:
        #/ 3jYbKK0
        file_obj = tempfile.NamedTemporaryFile(delete=False)
        ## 6nOuOHjB
        ## Note on Windows, the temp file is not created until |close| is called.
        ## But by default when |close| is called, the file is deleted.
        ## In order to get access to the temp file, have to use |delete=False|
        ##  and manually delete the file after job done.
        
        reg_file_path = file_obj.name
        
        file_obj.write(b'REGEDIT4\n')
        file_obj.write(res_txt_utf8)
        file_obj.close()
        
        #/ 2thKJr6
        proc_obj = subprocess.Popen(['regedit', '/s', reg_file_path],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )
             
        ret_output = proc_obj.communicate()
        
        ret_code = proc_obj.returncode
    finally:
        if reg_file_path:
            try:
                os.unlink(reg_file_path)
            except:
                pass
    
    #/ 9a7gWwP
    if ret_code == 0:
        #/ 8tBWx3Y
        sys.stderr.write('Ok\n')
    else:
        #/ 3oGPSzN
        sys.stderr.write('Failed\n')
        
        stderr_bytes = ret_output[1]
         
        sys.stderr.write(stderr_bytes)
        sys.stderr.write('\n')
        
        #/ 4tlxev2
        return CMD_RET_CODE_V_IMPORTING_TO_REGISTRY_FAILED
    
    #/ 6hVotpt
    sys.stderr.write('#/ Send shell change notification, to make changes take effect.\n')
    
    #/ 3djlJqJ
    try:
        import win32com.shell.shell as shell #@UnresolvedImport
        import win32com.shell.shellcon as shellcon #@UnresolvedImport
    except ImportError:
        #/ 9jmnJR7
        sys.stderr.write(r"""Failed. Changes may not take effects immediately.
Error:
Importing |win32com| failed.
Please install |pywin32|.
Download is available at http://sourceforge.net/projects/pywin32/files/pywin32/
""")
        
        #/ 3d4HYyD
        return CMD_RET_CODE_V_IMPORTING_WIN32COM_FAILED
         
    #/ 7bldEFK
    shell.SHChangeNotify(
        shellcon.SHCNE_ASSOCCHANGED,
        shellcon.SHCNF_IDLIST,
        None,
        None,
    )
    
    #/ 4gNKPDp
    sys.stderr.write('OK\n')
    
    #/ 3wGMLbJ
    return CMD_RET_CODE_V_IMPORTING_TO_REGISTRY_OK
        
if __name__ == '__main__':
    sys.exit(main())
    