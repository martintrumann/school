<?php
$num = rand(1, 100);
$game = 1;
while($game == 1){
	$a = 46;
	if($a > $num){
		echo "väiksem";
	}elseif($a < $num){
		echo "suurem";
	}else{
		echo "öige";
	}
	$game = 0;
}
?>
