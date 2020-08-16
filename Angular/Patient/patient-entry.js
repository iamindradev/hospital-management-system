var myApp = angular.module("myApp", ['ui.router']);
myApp.controller("registrationController", function ($scope, $http) {

    $scope.firstname = null;
    $scope.lastname = null;
    $scope.mobilenumber = null;
    $scope.email = null;
    $scope.gender = "Gender";
    $scope.password = null;
    $scope.age = "Your Age";
    $scope.bloodgroup = "Blood Group";
    $scope.height = "Your Height";
    $scope.weight = "Your Weight";

    $scope.postdata = function (firstname, lastname, mobilenumber, email, gender, password, age, bloodgroup, height, weight) {

        var data = {
            first_name: firstname,
            last_name: lastname,
            mobile_number: mobilenumber,
            email: email,
            gender: gender,
            password: password,
            age: age,
            blood_group: bloodgroup,
            height: height,
            weight: weight
        }
        var a = onSubmit();
        console.log(data);
        if (a == true) {
            $http.post(BASE_URL + "patient/register/", JSON.stringify(data))
                .then(function (res) {
                    console.log(res);
                    console.log(res.data);
                    if (res.data == "sucess") {
                        document.getElementById('out_data').innerHTML = "You Have Successfully Registered! Login To Continue";
                        swal("Registered Successfully!", "Login To Continue!", "success")
                            .then((value) => {
                                window.location.href = "patient-entry2.html"
                            })
                    } else {
                        swal("Not Registered!", "Some Error Occured", "error");
                        document.getElementById('out_data').innerHTML = "Not able to register some error occurred";
                    }
                })
        } else {
            console.log("not send");
        }

    }
});
myApp.controller("logController", function ($scope, $http) {
    $scope.email = null;
    $scope.password = null;

    $scope.postpatientdata = function (email, password) {
        console.log("hii");
        var data = {
            email: email,
            password: password
        }
        var a = validateFields();
        console.log(data);
        if (a == true) {
            $http.post(BASE_URL + "patient/login/", JSON.stringify(data))
                .then(function (res) {
                    console.log(res);
                    console.log(res.data);
                    if (res.data == "not registered") {
                        swal("Not Registered!", "Please Register To Continue!", "error")
                        document.getElementById('out_data').innerHTML = "You Have Not Registered Yet. Please Register To Continue"
                    } else if (res.data == "wrong password") {
                        swal("Wrong Password!", "Please Enter Correct Password!", "error")
                        document.getElementById('out_data').innerHTML = "Invalid Password"
                    } else {
                        var pdata = JSON.stringify(res.data[0]);
                        console.log(pdata);
                        localStorage.setItem("pdata", pdata);
                        window.location.href = "patient-portal.html";
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

myApp.config(function ($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state('signupmessage', {
            // url: '/dashboard/:e/:f',
            url: '/',
            templateUrl: "pages/signup.html",
            controller: 'signupController'
        })
        .state('loginmessage', {
            url: '/pages/login/:a/:b',
            templateUrl: 'pages/login.html',
            controller: 'loginController'

        })

    $urlRouterProvider.otherwise('/');

});
myApp.controller('signupController', function ($scope, $stateParams) {
    $scope.e = $stateParams.e,
        $scope.f = $stateParams.f
})
myApp.controller('loginController', function ($scope, $stateParams) {
    $scope.a = $stateParams.a,
        $scope.b = $stateParams.b
})
// -----
// ---- SIGN UP PAGE