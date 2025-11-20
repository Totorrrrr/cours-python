def formatter_memoire(octets):
   
    if octets < 1024:
        return f"{octets} octets"
    elif octets < 1024**2:
        ko = octets / 1024
        return f"{ko:.2f} Ko"
    else:
        mo = octets / (1024**2)
        return f"{mo:.2f} Mo"