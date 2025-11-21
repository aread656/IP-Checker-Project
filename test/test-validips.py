import sys
sys.path.insert(0,".")
from totalvalidips import totalValidIPs

def test1() -> bool:
    t = ["127.0.0.1",
        "100.200.300.400",
        "21:aa:3b:22:77:9a",
        "101.201.301.401",
        "....."]
    a = 1
    r = totalValidIPs(t)
    return r == a

def test2() -> bool:
    t = ["::1","1.1.1.1"]
    a = 2
    r = totalValidIPs(t)
    return r == a

def main():
    success = test1() and test2()
    if success:
        sys.exit(0)
    else:
        sys.exit(1)
    
if __name__ == "__main__":
    main()

"""valid_ipv4s = [
    "0.0.0.0",              # lowest IPv4
    "255.255.255.255",      # highest IPv4
    "1.2.3.4",
    "192.168.1.1",
    "127.0.0.1",            # loopback
    "8.8.8.8",
    "0.1.2.3",              # leading zero in a segment
    "1.2.3.004",            # leading zeros (textually weird but numeric)
    "192.168.001.010"
]

invalid_ipv4 = [
    "256.100.100.100",      # out of range
    "192.168.1",            # too few groups
    "192.168.1.1.1",        # too many groups
    "192.168..1",           # empty group
    "...",                  # all empty
    "1.2.3.-4",             # negative number
    "1.2.3.4a",             # invalid character
    "abc.def.ghi.jkl",      # no digits
    "1.2.3.",               # trailing dot
    ".1.2.3"                # leading dot
]

valid_ipv6s = [
    "::",                                   # zero-compressed
    "::1",                                  # loopback
    "1::",                                  # trailing ::
    "::1:2:3:4:5:6:7",                      # leading ::
    "1:2:3:4:5:6:7::",                      # trailing ::
    "0:0:0:0:0:0:0:1",                      # loopback full
    "2001:db8::",                           # documentation prefix
    "0aaa::1",                              # your test case
    "1a:2a:3a:4a:5a:6a::",                  # missing last groups
    "1a:2a:3a:4a:5a:6a:7a:8a",              # full 8 groups
    "abcd:ef01:2345:6789:abcd:ef01:2345:6789",  # full/max-length normal
    "0000:0000:0000:0000:0000:0000:0000:0000",  # explicit zero
    "FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF",  # max
    "::ffff:192.168.1.1"                    # IPv4-mapped IPv6
]

invalid_ipv6 = [
    "1:2:3:4:5:6:7:8:9",            # too many groups
    "1:2:3:4:5:6:7",                # too few groups w/o ::
    "1::2::3",                      # multiple ::
    ":::1",                         # triple colon
    "1:2:3:4:5::6:7:8:9",           # too many after expansion
    "1:2:3:4:5:6:G:1",              # invalid hex digit
    "::00000",                      # >4 hex digits in a group
    "1:2:3:4:",                     # trailing colon w/o ::
    ":1:2:3:4:5:6:7",               # leading colon w/o ::
    "1:2:3:::",                     # malformed
    "",                             # empty string
    ":::::::",                      # nonsense
]

print(totalValidIPs(valid_ipv4s))
print(totalValidIPs(invalid_ipv4))
print(totalValidIPs(valid_ipv6s))
print(totalValidIPs(invalid_ipv6))
"""