var checkbox = document.getElementById('flexCheckDefault');
var inputs = document.getElementsByClassName("password_input");

checkbox.addEventListener('change', (event) => 
{
	var l = inputs.length;
	for (i = 0; i < l; i++)
	{
		var input = inputs[i];
	    if (event.target.checked) 
	    {
	      input.type = "text";
	    } 
	    else
	    {
	      input.type="password";
	    }
	}
})