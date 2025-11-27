#include <iostream>
#include "countryinfo.h"
#include <cassert>
using namespace std;
//assert() will continue if a pass, then return 0 will pass the CI test
int main() {
    // successful tests
    assert(countryinfo("100.200.300.400")=="US");
    assert(countryinfo("101.201.301.401")=="UK");
    assert(countryinfo("102.202.302.402")=="China");
    assert(countryinfo("103.203.303.403")=="Unknown");
    //wrong length ip addresses
    assert(countryinfo("")=="Invalid");   
    assert(countryinfo("a")=="Invalid");  
    assert(countryinfo(" ")=="Invalid"); 
    assert(countryinfo("ab")=="Invalid");
    assert(countryinfo("23617864982173.aeaeaeeaeaeaeaeeaeaea.362786243283872.21")=="Invalid");
    //non-numeric
    assert(countryinfo("aaa.aaa.aaa.aaa")=="Invalid");
    assert(countryinfo("ab1.ab2.ab3.ab4")=="Invalid");
    assert(countryinfo("--------+[]{#####3,.}")=="Invalid");
    //various positions of non-numeric
    assert(countryinfo("abc.200.300.400")=="Invalid");
    assert(countryinfo("100.abc.300.400")=="Invalid");
    assert(countryinfo("100.200.abc.400")=="Invalid");
    assert(countryinfo("100.200.300.abc")=="Invalid");
    //negative numbers
    assert(countryinfo("-100.200.300.400")=="Invalid");
    assert(countryinfo("100.-200.300.400")=="Invalid");
    assert(countryinfo("100.200.-300.400")=="Invalid");
    assert(countryinfo("100.200.300.-400")=="Invalid");
    //valid start, invalid rest
    assert(countryinfo("100.abc.blahblah.blahblah")=="Invalid");
    assert(countryinfo("101.abc.blahblah.blahblah")=="Invalid");
    assert(countryinfo("102.abc.blahblah.blahblah")=="Invalid");
    //IPV6 tests
    assert(countryinfo("::1") == "IPV6");
    assert(countryinfo("a:.43") == "Invalid" || countryinfo("a:.43") == "IPV6");
    return 0;
}