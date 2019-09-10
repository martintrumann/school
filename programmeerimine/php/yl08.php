<?php
$a = 1804;

echo "$a on ";
if ($a % 400 == 0 || $a % 4 == 0 && $a % 100 != 0){
	echo "liigaasta";
}else{
	echo "lihtaasta";
}
?>
