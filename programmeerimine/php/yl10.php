<?php
$a = ["apelsiin", "mandariin", "õun"];
print_r($a);

array_push($a, "banaan");
echo "<br>";
echo $a[count($a) -1];
echo "<br>";
foreach($a as $val){
	if($val == "banaan"){
		echo "nimekirjas on banaan";
	}
}

echo "<br>";
echo "nimekirja pikkus on " . count($a);
echo "<br>";
array_pop($a);
print_r($a);
echo "<br>";
print_r(array_reverse($a));
echo "<br>";
sort($a);
print_r($a);
?>
