var patientData = localStorage.getItem("pdata");
patientJson = JSON.parse(patientData);
var myApp = angular.module("myApp", ['ui.router']);
myApp.controller("displayController", function ($scope, $http) {
    $scope.profile = patientJson;
    $scope.$on('$stateChangeSuccess', function () {
        var data = {
            id: patientJson.id
        }
        console.log(data);
        $http.post(BASE_URL + "patient/often/", JSON.stringify(data))
            .then(function (res) {
                console.log(res.data);
                $scope.docData = res.data;
            })
    });
    $scope.$on('$stateChangeSuccess', function () {
        var data = {
            id: patientJson.id
        }
        console.log(data);
        $http.post(BASE_URL + "patient/appointment_history/", JSON.stringify(data))
            .then(function (res) {
                console.log(res.data);
                $scope.datas = res.data;
            })
    });
})

myApp.config(function ($stateProvider, $urlRouterProvider) {
    $stateProvider
        .state('signupmessage', {
            // url: '/dashboard/:e/:f',
            url: '/',
            templateUrl: "pages/patient-dashboard.html",
            controller: 'signupController'
        })
        .state('loginmessage', {
            url: '/pages/login/:a/:b',
            templateUrl: 'pages/medical-history.html',
            controller: 'loginController'

        })
        .state('appointmentmessage', {
            url: '/pages/appointment/:g/:h',
            templateUrl: 'pages/fix-appointment.html',
            controller: 'thirdController'

        })
        .state('notificationmessage', {
            url: '/pages/notifications/:c/:d',
            templateUrl: 'pages/notification.html',
            controller: 'notificationController'

        })
        .state('allappointmentmessage', {
            url: '/pages/allappointment/:i/:j',
            templateUrl: 'pages/all-appointments.html',
            controller: 'allAppointmentController'

        })
        .state('paymentmessage', {
            url: '/pages/payment/:k/:l',
            templateUrl: 'pages/payment-status.html',
            controller: 'paymentController'

        })

    $urlRouterProvider.otherwise('/');

});
myApp.controller("appointmentController", function ($scope, $http) {
    $scope.disease = null;
    $scope.date = null;
    $scope.Time = null;

    $scope.makeappointment = function () {
        var dateValue = document.getElementById('date1').value;
        var timeValue = document.getElementById('time1').value;
        var diseaseValue = document.getElementById('disease1').value;

        var data = {
            disease: diseaseValue,
            date_for_app: dateValue,
            time_for_app: timeValue,
            email: patientJson.email
        }
        console.log(data);
        $http.post(BASE_URL + "patient/make_appointment/", JSON.stringify(data))
            .then(function (res) {
                console.log(res);
                console.log(res.data);
                if (res.data == "added") {
                    document.getElementById('out_data').innerHTML = "Your Appointment Has Been Fixed";
                    window.location.href = "patient-portal.html"
                } else if (res.data == "you already have a pending appointment") {
                    document.getElementById('out_data').innerHTML = "Appointment Not Fixed! You Already Have A Pending Appointment";
                } else {
                    document.getElementById('out_data').innerHTML = "Appointment Not Fixed Some Error";
                }

            })
    }

})

myApp.controller('medicalHistoryController', function ($scope, $http) {
    $scope.$on('$stateChangeSuccess', function () {
        var data = {
            id: patientJson.id
        }
        console.log(data);
        $http.post(BASE_URL + "patient/all_report/", JSON.stringify(data))
            .then(function (res) {
                console.log(res.data);
                $scope.appointments = res.data;

            })
    });
})

function sendAppId(value) {
    localStorage.setItem("patAppId", value);
    console.log(value);
}
myApp.controller('notificationsController', function ($scope, $http) {
    var appIdJson = localStorage.getItem("patAppId");
    $scope.$on('$stateChangeSuccess', function () {
        var data = {
            id: patientJson.id
        }
        console.log(data);
        $http.post(BASE_URL + "patient/notifications/", JSON.stringify(data))
            .then(function (res) {
                console.log(res.data);
                console.log(res.data.approved_seen);
                console.log(res.data.modified_seen);
                $scope.datas1 = res.data.approved_active;
                $scope.datas2 = res.data.modified_active;
                $scope.datas3 = res.data.modified_seen;
                $scope.datas = res.data.approved_seen;

            })
    });
    $scope.cancelappointment = function () {
        var data = {
            id: appIdJson,
            activity: "rejected"
            // id: "4"
        }
        console.log(data);
        $http.post(BASE_URL + "patient/cancel_appointment/", JSON.stringify(data))
            .then(function (res) {
                console.log(res.data);
            })
    }
})

function getReport(value) {
    localStorage.setItem("patAppId", value);
    console.log(value);
}
myApp.controller('allAppointmentDisplayController', function ($scope, $http) {
    $scope.$on('$stateChangeSuccess', function () {
        var data = {
            id: patientJson.id
        }
        console.log(data);
        $http.post(BASE_URL + "patient/appointment_history/", JSON.stringify(data))
            .then(function (res) {
                console.log(res.data);
                $scope.datas = res.data;

            })
    });
    $scope.getreport = function () {
        window.location.href = "get-report.html";
    }
})

myApp.controller('paymentDisplayController', function ($scope, $http) {
    $scope.$on('$stateChangeSuccess', function () {
        var data = {
            id: patientJson.id
        }
        console.log(data);
        $http.post(BASE_URL + "patient/appointment_history/", JSON.stringify(data))
            .then(function (res) {
                console.log(res.data);
                $scope.datas = res.data;

            })
    });
    $scope.getreport = function () {
        window.location.href = "get-report.html";
    }
})
// ---
myApp.controller('signupController', function ($scope, $stateParams) {
    $scope.e = $stateParams.e,
        $scope.f = $stateParams.f
})
myApp.controller('loginController', function ($scope, $stateParams) {
    $scope.a = $stateParams.a,
        $scope.b = $stateParams.b
})
myApp.controller('thirdController', function ($scope, $stateParams) {
    $scope.g = $stateParams.g,
        $scope.h = $stateParams.h
})
myApp.controller('notificationController', function ($scope, $stateParams) {
    $scope.c = $stateParams.c,
        $scope.d = $stateParams.d
})
myApp.controller('allAppointmentController', function ($scope, $stateParams) {
    $scope.i = $stateParams.i,
        $scope.j = $stateParams.j
})
myApp.controller('paymentController', function ($scope, $stateParams) {
    $scope.k = $stateParams.k,
        $scope.l = $stateParams.l
})