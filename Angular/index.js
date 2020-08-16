var a = 0;
$(window).scroll(function () {

    var oTop = $('#counter').offset().top - window.innerHeight;
    if (a == 0 && $(window).scrollTop() > oTop) {
        $('.counter-value').each(function () {
            var $this = $(this),
                countTo = $this.attr('data-count');
            $({
                countNum: $this.text()
            }).animate({
                countNum: countTo
            },

                {

                    duration: 2000,
                    easing: 'swing',
                    step: function () {
                        $this.text(Math.floor(this.countNum));
                    },
                    complete: function () {
                        $this.text(this.countNum);
                        //alert('finished');
                    }

                });
        });
        a = 1;
    }
    if ($(document).scrollTop() > 50) {
        document.getElementById('navbar-box').style.height = '7vh';
        document.getElementById('navbar-box').style.background = 'rgba(0, 0, 0,0.5)';
        document.getElementById('navlink1').style.color = '#ffffff';
        document.getElementById('navlink2').style.color = '#ffffff';
        document.getElementById('navlink3').style.color = '#ffffff';
        document.getElementById('navlink4').style.color = '#ffffff';
        document.getElementById('navlink5').style.color = '#ffffff';
        document.getElementById('navlink6').style.color = '#ffffff';
        // document.getElementsById('navlink7').style.color = '#ffffff';

    } else {
        document.getElementById('navbar-box').style.height = '11vh';
        document.getElementById('navbar-box').style.background = '#ffffff';
        document.getElementById('navlink1').style.color = '#444444';
        document.getElementById('navlink2').style.color = '#444444';
        document.getElementById('navlink3').style.color = '#444444';
        document.getElementById('navlink4').style.color = '#444444';
        document.getElementById('navlink5').style.color = '#444444';
        document.getElementById('navlink6').style.color = '#444444';
    }
});