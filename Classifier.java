import java.util.Arrays;

public class Classifier{
    public static String[] classifyIPs(String[] addresses){
        if (addresses.length < 1) return new String[]{"Enter addresses"};
        String[] results = new String[addresses.length];
        for(int i = 0; i<results.length;i++){
            String address = addresses[i];
            if (address.contains(".")){
                results[i] = "IPV4";
            }else if(address.contains(":")){
                results[i] = "IPV6";
            }else{
                results[i] = "Unknown";
            }
        }
        return results;
    }
    public static void main(String[] args){
        String[] ips = new String[]{"127.0.0.1","1.1.1.1","12:21::21:1a","aa:bb::cc:dd:ee"};
        System.out.println(Arrays.toString(classifyIPs(ips)));
    }
}
