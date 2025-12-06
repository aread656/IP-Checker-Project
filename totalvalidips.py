def totalValidIPs(ips):
    num_valid = 0
    for ip in ips:
        ip.strip()
        if "." in ip:
            if (valid_ipv4(ip)):
                num_valid += 1
        elif ":" in ip:
           if (valid_ipv6(ip)):
               num_valid += 1
        else:
            continue
    return num_valid

def valid_ipv4(ip):
    valid_chars = "1234567890."
    for c in ip:
        if c not in valid_chars:
            return False
    ip_parts = ip.split(".")
    if len(ip_parts) != 4:
        return False
    for part in ip_parts:
        if(not part.isdigit() or not (0<=int(part)<=255)):
            return False
    return True

def valid_ipv6(ip):
    if ip.count("::") >1:
        return False
    valid_chars = "1234567890abcdefABCDEF:"
    for c in ip:
        if c not in valid_chars:
            return False
    
    if "::" in ip:
        LHS, RHS = ip.split("::")
        if LHS:
            LHS_parts = LHS.split(":")
        else:
            LHS_parts = []
        if RHS:
            RHS_parts = RHS.split(":")
        else:
            RHS_parts = []
        empty_parts = 8 - (len(LHS_parts) + len(RHS_parts))
        ip_parts = LHS_parts + (["0000"]*empty_parts) + RHS_parts
    else:
        ip_parts = ip.split(":")

    #should now be eight parts
    if len(ip_parts) != 8:
        return False
    
    for part in ip_parts:
        if len(part) > 4 or len(part) == 0:
            return False
        for char in part.lower():
            if char.lower() not in "0123456789abcdef":
                return False
    return True