var myApp = angular.module("myApp", []);
myApp.controller("registrationController", function ($scope, $http) {
    // var firstName = document.getElementById("first_name").value
    // var lastName = document.getElementById("last_name").value;
    // var mobileNumber = document.getElementById("mobile_number").value;
    // var a = firstName.substr(0, 2);
    // console.log(a);
    // var b = lastName.substr(0, 2);
    // var c = mobileNumber.substr(6, 4);
    // var medicalId = a + b + c;
    // $scope.medicalid = medicalId;
    $scope.firstname = null;
    $scope.lastname = null;
    $scope.mobilenumber = null;
    $scope.email = null;
    $scope.gender = "Gender";
    $scope.password = null;
    $scope.age = "Age";
    $scope.department = "Department";
    $scope.qualification = "Qualification";
    $scope.experience = "Experience";


    $scope.postdata = function (firstname, lastname, mobilenumber, email, gender, password, age, department, qualification, experience) {

        var data = {
            first_name: firstname,
            last_name: lastname,
            mobile_number: mobilenumber,
            email: email,
            gender: gender,
            password: password,
            age: age,
            department: department,
            qualification: qualification,
            previous_exp: experience,
        }
        var a = onSubmit();
        if (a == true) {
            console.log(data);
            $http.post(BASE_URL + "doctor/register/", JSON.stringify(data))
                .then(function (res) {
                    console.log(res);
                    console.log(res.data);
                    if (res.data == "success") {
                        document.getElementById('out_data').innerHTML = "You Have Successfully Registered! Need To Wait For Manager Apporval For Login";
                        swal("Registered Successfully!", "Need To Wait For Manager Apporval For Login!", "success");
                    } else {
                        swal("Not Registered!", "Some Error Occured", "error");
                        document.getElementById('out_data').innerHTML = "Not able to register some error ocuured";
                    }
                })
        } else {
            console.log("not send");
        }

    }
});
// ---
// ---
function validateFirstName(a, b) {
    var name = document.getElementById(a).value;
    // const namValue = name.trim();
    var alphabet = /^[A-Za-z]+$/;
    if (name.match(alphabet)) {
        document.getElementById(b).innerHTML = "";
        $("#first_name").css("border", "1px solid green");
        return true;
    } else {
        document.getElementById(b).innerHTML = "Enter Valid Name";
        $("#first_name").css("border", "2px solid red");
    }
}

function validateLastName(a, b) {
    var name = document.getElementById(a).value;
    // const namValue = name.trim();
    var alphabet = /^[A-Za-z]+$/;
    if (name.match(alphabet)) {
        document.getElementById(b).innerHTML = "";
        $("#last_name").css("border", "1px solid green");
        return true;
    } else {
        document.getElementById(b).innerHTML = "Enter Valid Name";
        $("#last_name").css("border", "2px solid red");
    }
}

function validateNumber(a, b) {
    var mobileNumber = document.getElementById(a).value;
    const mobileNumberValue = mobileNumber.trim();
    if (mobileNumberValue == "") {
        document.getElementById(b).innerHTML = "Enter Your Mobile Number";
        $("#mobile_number").css("border", "2px solid red");
    } else if ((mobileNumberValue.charAt(0) != 9) && (mobileNumberValue.charAt(0) != 8) && (mobileNumberValue.charAt(0) != 7) && (mobileNumberValue.charAt(0) != 6)) {
        document.getElementById(b).innerHTML = "Mobile No.start with 6,7,8,9";
        $("#mobile_number").css("border", "2px solid red");
    } else if (mobileNumberValue.length != 10) {
        document.getElementById(b).innerHTML = "Must be of 10 digits";
        $("#mobile_number").css("border", "2px solid red");
    } else {
        document.getElementById(b).innerHTML = "";
        $("#mobile_number").css("border", "1px solid green");
        return true;
    }
}

