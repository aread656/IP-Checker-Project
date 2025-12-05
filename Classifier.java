import java.util.Arrays;
/**
 * Classifies IP addresses as IPV4/6 or Unknown
 */
public class Classifier{
    public static String[] classifyIPs(String[] addresses){
        String validIPChars = "1234567890.:abcdefABCDEF";
        if (addresses == null || addresses.length == 0){
            return new String[]{"No addresses given"};
        }
        String[] results = new String[addresses.length];
        for(int i = 0; i<results.length;i++){
            boolean invalid = false;
            String address = addresses[i];
            if (address != null){
                address = address.trim();
            }
            if(address == null||address.isEmpty()){
                results[i] = "Unknown";
                continue;
            }
            for (int j = 0; j<address.length();j++){
                char c = address.charAt(j);
                // if c does not belong to validIPChars
                //i.e. if validIPChars does not contain c
                if (validIPChars.indexOf(c)==-1){
                    results[i] = "Invalid";
                    invalid = true;
                    break;
                }
            }
            if(!invalid){
                if (address.contains(".")){
                results[i] = "IPV4";
                }else if(address.contains(":")){
                    results[i] = "IPV6";
                }else{
                    results[i] = "Unknown";
                }
            }
            
        }
        return results;
    }
    public static void main(String[] args){
        String[] ips = new String[]{"127.0.0.1","1.1.1.1","12:21::21:1a","aa:bb::cc:dd:ee"};
        System.out.println(Arrays.toString(classifyIPs(ips)));
    }
}
