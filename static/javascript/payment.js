function form(){
    var name = document.querySelector('#name');
    var card = document.querySelector('#card');
    var expyear = document.querySelector('#expyear');
    var cvv = document.querySelector('#cvv');
    var submit = document.querySelector('#submit');


    
     
    if (name.value==""){
        alert("name must be entered");
        return false;

    }
    if (card.value==""){
        alert("card number  must be entered");
        return false;

    }
    if (expyear.value==""){
        alert("expired year  must be entered");
        return false;

    }
    if (cvv.value==""){
        alert("cvv  must be entered");
        return false;

    }

    return true;
}