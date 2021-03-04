var form = document.getElementById("form1");

form.addEventListener("keyup", function(event)
{
	if (event.keyCode == 13)
	{
		event.preventDefault();
	}
}
)


form.addEventListener("keyup", function(event) {
  if (event.keyCode === 13)
  {
    	event.preventDefault();
		form.submit();
  }
});