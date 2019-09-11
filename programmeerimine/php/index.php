<?php

foreach(scandir("./") as $file){
	if(! preg_match("/\B\..*/i", $file) && $file != "index.php"){
		echo "<h2> $file </h2><p>";
		include($file);
		echo "</p>";
	}
}
?>
