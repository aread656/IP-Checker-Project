<?php
require 'functions.inc.php';
$fail = 0;

function test($result, $expected): void{
    global $fail;
    if ($result !== $expected){
        echo "Fail: got $result, expected $expected\n";
        $fail = 1;
    }else{
        echo "Pass: %result == $expected\n";
    }
}

test(getTotalIPs("1.1.1.1,2.2.2.2,3.3.3.3"),3);
test(getTotalIPs(""),1);
test(getTotalIPs("1:2:3:4:"),1);
test(getTotalIPs("a.b.c.d"),1);
test(getTotalIPs("127.0.0.1"),1);

exit($fail);