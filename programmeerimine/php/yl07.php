<?php
$a = "martin";
$b = "saaremaa";
$c = "17";

echo "Tere " . $a;
if($b == "saaremaa"){
	echo "<br>";
	echo "mina elan ka saaremaal";
}
if($c < 18){
	echo "<br>";
	echo "sa oled liiga noor, et autot juhtida";
}elseif($c = 18){
	echo "<br>";
	echo "õnnitlusi täilealiseks saamise puhul";
}elseif($c > 18){
	echo "<br>";
	echo "sa võid autot juhtida";
}else{
	echo "<br>";
	echo "WTF";
}
?>
