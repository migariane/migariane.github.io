<?php
 
# Set the timezone
# http://us3.php.net/manual/en/timezones.php
date_default_timezone_set('America/New_York');
 
# Ref: http://us1.php.net/manual/en/function.date.php
 
# Get the time... This will be used to display the time on the page
# g = 12-hour format of an hour without leading zeros
# : = Just a colon
# i = Minutes with leading zeros
# a = Lowercase am or pm
$time = date('g:ia');
 
$timezone = date('e');
 
# Figure out what the hour is using the 'G' format: 24-hour format of an hour without leading zeros
$hour = date('G');
 
# These are just tests we can uncomment when testing the code
# $hour = 6; # Test morning
# $hour = 12; # Test afternoon
# $hour = 6; # Test evening
# $hour = 23; # Test night
 
# Logic!
if($hour >= 5 AND $hour < 11) {
$image = 'php-morning.png';
$class = 'morning';
}
elseif($hour >= 11 AND $hour < 16) {
$image = 'php-afternoon.png';
$class = 'afternoon';
}
elseif($hour >= 16 AND $hour < 20) {
$image = 'php-evening.png';
$class = 'evening';
}
else {
$image = 'php-night.png';
$class = 'night';
}