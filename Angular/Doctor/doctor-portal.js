var doctorData = localStorage.getItem("docdata");
console.log(doctorData);
doctorJson = JSON.parse(doctorData);
console.log(doctorJson.email);

// --
var myApp = angular.module("myApp", ['ui.router']);

myApp.controller('docDisplayController', function ($scope, $http) {
    $scope.docprofile = doctorJson;
    $scope.$on('$stateChangeSuccess', function () {
        var data = {
            id: doctorJson.id
        }
        console.log(data);
        $http.post(BASE_URL + "doctor/patient_list/", JSON.stringify(data))
            .then(function (response) {
                console.log(response.data);
                // console.log(response.data.data[0]);
                $scope.datas = response.data;
            })
    });
    $scope.$on('$stateChangeSuccess', function () {
        var data = {
            id: doctorJson.id
        }
        console.log(data);
        $http.post(BASE_URL + "doctor/report_list/", JSON.stringify(data))
            .then(function (response) {
                console.log(response.data);
                // console.log(response.data.data[0]);
                $scope.data = response.data;
            })
    });
})

function viewDetails(value) {
    localStorage.setItem("docPatientId", value);
    console.log(value);
}
myApp.controller('patientListController', function ($scope, $http) {
    $scope.$on('$stateChangeSuccess', function () {
        var data = {
            id: doctorJson.id
        }
        console.log(data);
        $http.post(BASE_URL + "doctor/patient_list/", JSON.stringify(data))
            .then(function (response) {
                console.log(response.data);
                // console.log(response.data.data[0]);
                $scope.datas = response.data;
            })
    });

    $scope.getpatientdetail = function () {
        window.location.href = "patient-detail.html";
    }
})
myApp.controller('docPortalController', function ($scope, $http) {

})

function getPatientId(value) {
    localStorage.setItem("docPatientId", value);
    console.log(value);
}
myApp.controller("pendingAppointmentDisplayController", function ($scope, $http) {
    $scope.$on('$stateChangeSuccess', function () {
        var data = {
            id: doctorJson.id
        }
        console.log(data);
        $http.post(BASE_URL + "doctor/pending_appointments/", JSON.stringify(data))
            .then(function (response) {
                console.log(response.data);
                $scope.datas = response.data;
                console.log($scope.datas);
            })

    });
    $scope.approveappointment = function () {
        $scope.idData = localStorage.getItem("docPatientId");
        var data = {
            patient_id: $scope.idData,
            id: doctorJson.id,
            activity: "approved"
        }
        console.log(data);
        $http.post(BASE_URL + "doctor/approve_appointments/", JSON.stringify(data))
            .then(function (res) {
                console.log(res);
                console.log(res.data);

            })

    }
    $scope.modifyappointment = function () {
        localStorage.setItem("id", doctorJson.id)
        window.location.href = "modify-appointment.html"
    }
    $scope.rejectappointment = function () {
        var id = $scope.idData;
        console.log(id);
        var data = {
            patient_id: id,
            activity: "rejected"
        }
        console.log(data);
        $http.post(BASE_URL + "doctor/reject_appointments/", JSON.stringify(data))
            .then(function (res) {
                console.log(res);
                console.log(res.data);
            })
    }
});

function getAllData(value) {
    localStorage.setItem("docAllData", value);
    console.log(value);
}
myApp.controller('makeReportController', function ($scope, $http) {
    $scope.$on('$stateChangeSuccess', function () {
        var data = {
            id: doctorJson.id
        }
        console.log(data);
        $http.post(BASE_URL + "doctor/generate_report/", JSON.stringify(data))
            .then(function (response) {
                console.log(response.data);
                $scope.datas = response.data;
                console.log($scope.datas);
            })

    });

    $scope.generatereport = function () {
        window.location.href = "generate-report.html";
    }
})

function getReport(value) {
    localStorage.setItem("appId", value);
    console.log(value);
}
myApp.controller('reportListController', function ($scope, $http) {
    $scope.$on('$stateChangeSuccess', function () {
        var data = {
            id: doctorJson.id
        }
        console.log(data);
        $http.post(BASE_URL + "doctor/report_list/", JSON.stringify(data))
            .then(function (response) {
                console.log(response.data);
                $scope.datas = response.data;
                console.log($scope.datas);
            })

    });

    $scope.getreport = function () {
        window.location.href = "get-report.html"
    }
})

// ---

myApp.config(function ($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state('signupmessage', {
            // url: '/dashboard/:e/:f',
            url: '/',
            templateUrl: "pages-doc/doctor-dashboard.html",
            controller: 'signupController'
        })
        .state('allpatientmessage', {
            url: '/pages/login/:a/:b',
            templateUrl: 'pages-doc/patient-list.html',
            controller: 'loginController'

        })
        .state('appointmentmessage', {
            url: '/pages/appointment/:c/:d',
            templateUrl: 'pages-doc/pending-appointments.html',
            controller: 'appointmentController'

        })
        .state('reportmessage', {
            url: '/paages/report/:g/:h',
            templateUrl: 'pages-doc/make-report.html',
            controller: 'reportController'

        })
        .state('allreportmessage', {
            url: '/paages/allreport/:i/:j',
            templateUrl: 'pages-doc/report-list.html',
            controller: 'allReportController'

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
myApp.controller('appointmentController', function ($scope, $stateParams) {
    $scope.c = $stateParams.c,
        $scope.d = $stateParams.d
})
myApp.controller('reportController', function ($scope, $stateParams) {
    $scope.g = $stateParams.g,
        $scope.h = $stateParams.h
})
myApp.controller('allReportController', function ($scope, $stateParams) {
    $scope.i = $stateParams.i,
        $scope.j = $stateParams.j
})