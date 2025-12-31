#include "httplib.h"
#include "countryinfo.h"
#include <string>
#include <vector>
using namespace std;
/**
 * HTTP request gets items split by commas. parse_items splits
 * into individual items for later processing in the form of a 
 * string vector
 */
string remove_whitespace(const string &s){
    string stripped_s;
    for (char c:s){
        if (c!=' '){
            stripped_s += c;
        }
    }
    return stripped_s;
}

vector<string> parse_items(const string &items){
    vector<string> output;
    string currentString;
    for (char c:items){
        if(c == ','){
            output.push_back(remove_whitespace(currentString));
            currentString = "";
        }else{
            currentString+= c;
        }
    }
    output.push_back(remove_whitespace(currentString));
    return output;
}

/**
 * Establishes httpconnection using httplib c++ header file,
 * retrieved from the relevant raw github repository
 * https://raw.githubusercontent.com/yhirose/cpp-httplib/refs/heads/master/httplib.h
 */
int main(){
    int const PORT = 84;
    string const HOST = "0.0.0.0";
    httplib::Server server;
    server.Get("/", [](const httplib::Request &req, httplib::Response &res) {
        res.set_header("Content-Type","application/json");
        res.set_header("Access-Control-Allow-Origin","*");
        //getting items from http request
        if(!req.has_param("items")){
            res.set_content("{\"error\":true,\"input\":[],\"answer\":[],\"message\":\"No inputs were given\"}","application/json");
            return;
        }
        string items = req.get_param_value("items");
        //splitting items into string vector using parse_items
        vector<string> split_items = parse_items(items);
        vector<string> result;
        bool invalid = false;
        //returning countryinfo for each
        for (const auto& ip: split_items){
            try{
                if (ip.empty()){
                    result.push_back("Empty");
                }else{
                    string c_info = countryinfo(ip);
                    if (c_info == "Invalid"){
                        result.push_back("Invalid IPV4 or IPV6 format");
                        invalid = true;
                    }else{
                        result.push_back(c_info);
                    }
                }
            }catch (...){
                result.push_back("Invalid IPV4 or IPV6 format");
            }
        }
        //building up outputted JSON
        string JSONOutput = "{\"error\":" + string(invalid ? "true" : "false") + ",\"answer\":[";
        for (int i = 0; i < result.size(); i++){
            if (i != 0){
                JSONOutput += ",";
            }
            JSONOutput += "\"" + result[i] + "\"";
        }
        JSONOutput += "]}";
        res.set_content(JSONOutput,"application/json");
    });
    server.listen(HOST, PORT);
}