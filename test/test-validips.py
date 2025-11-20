import sys
from totalvalidips import totalValidIPs

"""it('Bad IP Test', function(done){
    var t = ["127.0.0.1",
        "100.200.300.400",
        "21:aa:3b:22:77:9a",
        "101.201.301.401"]
    var a = ["good","bad","good","bad"]
    expect(badipcount.badIPs(t)).to.deep.equal(a);
    done()
})"""

def main():
    test_success = True;
    t = ["127.0.0.1",
        "100.200.300.400",
        "21:aa:3b:22:77:9a",
        "101.201.301.401",
        "....."]
    a = 4
    r = totalValidIPs(t)
    if (r!=a):
        test_success = False
    
    if (test_success):
        sys.exit(0)
    else:
        sys.exit(1)
    
if __name__ == "__main__":
    main()