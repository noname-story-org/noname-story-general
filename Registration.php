<html>
	<head>
	</head>
	<body>
		<?php
			$servername = "localhost";
			$username = getEnv('USER_NAME');
			$password = getEnv('PASSWORD');
			$dbname = "NonameStoryDB";

			// Create connection
			$conn = new mysqli($servername, $username, $password, $dbname);
			// Check connection
			if ($conn->connect_error) 
			{
				die("Connection failed: " . $conn->connect_error);
			}
			
			// Retrieves information from Registration page
			
			// Checks to see if retrieved information is already in database (Also checks if DB is empty)
			
			$user_name_input = $_POST["username"];
			$user_password_input = $_POST["password"];
			$user_email = $_POST["email"];
			
			// Checks if user input all required values (A username and Password)
			if(!$user_name_input
			|| !$user_password_input)
			{
				echo "You have not entered all the required details.<br>"
				."Please go back and try again.";
				exit;
			}
			
			// Prep a query to check if a user is already in the database
			$query_user_count = "select count(*) from userData where userName = $user_name_input";
			$user_count = intval(mysql_query($query_user_count));
			if($user_count > 0)
			{
				echo "Username alread in use.<br>"
				."Please go back and try again.";
				exit;
			}
			
			// Get current time
			$current_date_time = new date();
			$current_date_time->format("Y-m-d H:i:s");
			
			// Get current max userID
			$query_max_userID = "select max(userID) from userData";
			$user_id = intval(mysql_query($query_max_userID)) + 1;
			
			// Check if an email has been input and create a new insert query
			$user_insert_query = "";
			if($user_email)
			{
				$user_insert_query = "insert into userData(userID, Username, Password, Email, JoinDate, LoginDate) values($user_id, $user_name_input, $user_password_input, $user_email, $current_date_time, $current_date_time)";
			}
			else
			{
				$user_insert_query = "insert into userData(userID, Username, Password, JoinDate, LoginDate) values($user_id, $user_name_input, $user_password_input, $current_date_time, $current_date_time)";
			}
			
			// Execute the user insert query
			mysql_query($user_insert_query);
			
			// Check if insert worked
			if(mysql_affected_rows <= 0)
			{
				echo "Unable to register user.<br>"
				."Please go back and try again.";
			}
		?>
	</body>
</html>