#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#@created: 18.07.2014
#@author: Aleksey Komissarov
#@contact: ad3002@gmail.com

from PyExp import AbstractModel

class OpticContig(AbstractModel):

    dumpable_attributes = [
        'cid',
        'length',
        'sites',
        'nsites',
    ]

    int_attributes = [
        'cid',
        'length',
        'nsites',
    ]

    list_attributes = ["sites",
                       "marks",
                       "smarks",
                       ]

    list_attributes_types = {"sites":int,
                             "marks":int,
                             "smarks":int,
                             }

class OpticMap(AbstractModel):
    pass