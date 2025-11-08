#for IPv4, check if there are 4 groups of values separated by dots; 
#and for IPv6, check if there are up to 8 groups (you can have 2/3/4/5/6/7/8 groups) of values separated by colons; 
#no need to check if the values are decimal/hexadecimal, 
#and no need to check number of digits or characters in each group.

def totalValidIPs(ips):
    num_valid = 0
    for ip in ips:
        if "." in ip:
            #"." means ipv4
            ip_parts = ip.split(".")
            if len(ip_parts) == 4:
                num_valid = num_valid + 1
        elif ":" in ip:
            #":" means ipv6
            ip_parts = ip.split(":")
            if 2 < len(ip_parts) <= 8:
                num_valid = num_valid + 1
        else:
            continue
    return num_valid