const form = document.querySelector("#signupForm");
const nameInput = document.querySelector("#name");
const phoneInput = document.querySelector("#phone");
const message = document.querySelector("#message");
const count = document.querySelector("#count");


const ETHIOPIAN_PHONE = /^(09\d{8}|\+2519\d{8})$/;


form.addEventListener("submit", function(event) {

    event.preventDefault();

    const name = nameInput.value.trim();
    const phone = phoneInput.value.trim();

    message.textContent = "";


    if (name.length < 2) {
        message.textContent = "Name must be at least 2 characters.";
        return;
    }


    if (!ETHIOPIAN_PHONE.test(phone)) {
        message.textContent = "Please enter a valid Ethiopian phone number.";
        return;
    }


    const people = JSON.parse(localStorage.getItem("people")) || [];


    const person = {
        name: name,
        phone: phone
    };


    people.push(person);


    localStorage.setItem("people", JSON.stringify(people));


    message.textContent = "Signup successful!";


    form.reset();


    showCount();

});


function showCount() {

    const people = JSON.parse(localStorage.getItem("people")) || [];

    count.textContent = `${people.length} people have signed up.`;

}


showCount();