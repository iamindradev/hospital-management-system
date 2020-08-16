var docJson = localStorage.getItem("docAllData");
var myApp = angular.module("myApp", []);
myApp.controller('generateReportController', function ($scope, $http) {
    $scope.makereport = function () {
        var prescription = document.getElementById('prescription').value;
        var instruction = document.getElementById('instruction').value;
        var docId = docJson;
        var data = {
            prescription: prescription,
            further_ins: instruction,
            appntment_id: docId
        }
        console.log(data);
        $http.post(BASE_URL + "doctor/submit_report/", JSON.stringify(data))
            .then(function (response) {
                console.log(response);
                console.log(response.data);
                if (response.data == "report created") {
                    window.location.href = "doctor-portal.html";
                } else {
                    console.log("some error");
                }
            })
    }
})