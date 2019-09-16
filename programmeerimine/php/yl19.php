<?php session_start();?>
<form action="yl19.php" method="get">
	<input type="submit" name="action" value="hit" >
	<input type="submit" name="action" value="stand" >
</form>
<?php
$cardpack = array
	(
	array("2");
	array("2" ,0);
	array("2" );
	array("2" );
	array("3" );
	array("3" );
	array("3" );
	array("3" );
	array("4" );
	array("4" );
	array("4" );
	array("4" );
	array("5" );
	array("5" );
	array("5" );
	array("5" );
	array("6" );
	array("6" );
	array("6" );
	array("6" );
	array("7" );
	array("7" );
	array("7" );
	array("7" );
	array("8" );
	array("8" );
	array("8" );
	array("8" );
	array("9" );
	array("9" );
	array("9" );
	array("9" );
	array("10");
	array("10");
	array("10");
	array("10");
	array("J" );
	array("J" );
	array("J" );
	array("J" );
	array("Q" );
	array("Q" );
	array("Q" );
	array("Q" );
	array("K" );
	array("K" );
	array("K" );
	array("K" );
	array("A" );
	array("A" );
	array("A" );
	array("A" );
	);
if ($_GET["action"] == "hit"){
	$card = $cardpack[array_rand($cardpack)];
	unset()
}
?>
