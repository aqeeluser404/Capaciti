let users = [    
    // { name: "User 1", email: "user1@example.com", password: "password1" },
    // { name: "User 2", email: "user2@example.com", password: "password2" },
];

function ValidateEmail(email) {
    var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
    
    if (!email.match(mailformat)) {
        alert("Enter Correct Email");
        return false;
    }
    return true;
}

function saveUsers() {
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    // temporary user object to store current user
    let user = {
        name: name,
        email: email,
        password: password
    };
    
    // validate if fields are empty
    if (name === "" || password === "" || email === "") {
        alert("Please fill in the missing information!");
    } 
    // calling validate email method
    else if (!ValidateEmail(email)) {
        document.getElementById("email").value = "";
        return;
    } 
    // saves user if conditions are met
    else {
        users.push(user);
        alert("User information saved!");

        document.getElementById("name").value = "";
        document.getElementById("email").value = "";
        document.getElementById("password").value = "";
    }
}

function login() {
    let email = document.getElementById("email").value;
    let password = document.getElementById("password").value;

    // Find match
    let matchingUser = users.find(user => user.email === email && user.password === password);

    if (matchingUser) {
        alert("Welcome, " + matchingUser.name + "!"); 
    } else {
        alert("Invalid email or password. Please try again."); 
    }
}

function viewUsers() {
    for (let i = 0; i < users.length; i++) {
        let user = users[i];

        let userInfo = "Name: " + user.name + "\n" +
        "Email: " + user.email + "\n" +
        "Password: " + user.password
        alert(userInfo);
    }
}