function form(){
    var fname = document.querySelector('#fname');
    var lname = document.querySelector('#lname');
    var email = document.querySelector('#email');
    var phone = document.querySelector('#phone');
    var amount = document.querySelector('#amount');
    var Address = document.querySelector('#Address');
    var submit = document.querySelector('#submit');


    
    if (fname.value==""){
        alert("name must be filled");
        return false;

    }
    if (lname.value==""){
        alert("name must be filled");
        return false;
    }
        if (email.value==""){
            alert("email must be filled");
            return false;
        }
        if (phone.value==""){
            alert("phone number  must be filled");
            return false;
        }
        if (amount.value==""){
            alert("amount must be filled");
            return false;
    
        }
        if (Address.value==""){
            alert("Address must be filled");
            return false;
        }
        
    
    return true;

}