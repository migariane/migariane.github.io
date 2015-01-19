<?php
error_reporting(E_ALL);       # Report Errors, Warnings, and Notices
ini_set('display_errors', 1); # Display errors on page (instead of a log file)
?>

<!DOCTYPE html>
<html>

<head>
    <title>Parsing Variables</title>
</head>
#Using a static variable...

<?php
function upvote() {

    static $votes = 100;
    $votes++;
    echo $votes.'<br>';

}
upvote(); # Outputs 101
upvote(); # Outputs 102
upvote(); # Outputs 103
?>
<body>
<p>
     You have $<?php echo upvote();?>votes.
</p>
</body>
</html>