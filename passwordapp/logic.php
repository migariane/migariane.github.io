
<?php

if (isset($_POST['count'])){
	$count = $_POST['count'];
	if(!is_numeric($count)){
	return 'Sorry, there was an error with your amount of words.';
	}
	} else {
	$count = 1;
	}

if (isset($_POST['uppercase'])){
	$uppercase = true;
} else {
	$uppercase = false;
}
if (isset($_POST['symbol'])){
	$symbol = true;
} else{
	$symbol = false;
}
if (isset($_POST['number'])){
	$number = true;
}else{
	$number = false;
}

if($words = file('words.txt')){
	$selected_words = []; //$words[0] == first word
}
for($i = 0; $i < $count; $i++) {
	//generate random number from o to dictionary size	
	$symbols = ['!', '@', '#'];
 	$numbers = [0,1,2,3,4,5,6,7,8,9];
	$max = count($words) -1;
	$rand = rand(0,$max);
    $word2 = $words[$rand];
}
 if($uppercase){
 //loop through words and change the first letter to uppercase
	foreach($selected_words as $index => $word2){
	$selected_words[$index] = ucfirst($word2);
	array_push($word2);}

if($symbol){
for($i = 0; $i < $count; $i++) {
	$max = count($symbols) -1;
	$rand = rand(0,$max);
    $symbol = $symbols[$rand];
    array($symbol);
	}
}

if($number){
for($i = 0; $i < $count; $i++) {
	$max = count($numbers) -1;
	$rand = rand(0,$max);
    $number = $numbers[$rand];
   	array($number);
	}
}
}
