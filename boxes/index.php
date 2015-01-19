<?php
error_reporting(-1); # Report all PHP errors
ini_set('display_errors', 1);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">
    <title>BOX</title>
    <!-- Custom styles for this template -->
    <link type="text/css" href="css/box.css" rel="stylesheet" >
</head>
<body>
    <?php include("logic.php");?>
    <div class='box'>1</div>
    <div class='box'>2</div>
    <?php echo $boxes; ?>
</body>
    <script src="https://code.jquery.com/jquery.js"></script>
</html>
