function validate()
{
	var name = document.getElementById("login_input").value;
	var password = document.getElementById("password_input").value;
	var value = false;
	if (name.length >= 5 && name.length <= 32)
	{
		if (password.length >= 5 && password.length <= 32)
		{
			;
		}
		else
		{
			value = "Password must be between 5 and 32 characters long";
		}
	}
	else
	{
		value = "Login must be between 5 and 32 characters long";
	}
	
	if (value != false)
	{
		window.alert(value);
	}
	else
	{
		var form = document.getElementById("form1");
		form.submit();
	}
}

document.getElementById("submit_bt").onclick = validate;