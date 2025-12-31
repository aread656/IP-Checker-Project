var expect = require('chai').expect;
var badipcount = require('../badips');

it('Bad IP Test', function(done){
    var t = ["127.0.0.1",
        "100.200.300.400",
        "21:aa:3b:22:77:9a",
        "101.201.301.401"]
    var a = ["good","bad","good","bad"]
    expect(badipcount.badIPs(t)).to.deep.equal(a);
    done()
})