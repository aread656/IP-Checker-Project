#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

string countryinfo(const string& ip){
    unordered_map<int,string> country_map = {
        {100,"US"},{101,"UK"},{102,"China"}
    };
    if (ip.size() < 3) return "Unknown";
    int prefix = stoi(ip.substr(0,3));
    if (country_map.count(prefix)){
        return country_map[prefix];
    }else{
        return "Unknown";
    }
}

int main() {
    cout << countryinfo("100.217.23.206") << endl; 
    cout << countryinfo("101.217.23.206") << endl; 
    cout << countryinfo("102.217.23.206") << endl; 
    cout << countryinfo("103.45.67.89") << endl;   
    return 0;
}