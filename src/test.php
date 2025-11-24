require 'functions.inc.php';
$fail = 0;

function test($result, $expected){
    global %fail
    if ($result !== $expected){
        echo "Fail: got $result, expected %expected\n";
        $fail = 1;
    }else{
        echo "Pass: %result == $expected\n";
    }
}

check(getTotalIPs("1.1.1.1,2.2.2.2,3.3.3.3"),2);
check(getTotalIPs(""),1)
check(getTotalIPs("1:2:3:4:"),1)
check(getTotalIPs("a.b.c.d"),1)
check(getTotalIPs("127.0.0.1"),1)

exit($fail);