# coding: utf-8
"""
File ID: 3dYVyMI
"""

from aoikwfta.config_const import CFG_K_EXT_INFO_K_CLS
from aoikwfta.config_const import CFG_K_EXT_INFO_K_CLS_FRIENDLY_TYPE_NAME
from aoikwfta.config_const import CFG_K_EXT_INFO_K_CMD_DFT
from aoikwfta.config_const import CFG_K_EXT_INFO_K_CMD_EDIT
from aoikwfta.config_const import CFG_K_EXT_INFO_K_CMD_INFO_S
from aoikwfta.config_const import CFG_K_EXT_INFO_K_CMD_OPEN
from aoikwfta.config_const import CFG_K_EXT_INFO_K_EXT_CONTENT_TYPE
from aoikwfta.config_const import CFG_K_EXT_INFO_K_EXT_PERCEIVED_TYPE
from aoikwfta.config_const import CFG_K_EXT_INFO_K_ICON
from aoikwfta.config_const import CFG_K_EXT_INFO_K_SHELLNEW_INFO
from aoikwfta.config_const import CFG_K_VAR_D_K__EXT_CLS_PREFIX
from aoikwfta.config_const import CFG_K_VAR_D_K__EXT_CLS_PREFIX_V_DFT
from aoikwfta.config_const import CFG_K_VAR_D_K__SHELLNEW_REMOVE_UNSPECIFIED
from aoikwfta.util import reg_util
from aoikwfta.util.reg_util import hkcr_ext_remove_shellnew

#/ 8n0H7m6
def config_parse(ext_d, var_d):
    """
    Parse config dict, produce registry file data.
    """
    #/
    res_txt_s = []
    
    #/ 4eQzSKE
    ext_cls_prefix = var_d.get(CFG_K_VAR_D_K__EXT_CLS_PREFIX, CFG_K_VAR_D_K__EXT_CLS_PREFIX_V_DFT)
    
    #/ 5bmLgAe
    shellnew_remove_unspecified = bool(var_d.get(CFG_K_VAR_D_K__SHELLNEW_REMOVE_UNSPECIFIED, False))
        
    #/ 3itUQnC
    for ext, ext_info in ext_d.items():
        #/
        if ext.startswith('.'):
            ext = ext.lstrip('.')
            
        assert not ext.startswith('.')
        assert len(ext) > 0
        
        #/
        dot_ext = '.' + ext
        
        #/ 4q34lgt
        ext_cls = ext_info.get(CFG_K_EXT_INFO_K_CLS, None)
        ## can be None
        
        #/ 5x2P2EJ
        if ext_cls is None:
            #/ 8p9ijUO
            ext_cls = '{}{}'.format(ext_cls_prefix, ext)
