
$(function() {
  $(".button").click(function() {

        number= $("#form_number").val();
        message= $("#form_msg").val();

    //   var xhr = new XMLHttpRequest();
	  
	  // xhr.onload = function(){
		//   const serverres= document.getElementById("res");
		//   serverres.innerHTML = this.responseText;
	  // }
	  
	  // xhr.open("POST", "http://localhost:8080/email.php", true);
	  // xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
	  // xhr.send("number="+number+"&message="+message);
      
      $.ajax({
          type: "POST",
          //beforeSend: function(xhr){xhr.setRequestHeader("Content-type", "application/x-www-form-urlencoded");},
          data: "number="+number+"&message="+message,
          url: "http://localhost:8080/email.php",
		      crossDomain: true,
      });

      return false;
  });
});



