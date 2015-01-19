    <?php
    # Define 4 different variables, which will each represent how much a given coin is worth
    $penny_value   = .01;
    $nickle_value  = .05;
    $dime_value    = .10;
    $quarter_value = .25;

    # Define 4 more variables, which will each represent how many of each coin is in the bank
    $pennies  = 1000;
    $nickles  = 2500;
    $dimes    = 340;
    $quarters = 340;

    # Add up how much money is in the piggy bank
    $total = ($pennies * $penny_value) + 
			 ($nickles * $nickle_value) + 
			 ($dimes * $dime_value) + 
			 ($quarters * $quarter_value);
    # Conditionals
    $goal = 10000;

    if($total >= $goal) {
        $image = "http://making-the-internet.s3.amazonaws.com/php-goal-met.png"; 
    }
    else if ($total>=90) {
        $image = "http://making-the-internet.s3.amazonaws.com/php-goal-not-met.png"; 
    }
    ?>