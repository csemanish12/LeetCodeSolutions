ip4 = "123.234.234.345"

import string
def valid(ip4):
    if ip4.count(".") == 3:
        parts = ip4.split(".")
        condition = 0
        for part in parts:
            if part.isdigit() and len(part) == 1:
                condition += 1
            elif part.isdigit() and int(part) < 256 and part[0] != '0':
                condition += 1
            else:
                return False
        return condition == 4

    elif ip4.count(":") == 7:
        parts = ip4.split(":")
        condition = 0
        for part in parts:
            if part.isalnum() and len(part) == 1 and part in string.hexdigits:
                condition += 1
            elif part.isalnum() and len(part) <= 4 and all(c in string.hexdigits for c in part):
                condition += 1
            else:
                return False
        return condition == 8
    else:
        return False

