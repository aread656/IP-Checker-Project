public class ClassifierTest{

    public static void main(String[] args){
        boolean pass = true;
        pass &= basicIPV4();
        pass &= basicIPV6();
        pass &= emptyOrNull();
        pass &= nullArray();
        pass &= emptyArray();
        pass &= miscTest();
        if(pass){
            System.exit(0);
        }else{
            System.exit(1);
        }
        }

    private static boolean test(String[] i, String[] e){
        String[] r = Classifier.classifyIPs(i);
        boolean pass = true;
        if (e.length != r.length){
            pass = false;
        }else{
            for(int j = 0;j<e.length;j++){
                if (!e[j].equals(r[j])){
                    pass = false;
                    break;
                }
            }
        }
        return pass;
    }
    public static boolean basicIPV4(){
        String[] input = {"127.0.0.1","100.200.300.400"};
        String[] result = {"IPV4","IPV4"};
        return test(input, result);
    }
    public static boolean basicIPV6(){
        String[] input = {"::a","1a:2a:3a:4a:5a:6a:7a:8a"};
        String[] result = {"IPV6","IPV6"};
        return test(input, result);
    }
    public static boolean emptyOrNull(){
        String[] input = {"","",null};
        String[] result = {"Unknown","Unknown","Unknown"};
        return test(input, result);
    }
    public static boolean nullArray(){
        String[] input = null;
        String[] result = {"No addresses given"};
        return test(input, result);
    }
    public static boolean emptyArray(){
        String[] input = {};
        String[] result = {"No addresses given"};
        return test(input, result);
    }
    public static boolean miscTest(){
        String[] input = {"127.0.0.1","100.200.300.400","1a:2a::8a",
        "a_very_invalid_address][][][][][][][][}{}{}{}{()()()()()}]",""," "};
        String[] result = {"IPV4","IPV4","IPV6","Invalid","Unknown","Unknown"};
        return test(input, result);
    }
}