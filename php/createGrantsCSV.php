<?php
	$link = mysqli_connect("localhost", "root", "", "grants");

		    if (mysqli_connect_errno()) {
            printf("Connect failed: %s\n", mysqli_connect_error());
            exit();
        }

        $link->query("SELECT * FROM `Grant`") or die("Error in the consult.." . mysqli_error($link));
?>
