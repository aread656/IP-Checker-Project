import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.Headers;
import com.sun.net.httpserver.HttpExchange;

import java.io.IOException;
import java.io.OutputStream;

public class Server{
    public void HTTPRequest(HttpExchange exchange){
        String JSONResponse;

        Headers headers = exchange.getRequestHeaders();
        headers.add("Content-Type", "application/json");
        headers.add("Access-Control-Allow-Origin", "*");
        String query = exchange.getRequestURI().getQuery();
        String items = get_url_parameters(query, "items");
        if (items.isEmpty()){
            JSONResponse = emptyJSONResponse();
        }else{
            JSONResponse = validJSONResponse(items);
        }
        try{
            exchange.sendResponseHeaders(200, JSONResponse.length());
            OutputStream stream = exchange.getResponseBody();
            stream.write(JSONResponse.getBytes());
            stream.close();
        }catch (IOException e){
            System.out.println(e);
        }
    }
    public String get_url_parameters(String query,String param){
        if (query == null) {
            return null;
        }
        for (String parameter: query.split("&")){
            String[] parameter_parts = parameter.split("=");
            if (parameter_parts.length > 1 && parameter_parts[0].equals(param)){
                return parameter_parts[1];
            }
        }
        return null;
    }
    public String emptyJSONResponse(){
        String string = """
            {
                "error":true,
                "input":[],
                "result",[],
                "output_message":"no inputs"
            }
            """;
        return string;
    }
    public String validJSONResponse(String input){
        String[] items = input.split(",");
        for(String item:items){
            item = item.trim();
        }
        String JSONItems = "[";
        for(int i = 0;i<items.length;i++){
            JSONItems += "\""+items[i]+"\"";
            if (i < items.length-1){
                JSONItems += ",";
            };
        }
        JSONItems += "]";

        String[] answer = Classifier.classifyIPs(items);
        String JSONAnswer = "[";
        for(int i = 0;i<answer.length;i++){
            JSONAnswer += "\""+answer[i]+"\"";
            if (i < answer.length-1){
                JSONAnswer += ",";
            };
        }
        JSONAnswer += "]";
        
        String JSONOutput = "{"+
            "\"error\":false, "+
            "\"input\":" + JSONItems + 
            ", " + "\"answer\": " + 
            JSONAnswer + "}"; 

        return JSONOutput;
    }
}