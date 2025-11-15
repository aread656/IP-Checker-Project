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
        String items = get_query(query, "items");
        if (items.isEmpty()){
            JSONResponse = emptyJSONResponse();
        }else{
            JSONResponse = validJSONResponse();
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
    public String get_query(String query,String selection){
        return "0";
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
    public String validJSONResponse(){
        return "0";
    }
}