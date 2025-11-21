#include <iostream>
#include "countryinfo.h"
using namespace std;
int main() {
    cout << countryinfo("100.217.23.206") << endl; 
    cout << countryinfo("101.217.23.206") << endl; 
    cout << countryinfo("102.217.23.206") << endl; 
    cout << countryinfo("103.45.67.89") << endl;   
    return 0;
}