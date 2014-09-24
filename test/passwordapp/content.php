<?php require("logic.php");?>

<div class="container">
	<h2>xkcd Password Generator</h2>
	<h2>Your current password</h2>
	<p>Your password is:</p>
	<h2>Generate a new password</h2>
	<form method="POST" action="/.php"><!-- or GET p2:8888?parametervalue-->
		
		<label name="count">Number of words</label>
		<input type="text" id="count" value="count"/><br/>

		<label name="uppercase">Uppercase first letter?</label>
		<input type="checkbox" name="uppercase" value="checkbox"/><br/>

		<label name="symbol">Use a symbol</label>
		<input type="checkbox" name="symbol" value="checkbox"/><br/>

		<label name="number">Include a number</label>
		<input type="checkbox" name="number" value="checkbox"/><br/>

		<input type="submit" name="submit" value="submit"/>
	</form>