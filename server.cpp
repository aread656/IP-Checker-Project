#include "httplib.h"
#include "countryinfo.h"
#include <string>
#include <vector>
using namespace std;

int main(){
    int const PORT = 82;
    string const HOST = "0.0.0.0";
    httplib::Server server;
    server.Get("/", [](const httplib::Request &req, httplib::Response &res) {
        res.set_header("Content-Type","application/json");
        res.set_header("Access-Control-Allow-Origin","*");
        string items = req.get_param_value("items");
        if(items.empty()){
            res.set_content("{\"error\":true,\"input\":[],\"answer\":[],\"message\":\"No inputs were given\"}","application/json");
            return;
        }
        string result = countryinfo(items);
        string JSONOutput = "{\"error\":false,\"answer\":\"" + result + "\"}";
        res.set_content(JSONOutput,"application/json");
    });
    server.listen(HOST, PORT);
}