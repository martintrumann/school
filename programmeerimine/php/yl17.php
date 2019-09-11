<?php
$a = "kivi";
$com = rand(1,3);
if($a = "kivi"){
	$num_a = 1;
}elseif($a = "käärid"){
	$num_a = 2;
}elseif($a = "paper"){
	$num_a = 3;
}

if($com == $num_a){
	echo "viik";
}elseif($com + 1 == $num_a || $num_a + 2 == $com){
	echo "sinu võit";
}elseif($com - 1 == $num_a || $num_a - 2 == $com){
	echo "minu võit";
}
?>
