# Module is nothing but a python file which holds the group of python objects.
# Modules are used to provide a special feature called modularity.
# [The process of accessing the data from one file to another known as modularity]
'''Python supports three types of modules are:
   1) user deffined modules
   2) built in modules
   3) third party modules'''
# note: A module is lso known as library (or) package

# 1) user defined modules:
# ------------------------

'''The modules created by the developer/ user are known as user defined modules.
   To access the data from an user defined module python provides two types of mechanisms.They are
   1) import
   2) from import

   1)import:
   This keyword is used to import all the properties from the module irrespective of usage.
   Follow the below syntax to import and access the data from it(module).
   syntax:
         import module_name
         module_name.property_name

    2) from import:
    This keyword is used to import the specific properties from the module.
    when it compared with import statement from import will consume less memory.
    syntax:
           from module-name import p1........'''

# 2) built in modules:
# ---------------------

''' The modules comes with default programming language is known as in-built-modules.
    Just like user defined modules we can access the data from built-in-modules by using import and from-import keyword.
    eg:
    os
    sys
    datetime
    itertools
    etc....'''

# 3) third party modules:
# -----------------------

''' The moules neither created by user nor comes with the programming language are known as third party modules.
    All the third party modules are available at internet(network) especially at "www.pypi.org"(pypi--->python package index)
    eg:
    request
    django
    flask
    web2py
    pandas
    numpy
    etc....'''


    
