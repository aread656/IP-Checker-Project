var expect = require('chai').expect;
var classifier = require('../ipclassifier');

it('Classifier Test', function(done){
    var t = ["127.0.0.1",
        "100.200.300.400",
        "21:aa:3b:22:77:9a",
        "101.201.301.401"]
    var a = ["IPV4","IPV4","IPV5","IPV4"];
    expect(badipcount.badIPs(t)).to.deep.equal(a);
    done()
})