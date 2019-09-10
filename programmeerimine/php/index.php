<?php

foreach(scandir("./") as $file){
	if(! preg_match("/\B\..*/i", $file) && $file != "index.php"){
		echo "<h2> $file </h2>";
		include($file);
		echo "</p><p>";
	}
}
echo "<br>";
$dir =opendir("./");
echo "<br>";

?>