function validateEmail(a, b) {
    var email = document.getElementById(a).value;
    var emailValue = email.trim();
    var arr = emailValue.split("@");
    var alphabet = /^[A-Za-z0-9@|.]+$/;

    if (emailValue.match(alphabet)) {
        if (emailValue == "") {
            document.getElementById(b).innerHTML = "Enter Valid Email";
            $("#email").css("border", "2px solid red");
        } else if ((emailValue.indexOf('@') == 0) || (emailValue.indexOf('.') == 0)) {
            document.getElementById(b).innerHTML = "Enter Valid Email";
            $("#email").css("border", "2px solid red");
        } else if ((emailValue.charAt(0) == 9) || (emailValue.charAt(0) == 8) || (emailValue.charAt(0) == 7) || (emailValue.charAt(0) == 6) || (emailValue.charAt(0) == 5) || (emailValue.charAt(0) == 4) || (emailValue.charAt(0) == 3) || (emailValue.charAt(0) == 2) || (emailValue.charAt(0) == 1) || (emailValue.charAt(0) == 0)) {
            document.getElementById(b).innerHTML = "Enter Valid Email";
            $("#email").css("border", "2px solid red");
        } else if (arr.length > 2) {
            document.getElementById(b).innerHTML = "Enter Valid Email";
            $("#email").css("border", "2px solid red");
        } else if (emailValue.lastIndexOf('.') - emailValue.indexOf('@') < 5) {
            document.getElementById(b).innerHTML = "Enter Valid Email";
            $("#email").css("border", "2px solid red");
        } else if (emailValue.lastIndexOf('.') >= (emailValue.length - 2)) {
            document.getElementById(b).innerHTML = "Enter Valid Email";
            $("#email").css("border", "2px solid red");
        } else if ((emailValue.indexOf('@') == -1) || (emailValue.indexOf('.') == -1)) {
            document.getElementById(b).innerHTML = "Enter Valid Email";
            $("#email").css("border", "2px solid red");
        } else {
            document.getElementById(b).innerHTML = "";
            $("#email").css("border", "1px solid green");
            return true;
        }
    } else {
        document.getElementById(b).innerHTML = "Enter Valid Email";
        $("#email").css("border", "2px solid red");
    }
}

function validatePassword(a, b) {
    var password = document.getElementById(a).value;

    if (password == "") {
        document.getElementById(b).innerHTML = "Enter Your Password";
        $("#password").css("border", "2px solid red");
    } else if (password.length < 6) {
        $("#password").css("border", "2px solid red");
        document.getElementById(b).innerHTML = "Password must be of 6 digits";
    } else {
        document.getElementById(b).innerHTML = "";
        $("#password").css("border", "1px solid green");

        return true;
    }

}

function validateCnfPassword(a, b) {
    var password = document.getElementById('password').value;
    var cnfPassword = document.getElementById(a).value;
    if (cnfPassword == "") {
        document.getElementById(b).innerHTML = "Re-Enter Your Password";
        $("#cnfpassword").css("border", "2px solid red");
    } else if (password != cnfPassword) {
        document.getElementById('cnfpassworderror').innerHTML = "Passwords do not match";
        $("#cnfpassword").css("border", "2px solid red");
    } else {
        document.getElementById(b).innerHTML = "";
        $("#cnfpassword").css("border", "1px solid green");
        return true;
    }
}

function validateAge(a, b) {
    var age = document.getElementById(a).value;
    if (age == "Age") {
        document.getElementById(b).innerHTML = "Enter Your Age";
    } else {
        document.getElementById(b).innerHTML = "";
        return true;
    }
}

function validateGender(a, b) {
    var gender = document.getElementById(a).value;
    if (gender == "Gender") {
        document.getElementById(b).innerHTML = "Enter Your Gender";
        console.log(gender);
    } else {
        document.getElementById(b).innerHTML = "";
        console.log(gender);
        return true;
    }
}

function validateDepartment(a, b) {
    var department = document.getElementById(a).value;
    if (department == "Department") {
        document.getElementById(b).innerHTML = "Enter Your Department";
        console.log(department);
    } else {
        document.getElementById(b).innerHTML = "";
        console.log(department);
        return true;
    }
}

function validateExperience(a, b) {
    var experience = document.getElementById(a).value;
    if (experience == "Experience") {
        document.getElementById(b).innerHTML = "Enter Your Experience";
        console.log(experience);
    } else {
        document.getElementById(b).innerHTML = "";
        console.log(experience);
        return true;
    }

}

function validateQualification(a, b) {
    var qualification = document.getElementById(a).value;
    if (qualification == "Qualification") {
        document.getElementById(b).innerHTML = "Enter Your Qualification";
        console.log(qualification);
    } else {
        document.getElementById(b).innerHTML = "";
        console.log(qualification);
        return true;
    }
}



function onSubmit() {
    var a = validateFirstName('first_name', 'firstnameerror');
    var b = validateLastName('last_name', 'lastnameerror');
    var c = validateNumber('mobile_number', 'mobilenumbererror');
    var d = validateEmail('email', 'emailerror');
    var e = validateCnfPassword('cnfpassword', 'cnfpassworderror');
    var f = validatePassword('password', 'passworderror');
    var g = validateAge('age', 'ageerror');
    var h = validateQualification('qualification', 'qualificationerror');
    var i = validateExperience('experience', 'experienceerror')
    var j = validateGender('gender', 'gendererror');
    var k = validateDepartment('department', 'departmenterror')
    if ((a == true) && (b == true) && (c == true) && (d == true) && (e == true) && (f == true) && (g == true) && (h == true) && (i == true) && (j == true) && (k == true)) {
        // sendRegistrationData();
        console.log("RIGHT");
        return true;

        // postdata(firstname, lastname, mobilenumber, email, gender, password, age, qualification, experience);

    } else {
        // alert("Fill All Fields")
        console.log("WRONG");
    }
}