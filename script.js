function addCart(item, price){

    alert(item + " Added To Cart 🛒");

}

function payment(){

    document.getElementById("success-box").style.display = "block";

}

function submitReview(){

    let review = document.getElementById("review").value;

    if(review != ""){

        document.getElementById("thank-msg").innerHTML =
        "❤️ Thank you for your review!";

    }

}

function searchFood(){

    let input =
    document.getElementById("search").value.toLowerCase();

    let cards =
    document.getElementsByClassName("food-card");

    for(let i=0; i<cards.length; i++){

        let foodName =
        cards[i].getElementsByTagName("h2")[0];

        let text =
        foodName.innerHTML.toLowerCase();

        if(text.includes(input)){

            cards[i].style.display = "block";

        }

        else{

            cards[i].style.display = "none";

        }

    }

}