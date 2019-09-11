<?php
$letters = array("a", "e", "i", "o", "u", "ö", "ä", "õ", "ü");
$a = "juihuyde";
$a_array = str_split($a);
$f_array = array();
foreach($a_array as $let){
	if(in_array($let, $letters)){
		array_push($f_array, $let);
	}
}
foreach($f_array as $let){
	echo $let;
}
?>
