<?php
error_reporting(E_ALL);       # Report Errors, Warnings, and Notices
ini_set('display_errors', 1); # Display errors on page (instead of a log file)
?>

<!DOCTYPE html>
<html>

<head>
    <title>Parsing Variables</title>
</head>
#Using a global variable...

<?php
function upvote() {

    global $votes;
    $votes++;
    echo $votes.'<br>';

}
$votes = 100;
upvote(); # Outputs 101
upvote(); # Outputs 102
upvote(); # Outputs 103
?>
<body>
<p>
     You have $<?php echo $votes; ?> votes.
</p>
</body>

</html>