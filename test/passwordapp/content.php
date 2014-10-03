<?php require("logic.php");?>

<div class="container">
	<h2>xkcd Password Generator</h2>
	<h2>Your current password</h2>
	<p>Your password is:<br/>
	<?php
	print_r ($word2);
	print_r ($symbol);
 	print_r ($number);
	?>
	</p>
	<h2>Generate a new password</h2>
	<form method="POST" action="/index.php"><!-- or GET p2:8888?parametervalue-->
		
		<label name="count">Number of words</label>
		<input type="text" id="count" name="count"/><br/>

		<label name="uppercase">Uppercase first letter?</label>
		<input type="checkbox" name="uppercase" value="checkbox"<?php echo ($uppercase) ? 'checked = "checked"' : '' ;?>/><br/>

		<label name="symbol">Use a symbol?</label>
		<input type="checkbox" name="symbol" value="checkbox"<?php echo ($symbol) ? 'checked = "checked"' : '' ;?>/><br/>

		<label name="number">Include a number?</label>
		<input type="checkbox" name="number" value="checkbox"<?php echo ($number) ? 'checked = "checked"' : '' ;?>/><br/>

		<input type="submit" name="submit" value="submit"/>

	</form>