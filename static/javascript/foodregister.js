function validate(){
    var name =document.querySelector('#fname');
    var email =document.querySelector('#email');
    var phone =document.querySelector('#phone');
    var food =document.querySelector('#food');
    var submit
 
    if (name.value == "") { 
            window.alert("Please enter your name."); 
            name.focus(); 
            return false; 
        } 
        if (email.value == "") { 
            window.alert("Please enter your email."); 
            email.focus(); 
            return false; 
        } 
        if (phone.value == "") { 
            window.alert("Please enter your phone number."); 
            phone.focus(); 
            return false; 
        } 


  

        if (food.value == "") { 
            window.alert("Please enter food details."); 
            food.focus(); 
            return false; 
        } 
        return true; 
    }