public class ClassifierTest{
    public static void main(String[] args){
        boolean testSuccess = true;
        String[] input = {"127.0.0.1","100.200.300.400","2a:3a:1a:22:4b:4c","101.201.301.401"};
        String[] expected = {"IPV4","IPV4","IPV6","IPV4"};
        String[] result = Classifier.classifyIPs(input);

        for(int i = 0; i<input.length;i++){
            if(!result[i].equals(expected[i])){
                testSuccess = false;
            }
        }
        if(testSuccess == true){
            System.exit(0);
        }else{
            System.exit(1);
        }
    }
}