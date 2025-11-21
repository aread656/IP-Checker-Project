#include <unordered_map>
#include <string>
#include "countryinfo.h"
using namespace std;

//split the input into arrays
string countryinfo(const string& ip){
    unordered_map<int,string> country_map = {
        {100,"US"},{101,"UK"},{102,"China"}
    };
    //to do: exclude ipv6 addresses
    if (ip.size() < 3) return "Unknown";
    int prefix = stoi(ip.substr(0,3));
    if (country_map.count(prefix)){
        return country_map[prefix];
    }else{
        return "Unknown";
    }
}
