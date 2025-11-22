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
    assert(countryinfo("")=="Unknown");   
    assert(countryinfo("a")=="Unknown");  
    assert(countryinfo(" ")=="Unknown"); 
    assert(countryinfo("ab")=="Unknown");
    assert(countryinfo("23617864982173.aeaeaeeaeaeaeaeeaeaea.362786243283872.21")=="Unknown");
    //non-numeric
    assert(countryinfo("aaa.aaa.aaa.aaa")=="Unknown");
    assert(countryinfo("ab1.ab2.ab3.ab4")=="Unknown");
    assert(countryinfo("--------+[]{#####3,.}")=="Unknown");
    //various positions of non-numeric
    assert(countryinfo("abc.200.300.400")=="Unknown");
    assert(countryinfo("100.abc.300.400")=="Unknown");
    assert(countryinfo("100.200.abc.400")=="Unknown");
    assert(countryinfo("100.200.300.abc")=="Unknown");
    //negative numbers
    assert(countryinfo("-100.200.300.400")=="Unknown");
    assert(countryinfo("100.-200.300.400")=="Unknown");
    assert(countryinfo("100.200.-300.400")=="Unknown");
    assert(countryinfo("100.200.300.-400")=="Unknown");
    //IPV6 tests
    assert(countryinfo("::1") == "IPV6");
    assert(countryinfo("a:.43") == "Unknown" || countryinfo("a:.43") == "IPV6");
    return 0;
}