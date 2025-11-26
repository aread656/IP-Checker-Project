import com.sun.net.httpserver.HttpServer;
import com.sun.net.httpserver.Headers;
import com.sun.net.httpserver.HttpExchange;
import java.net.InetSocketAddress;
import java.io.IOException;
import java.io.OutputStream;
/**
 * Server handling for Classifier.java functionality
 */
public class Server{
    private static final int PORT = 83;
    private static final String HOST = "0.0.0.0";
    public static void main(String[] args)throws Exception{
        System.out.println("Test");
        HttpServer httpServer = HttpServer.create(new InetSocketAddress(HOST, PORT),0);
        Server server = new Server();
        httpServer.createContext("/",server::handleHTTPReq);
        httpServer.start();
    }
    public void handleHTTPReq(HttpExchange exchange){
        String JSONResponse;
        Headers headers = exchange.getResponseHeaders();
        headers.add("Content-Type", "application/json");
        headers.add("Access-Control-Allow-Origin", "*");
        String query = exchange.getRequestURI().getQuery();
        String items = get_url_parameters(query, "items");
        items = items.trim();
        if (items == null || items.isEmpty()){
            JSONResponse = emptyJSONResponse();
        }else{
            JSONResponse = nonEmptyJSONResponse(items);
        }
        try{
            exchange.sendResponseHeaders(200, JSONResponse.length());
            OutputStream os = exchange.getResponseBody();
            os.write(JSONResponse.getBytes());
        }catch (IOException e){
            System.out.println(e);
        }
    }
    /**
     * Extract items parameter from the URL
     */
    public String get_url_parameters(String query,String param){
        if (query == null) {
            return null;
        }
        for (String parameter: query.split("&")){
            String[] parts = parameter.split("=");
            if (parts.length > 1 && parts[0].equals(param)){
                return parts[1];
            }
        }
        return null;
    }
    /**
     * JSON response if no items
    */
    public String emptyJSONResponse(){
        return """
        {"error":true,"input":[],"result":[],"output_message":"no inputs"}
        """;
    }
    /**
     * Build JSON for when items are present
     */
    public String nonEmptyJSONResponse(String rawInput){
        try{
            String[] items = rawInput.split(",");
            for(int i=0; i<items.length;i++){
                items[i] = items[i].trim();
            }

            StringBuilder JSONItems = new StringBuilder("[");
            for(int i = 0;i<items.length;i++){
                JSONItems.append("\"").append(items[i]).append("\"");
                if (i < items.length-1){
                    JSONItems.append(",");
                };
            }
            JSONItems.append("]");

            String[] classifications = Classifier.classifyIPs(items);
            for (String classification : classifications) {
                if (classification.equals("Invalid")||classification.equals("Unknown")){
                    return buildInvalidJSONResponse(classifications, JSONItems);
                }
            }
            return buildValidJSONReponse(classifications, JSONItems);
        }catch (Exception e){
            return "{"+"\"error\":true, "+
            "\"input\":[], " + "\"answer\":\"invalid characters\""+"}"; 
        }
    }
    /**
     * Building JSON response if any of the IPs are invalid
     */
    public String buildInvalidJSONResponse(String[] classifications,StringBuilder JSONItems){
        StringBuilder JSONAnswer = new StringBuilder("[");
        for(int i = 0;i < classifications.length; i++){
            JSONAnswer.append("\"").append(classifications[i]).append("\"");
            if (i < classifications.length-1){JSONAnswer.append(",");}
        }
        JSONAnswer.append("]");
        
        String JSONOutput = "{"+"\"error\":true, "+
            "\"input\":" + JSONItems + 
            ", " + "\"answer\":\"invalid characters\""+"}"; 
        return JSONOutput;
    }
    /**
     * Building JSON response if all the IPs are valid
     */
    public String buildValidJSONReponse(String[] classifications,StringBuilder JSONItems){
         StringBuilder JSONAnswer = new StringBuilder("[");
        for(int i = 0;i < classifications.length; i++){
            JSONAnswer.append("\"").append(classifications[i]).append("\"");
            if (i < classifications.length-1){JSONAnswer.append(",");}
        }
        JSONAnswer.append("]");
        
        String JSONOutput = "{"+"\"error\":false, "+
            "\"input\":" + JSONItems + 
            ", " + "\"answer\": " + JSONAnswer + "}"; 
        return JSONOutput;
    }
}