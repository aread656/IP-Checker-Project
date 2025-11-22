#include <unordered_map>
#include <string>
#include <stdexcept>
#include "countryinfo.h"
using namespace std;

//split the input into arrays
string countryinfo(const string& ip){
    //map of valid prefixes
    unordered_map<int,string> country_map = {
        {100,"US"},{101,"UK"},{102,"China"}
    };
    //exclude ipv6 addresses
    if (ip.find(':') != string::npos) return "IPV6";
    //unknown for small ips
    if (ip.size() < 3) return "Unknown";
    //return unknown if any non-digits
    for (char c:ip){
        if(!isdigit(c) and c != '.') return "Unknown";
    }
    //check first four items and return prefix
    int prefix;
    try{
        prefix = stoi(ip.substr(0,3));
    } catch (const std::exception& e){
        return "Unknown";
    }
    //match the prefix
    if (country_map.count(prefix)){
        return country_map[prefix];
    }else{
        return "Unknown";
    }
}
