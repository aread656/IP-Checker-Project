#include <unordered_map>
#include <string>
#include <stdexcept>
#include "countryinfo.h"
using namespace std;

//split the input into arrays
string countryinfo(const string& ip){
    //map of prefixes
    unordered_map<int,string> country_map = {
        {100,"US"},{101,"UK"},{102,"China"}
    };

    if (ip.empty()) {
        return "Unknown";
    }

    //handle ipv6 addresses
    if (ip.find(':') != string::npos){
        for (char c :ip){
            //if not a colon and not a digit, return invalid if not a valid hex letter
            if (!isdigit(c) && c != ':' && (c<'A'||c>'F')&&(c<'a'||c>'f')){
                return "Invalid";
            }
        }
        return "IPV6";
    }
    //handle ipv4 addresses
    if (ip.find('.') != string::npos){
        for (char c:ip){
            //return invalid if not a digit or '.'
            if(!isdigit(c) and (c != '.')) return "Invalid";
        }
        //check first three items and return prefix
        int prefix;
        try{
            prefix = stoi(ip.substr(0,3));
        } catch (const std::exception& e){
            return "Invalid";
        }
        //match the prefix
        if (country_map.count(prefix)){
            return country_map[prefix];
        }else{
            return "Unknown";
        }
    }
    //all others assumed invalid
    return "Invalid";
    
}
