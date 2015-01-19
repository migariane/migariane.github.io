<?php
error_reporting(-1); # Report all PHP errors
ini_set('display_errors', 1);
?>
<!DOCTYPE html>
<html>
<head>
 
<meta charset="utf-8">
 
<title>What time is it?</title>
 
<link rel='stylesheet' href='styles.css' type='css'>
<?php require('logic.php'); ?>
</head>
 
<body class='<?php echo $class?>'>
 
<h1>
It is <?php echo $time?>
</h1>
 
<small>Time zone: <?php echo $timezone?>;</small><br>
 
<img src='http://making-the-internet.s3.amazonaws.com/<?=$image?>' alt='Scenery matching the time of day'>
 
</body>
</html>
