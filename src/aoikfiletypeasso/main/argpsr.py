# coding: utf-8
from __future__ import absolute_import

from argparse import ArgumentParser

from aoikfiletypeasso.main.argpsr_const import ARG_CONFIG_PATH_F
from aoikfiletypeasso.main.argpsr_const import ARG_CONFIG_PATH_H
from aoikfiletypeasso.main.argpsr_const import ARG_CONFIG_PATH_K
from aoikfiletypeasso.main.argpsr_const import ARG_CONFIG_PATH_V
from aoikfiletypeasso.main.argpsr_const import ARG_IMPORT_ON_A
from aoikfiletypeasso.main.argpsr_const import ARG_IMPORT_ON_F
from aoikfiletypeasso.main.argpsr_const import ARG_IMPORT_ON_H
from aoikfiletypeasso.main.argpsr_const import ARG_IMPORT_ON_K
from aoikfiletypeasso.main.argpsr_const import ARG_OWP_DEL_A
from aoikfiletypeasso.main.argpsr_const import ARG_OWP_DEL_F
from aoikfiletypeasso.main.argpsr_const import ARG_OWP_DEL_H
from aoikfiletypeasso.main.argpsr_const import ARG_OWP_DEL_K
from aoikfiletypeasso.main.argpsr_const import ARG_VER_ON_A
from aoikfiletypeasso.main.argpsr_const import ARG_VER_ON_F
from aoikfiletypeasso.main.argpsr_const import ARG_VER_ON_H
from aoikfiletypeasso.main.argpsr_const import ARG_VER_ON_K


#/
def parser_make():
    #/
    parser = ArgumentParser(add_help=True)

    #/
    parser.add_argument(
        ARG_VER_ON_F,
        dest=ARG_VER_ON_K,
        action=ARG_VER_ON_A,
        help=ARG_VER_ON_H,
    )

    #/
    parser.add_argument(
        ARG_CONFIG_PATH_F,
        dest=ARG_CONFIG_PATH_K,
        metavar=ARG_CONFIG_PATH_V,
        help=ARG_CONFIG_PATH_H,
    )

    #/
    parser.add_argument(
        ARG_IMPORT_ON_F,
        dest=ARG_IMPORT_ON_K,
        action=ARG_IMPORT_ON_A,
        help=ARG_IMPORT_ON_H,
    )

    #/
    parser.add_argument(
        ARG_OWP_DEL_F,
        dest=ARG_OWP_DEL_K,
        action=ARG_OWP_DEL_A,
        help=ARG_OWP_DEL_H,
    )

    #/
    return parser
