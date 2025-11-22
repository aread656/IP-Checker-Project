import sys
sys.path.insert(0,".")
from totalvalidips import totalValidIPs

def test1() -> bool:
    t = ["0.0.0.0","255.255.255.255","1.2.3.4","192.168.1.1",
    "127.0.0.1","8.8.8.8","0.1.2.3","1.2.3.004","192.168.001.010"]
    a = 9
    r = totalValidIPs(t)
    return r == a

def test2() -> bool:
    t = ["256.100.100.100","192.168.1","192.168.1.1.1","192.168..1","...",
    "1.2.3.-4","1.2.3.4a","abc.def.ghi.jkl","1.2.3.",".1.2.3"]
    a = 0
    r = totalValidIPs(t)
    return r == a

def test3() -> bool:
    t = ["::","::1","1::","::1:2:3:4:5:6:7","1:2:3:4:5:6:7::","0:0:0:0:0:0:0:1","2001:db8::","0aaa::1",
    "1a:2a:3a:4a:5a:6a::","1a:2a:3a:4a:5a:6a:7a:8a","abcd:ef01:2345:6789:abcd:ef01:2345:6789",
    "0000:0000:0000:0000:0000:0000:0000:0000","FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF"]
    a = 14
    r = totalValidIPs(t)
    return r == a

def test4() -> bool:
    t = ["1:2:3:4:5:6:7:8:9","1:2:3:4:5:6:7","1::2::3",":::1","1:2:3:4:5::6:7:8:9","1:2:3:4:5:6:G:1",
    "::00000","1:2:3:4:",":1:2:3:4:5:6:7","1:2:3:::","",":::::::"]
    a = 0
    r = totalValidIPs(t)
    return r == a

def main():
    success = test1() and test2() and test3() and test4()
    if success:
        sys.exit(0)
    else:
        sys.exit(1)
    
if __name__ == "__main__":
    main()