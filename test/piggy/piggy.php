<?php
error_reporting(E_ALL);       # Report Errors, Warnings, and Notices
ini_set('display_errors', 1); # Display errors on page (instead of a log file)
?>

<!DOCTYPE html>
<html>

<head>

    <title>PHPiggy Bank</title>

	<?php require('piggycontr.php');?>

</head>

<body>

    <img alt='PHPiggy Bank Logo' src='http://making-the-internet.s3.amazonaws.com/php-phpiggy-bank.png'>

    <p>
     You have $<?php echo $total; ?> in your piggy bank.
	 <br> You are LUCKY!!!</br>
    </p>
    <img src='<?php echo $image; ?>'>
</body>
</html>