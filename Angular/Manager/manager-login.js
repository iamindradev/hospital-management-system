var app = angular.module("myApp", []);
app.controller("loginController", function ($scope, $http) {
    $scope.username = null;
    $scope.password = null;

    $scope.postmanagerdata = function (username, password) {

        var data = {
            username: username,
            password: password
        }
        var a = validateFields();
        console.log(data);
        if (a == true) {
            $http.post(BASE_URL + "manager/login/", JSON.stringify(data))
                .then(function (res) {
                    console.log(res);
                    // console.log(res.data);
                    console.log(res.data);
                    window.location.href = "manager-portal.html";
                })
        } else {
            console.log("not send");
        }

    }
    // $http.get("url")
    // .then(function(response){
    //     $scope.dataOut = response.data;
    // })
})



// -----
function validateUsername() {
    var username = document.getElementById("username").value;
    var usernameValue = username.trim();
    if (usernameValue == "") {
        // document.getElementById("usererror").innerHTML = "Enter your username";
        $("#username").css({
            "border": "none",
            "border-bottom": "2px solid red"
        });
    } else if (usernameValue != "") {
        // document.getElementById("usererror").innerHTML = "";
        $("#username").css({
            "border": "none",
            "border-bottom": "2px solid green"
        });
        return true;
    }
}

function validatePassword() {
    var password = document.getElementById("password").value;
    var passwordValue = password.trim();
    if (passwordValue == "") {
        // document.getElementById("passerror").innerHTML = "Enter your password";
        $("#password").css({
            "border": "none",
            "border-bottom": "2px solid red"
        });
    } else if (passwordValue != "") {
        // document.getElementById("passerror").innerHTML = "";
        $("#password").css({
            "border": "none",
            "border-bottom": "2px solid green"
        });
        return true;
    }
}

function validateFields() {
    var p = validatePassword();
    var u = validateUsername();
    if ((p == true) && (u == true)) {
        console.log("right");
        return true;
    } else {
        console.log("wrong");
    }
}

// function validateAPI() {
//     fetch("http://jsonplaceholder.typicode.com/users/2")
//         .then(function (response) {
//             if (response.status == 200) {
//                 return response.json();
//             } else {
//                 throw new Error('Invalid user ID');
//             }
//         })
//         .then((data) => {
//             console.log(data);
//             var usernameData = document.getElementById("username").value;
//             var passwordData = document.getElementById("password").value;

//             if ((data.username == usernameData) && (data.id == passwordData)) {
//                 window.location = "PortalPRS.html";
//             } else {
//                 alert("Invalid Credentials");
//             }
//         })
//         .catch((err) => {
//             console.log('ERROR: ', err.message);
//         });
// }