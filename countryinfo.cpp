#include <unordered_map>
#include <string>
#include <stdexcept>
#include "countryinfo.h"
using namespace std;

//split the input into arrays
string countryinfo(const string& ip){
    unordered_map<int,string> country_map = {
        {100,"US"},{101,"UK"},{102,"China"}
    };
    //to do: exclude ipv6 addresses
    if (ip.size() < 3) return "Unknown";
    if (ip.find(':') != string::npos) return "IPV6";
    int prefix;
    try{
        prefix = stoi(ip.substr(0,3));
    } catch (const std::exception& e){
        return "Unknown";
    }
    if (country_map.count(prefix)){
        return country_map[prefix];
    }else{
        return "Unknown";
    }
}
