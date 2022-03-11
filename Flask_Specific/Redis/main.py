# > On Command Prompt > python main.py
# redis-cli

"""
# Create / Update data
set key value
# set if not exist value in key
setnx key value
"""

"""
Get data
 get key

 For example:
 get phone_type
"""

"""
Modify key’s name
renamenx <key_name> <new_key_name>
renamenx phone_type phonetype
"""

"""
Check whether key is existed or not
 exists key
 exists phone_type
"""