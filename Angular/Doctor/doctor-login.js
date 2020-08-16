// var myApp = angular.module("myApp", []);
// myApp.controller("loginController", function ($scope, $http, $log) {
//     $http({
//         mrthod: 'GET',
//         url: "https://jsonplaceholder.typicode.com/users",
//     })
//     .then(function(response){
//         $scope.users = response.data;
//         $log.info(response);
//     },function(reason){
//         $scope.error =  reason.data;
//         $log.info(reason);

//     });
// });
var app = angular.module("myApp", []);
app.controller("loginController", function ($scope, $http) {
    $scope.email = null;
    $scope.password = null;

    $scope.postdoctordata = function (email, password) {

        var data = {
            email: email,
            password: password
        }
        var a = validateFields();
        console.log(data);
        if (a == true) {
            $http.post(BASE_URL + "doctor/login/", JSON.stringify(data))
                .then(function (res) {
                    console.log(res);
                    console.log(res.data);
                    if (res.data == "not approved by manager") {
                        swal("Hello world!");
                        document.getElementById('out_data').innerHTML = "You Have Not Registered Yet! Please Register To Continue <br> or Your Registration Has Yet Not Been Approved By Manager"
                    } else if (res.data == "wrong password") {
                        document.getElementById('out_data').innerHTML = "Wrong Password";
                        swal("Hello world!");
                    } else if (res.data == "not registered") {
                        document.getElementById('out_data').innerHTML = "You Have Not Registered Yet! Register To Continue";

                    } else {
                        console.log(res.data.data_r);
                        console.log(res.data.pending_appointment);
                        var docdata = JSON.stringify(res.data.data_r[0]);
                        console.log(docdata);
                        localStorage.setItem("docdata", docdata);
                        swal("Hello world!");
                        window.location.href = "doctor-portal.html";
                    }
                })
        } else {
            console.log("Not Send");
        }

    }
    // $http.get("url")
    // .then(function(response){
    //     $scope.dataOut = response.data;
    // })
})

// ---
// ---
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
        // validateAPI();
        console.log("right");
        return true;
    } else {
        // alert("Fill alll Fields!")
        console.log("wrong");
    }
}

// function validateAPI() {
//     var url = "";
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