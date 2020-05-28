'''
pure python utils
'''


def options_val(dictionary, key, default):
    if key in dictionary:
        return dictionary[key]
    else:
        return default