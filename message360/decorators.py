# -*- coding: utf-8 -*-

"""
   message360.decorators

   This file was automatically generated for message360 by APIMATIC v2.0 ( https://apimatic.io ) on 10/21/2016
"""

class lazy_property(object):

    """A decorator class for lazy instantiation."""

    def __init__(self,fget):
        self.fget = fget
        self.func_name = fget.__name__

    def __get__(self,obj,cls):
        if obj is None:
            return None
        value = self.fget(obj)
        setattr(obj,self.func_name,value)
        return value