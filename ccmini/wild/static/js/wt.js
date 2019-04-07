
		
		function validate()
		{

			var x = document.getElementById("username").value;
			var y = document.getElementById("pass").value;
			//var a = document.getElementById("PhoneNumber")
			var nm = document.getElementById("username").value;
			var reg = /[a-zA-Z]*/
			
			//alert(a.value);
			
			if(!reg.test(nm))
			{
				alert("Only text characters!");
					return false;
			}
			
			
			if(x === "")
				{
					alert("Please enter username");
					return false;
				}
				
			if(y === "")
				{
					alert("Please enter password");
					return false;
				}

			alert("LOGIN SUCCESSFULL for user "+x);
             


		}
		
		function tpfun()
		{
              alert("Button clicked ");

		}

		 function myfunction1(image){
            var middleimage=document.getElementById("middle").src;
            var imagesrc=image.src;
            
            var temp=imagesrc;
            image.src=middleimage;
            document.getElementById("middle").src=temp;
            
        }