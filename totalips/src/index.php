<?php
header("Content-type: application/json");
require('functions.inc.php');

$valid_ipv4_chars = "0123456789.";
$valid_ipv6_chars = "0123456789abcdefABCDEF:";

$output = array(
	"error" => false,
  "items" => "",
	"total_ips" => 0
);

$items = $_REQUEST['items'];
$ips = explode(",",$items);
$total_ips=getTotalIPs($items);

$invalid = false;
foreach($ips as $ip){
	$ip = trim($ip);
	if ($ip === ""){
		continue;
	}
	if (strpos($ip,".")!==false){
		if(strspn($ip,$valid_ipv4_chars)
			!==strlen($ip)){
			$invalid = true;
			break;
		}
	}elseif(strpos($ip,":")!==false){
		if(strspn($ip,$valid_ipv6_chars)
			!==strlen($ip)){
			$invalid = true;
			break;
		}
	}else{
		$invalid = true;
		break;
	}
}

$output['items']=$items;
$output['total_ips']=$total_ips;

if ($invalid){
	$output['error'] = true;
	$output['message']="Invalid character(s), please use hex only";
}

echo json_encode($output);
exit();