#        else:
#            #/ 3clfMF3
#            pass
        
        assert len(ext_cls) > 0
        
        #/ 2rpS10w
        res_txt_s.append(
            reg_util.hkcr_ext_make_attr_dft(
                ext=dot_ext,
                cls=ext_cls,
            )
        )
        
        #/ 3i3jMU7
        ext_cls_ftn = ext_info.get(CFG_K_EXT_INFO_K_CLS_FRIENDLY_TYPE_NAME, None)
        
        if ext_cls_ftn is None:
            ext_cls_ftn = ext_cls
            
        assert ext_cls_ftn is not None
        
        res_txt_s.append(
            reg_util.hkcr_cls_make_attr(
                cls=ext_cls,
                attr='FriendlyTypeName',
                val=ext_cls_ftn,
            )
        )
        
        #/ 3qfD6yO
        content_type = ext_info.get(CFG_K_EXT_INFO_K_EXT_CONTENT_TYPE, None)
        ## can be None
        
        if content_type is not None:
            res_txt_s.append(
                reg_util.hkcr_ext_make_attr_contenttype(
                    ext=dot_ext,
                    val=content_type,
                )
            )
        
        #/ 9xhpAd3
        perceived_type = ext_info.get(CFG_K_EXT_INFO_K_EXT_PERCEIVED_TYPE, None)
        ## can be None
        
        if perceived_type is not None:
            res_txt_s.append(
                reg_util.hkcr_ext_make_attr_perceivedtype(
                    ext=dot_ext,
                    val=perceived_type,
                )
            )
            
        #/ 7mhLiCE
        cmd_info_s = ext_info.get(CFG_K_EXT_INFO_K_CMD_INFO_S, [])
        
        #/
        cmd_open = ext_info.get(CFG_K_EXT_INFO_K_CMD_OPEN, None)
        
        if cmd_open is not None:
            cmd_info = {'open': cmd_open}
            cmd_info_s.append(cmd_info)
        
        #/
        cmd_edit = ext_info.get(CFG_K_EXT_INFO_K_CMD_EDIT, None)
        
        if cmd_edit is not None:
            cmd_info = {'edit': cmd_edit}
            cmd_info_s.append(cmd_info)
            
        #/
        if cmd_info_s:
            for cmd_info in cmd_info_s:
                cmd_key = next(iter(cmd_info))
                cmd_val = cmd_info[cmd_key]
                
                if cmd_val in var_d:
                    cmd_val = var_d[cmd_val]
                    
                res_txt_s.append(
                    reg_util.hkcr_cls_make_shell_command(
                        cls=ext_cls,
                        cmd_key=cmd_key,
                        cmd_val=cmd_val
                    )
                )
            
        #/ 3mWgiNc
        dft_cmd_key = ext_info.get(CFG_K_EXT_INFO_K_CMD_DFT, None)
        
        #/ 6vhKi1F
        if dft_cmd_key is None:
            #/ 7kA2XGi
            if cmd_info_s:
                #/ 5irpX2B
                dft_cmd_key = next(iter(cmd_info_s[0]))
                
                assert dft_cmd_key is not None
            #else 2oD6axR
            
        #else 3agZzIa
        
        #/ 3agZzIa
        #/ 5irpX2B
        if dft_cmd_key is not None:
            res_txt_s.append(
                reg_util.hkcr_cls_make_shell_command_default(
                    cls=ext_cls,
                    cmd_key=dft_cmd_key,
                )
            )
        #else 2oD6axR
        
        #/ 5i4xfuc
        icon_file_path = ext_info.get(CFG_K_EXT_INFO_K_ICON, None)
        
        if icon_file_path is not None:
            #/
            if icon_file_path in var_d:
                icon_file_path = var_d[icon_file_path]
            
            #/
            res_txt_s.append(
                reg_util.hkcr_cls_make_defaulticon(
                    cls=ext_cls,
                    icon=icon_file_path,
                )
            )
        
        #/ 7jEcqDL
        
        #/ 9tWMLSO
        if CFG_K_EXT_INFO_K_SHELLNEW_INFO in ext_info:
            #/ 3e855O9
            shellnew_info = ext_info[CFG_K_EXT_INFO_K_SHELLNEW_INFO]
            
            if shellnew_info is None:
                res_txt_s.append(
                    reg_util.hkcr_ext_make_shellnew(
                       ext=dot_ext,
                       shellnew_info={'NullFile': None},
                    )
                )
            else:
                shellnew_file_path = shellnew_info
                
                if shellnew_file_path in var_d:
                    shellnew_file_path = var_d[shellnew_file_path]
                
                res_txt_s.append(
                    reg_util.hkcr_ext_make_shellnew(
                       ext=dot_ext,
                       shellnew_info={'FileName': shellnew_file_path},
                    )
                )
        else:
            #/ 6q5OEkP
            if shellnew_remove_unspecified:
                res_txt_s.append(
                    hkcr_ext_remove_shellnew(dot_ext)
                )
        
    #/
    res_txt = ''.join(res_txt_s)
    
    return res_txt
    