<?php
error_reporting(E_ALL);       # Report Errors, Warnings, and Notices
ini_set('display_errors', 1); # Display errors on page (instead of a log file)
?>

<!DOCTYPE html>
<html>

<head>
    <title>Parsing Variables</title>
</head>
	#Using a variable reference....
<?php
function upvote(&$votes) {

    $votes++;
    echo $votes.'<br>';

}

$votes = 100;
upvote($votes); # Outputs 101
upvote($votes); # Outputs 102
upvote($votes); # Outputs 103
?>
<body>
<p>
     You have $<?php echo $votes; ?> votes.
</p>
</body>	
</html>