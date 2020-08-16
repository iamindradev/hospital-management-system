 var departmentValue = localStorage.getItem("departmentData2");
 var patientJson = localStorage.getItem("PatientId");
 var departmentJson = JSON.parse(departmentValue);
 var myApp = angular.module("myApp", []);
 myApp.controller("modifyAppointmentController", function ($scope, $http) {
     $scope.departments = departmentJson;
     $scope.getdoctors = function (department) {
         var data = {
             department: department
         }
         console.log(data);
         $http.post(BASE_URL + "manager/assign_doctor/", JSON.stringify(data))
             .then(function (res) {
                 console.log(res);
                 console.log(res.data);
                 $scope.datas = res.data;
             })
     }
     $scope.modifyappointment = function () {
         var doctorName = document.getElementById('doctor').value;
         var time = document.getElementById('time').value;
         var date = document.getElementById('date').value;
         var arr = doctorName.split(",");
         var id = arr[0];
         console.log(id);
         var data = {
             patient_id: patientJson,
             doct_key_id: id,
             date_for_app: date,
             time_for_app: time,
             activity: "modified"
         }
         console.log(data);
         $http.post(BASE_URL + "manager/approve_appointment/", JSON.stringify(data))
             .then(function (res) {
                 console.log(res);
                 console.log(res.data);
                 if (res.data = "approved") {
                     window.location.href = "manager-portal.html";
                 } else {
                     alert("Not Submitted Some Issue")
                 }
             })
     }
 });