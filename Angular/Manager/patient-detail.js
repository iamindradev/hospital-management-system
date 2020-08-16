var docIdJson = localStorage.getItem("manPatientId");
var myApp = angular.module("myApp", []);
myApp.controller('patientDetailController', function ($scope, $http) {
    $scope.$watch('$viewContentLoaded', function () {
        var data = {
            id: docIdJson
        }
        console.log(data);
        $http.post(BASE_URL + "manager/see_details_patient/", JSON.stringify(data))
            .then(function (response) {
                console.log(response.data);
                console.log(response.data.basic_data);
                $scope.profile = response.data.basic_data[0];
                $scope.appointments = response.data.all_appointments
                // console.log($scope.profile);
            })
    });

})