#include <iostream>
#include "countryinfo.h"
#include <cassert>
using namespace std;
//assert() will continue if a pass, then return 0 will pass the CI test
int main() {
    assert(countryinfo("100.200.300.400")=="US");
    assert(countryinfo("101.201.301.401")=="UK");
    assert(countryinfo("102.202.302.402")=="China");
    assert(countryinfo("103.203.303.403")=="Unknown");
    assert(countryinfo("a")=="Unknown");   
    return 0;
}