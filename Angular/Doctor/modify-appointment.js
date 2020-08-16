var myApp = angular.module("myApp", []);
myApp.controller("modifyAppointmentController", function ($scope, $http) {
    $scope.modifyappointment = function () {
        var patientJson = localStorage.getItem("docPatientId")
        var idJson = localStorage.getItem("id");
        var time = document.getElementById('time').value;
        var date = document.getElementById('date').value;
        var data = {
            patient_id: patientJson,
            id: idJson,
            date_for_app: date,
            time_for_app: time,
            activity: "modified"
        }
        console.log(data);
        $http.post(BASE_URL + "doctor/approve_appointments/", JSON.stringify(data))
            .then(function (res) {
                console.log(res);
                console.log(res.data);
                if (res.data = "modified") {
                    window.location.href = "doctor-portal.html";
                } else {
                    alert("Not Submitted Some Issue")
                }
            })
    }
});