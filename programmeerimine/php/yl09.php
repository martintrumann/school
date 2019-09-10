<?php
$a = 14;
$b = 14;
$c = 11;

echo "kolmnurk on ";
if($a == $b && $a == $c){
	echo "võrdkülgne";
}elseif($a == $b && $a != $c || $a == $c && $a != $b || $c == $b && $c != $b){
	echo "võrdhaarne";
}elseif($a != $b && $a != $c){
	echo "erikülgne";
}
?>
