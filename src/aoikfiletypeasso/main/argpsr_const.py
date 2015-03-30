# coding: utf-8
from __future__ import absolute_import

from aoikargutil import SPEC_DI_K_ONE


#/
ARG_HELP_ON_F = '-h'
ARG_HELP_ON_F2 = '--help'

#/
ARG_VER_ON_F = '--ver'
ARG_VER_ON_K = '9coixKL'
ARG_VER_ON_A = 'store_true'
ARG_VER_ON_H = 'Show version.'

#/
ARG_CONFIG_PATH_F = '-c'
ARG_CONFIG_PATH_K = '2m7yeDR'
ARG_CONFIG_PATH_V = 'CONFIG'
ARG_CONFIG_PATH_H = 'A YAML config file path.'

#/
ARG_IMPORT_ON_F = '-i'
ARG_IMPORT_ON_K = '7iX9sdC'
ARG_IMPORT_ON_A = 'store_true'
ARG_IMPORT_ON_H = 'Import to Windows Registry.'

#/
ARG_OWP_DEL_F = '-O'
ARG_OWP_DEL_K = '6cBdkNX'
ARG_OWP_DEL_A = 'store_true'
ARG_OWP_DEL_H = 'Remove key "OpenWithProgids".'

#/
ARG_SPEC = {
    SPEC_DI_K_ONE: (
        ARG_HELP_ON_F,
        ARG_HELP_ON_F2,
        ARG_VER_ON_F,
        ARG_CONFIG_PATH_F,
    ),
}
