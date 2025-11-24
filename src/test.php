<?php
require 'functions.inc.php';
$fail = 0;

function test($result, $expected): void{
    global $fail;
    if ($result !== $expected){
        echo "Fail: got $result, expected %expected\n";
        $fail = 1;
    }else{
        echo "Pass: %result == $expected\n";
    }
}

test(result: getTotalIPs(items: "1.1.1.1,2.2.2.2,3.3.3.3"),expected: 2);
test(result: getTotalIPs(items: ""),expected: 1);
test(result: getTotalIPs(items: "1:2:3:4:"),expected: 1);
test(result: getTotalIPs(items: "a.b.c.d"),expected: 1);
test(result: getTotalIPs(items: "127.0.0.1"),expected: 1);

exit($fail);