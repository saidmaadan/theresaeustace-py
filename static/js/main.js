(function ($) {
"use strict";

/*---------------------------------------------------------------------------------------
    Data Background Active
-----------------------------------------------------------------------------------------*/
    $("[data-background]").each(function () {
        $(this).css("background-image", "url(" + $(this).attr("data-background") + ")")
    });
/*---------------------------------------------------------------------------------------
    Sticky Header Active
-----------------------------------------------------------------------------------------*/
    // sticky Header layout 1
    $(window).on('scroll', function () {
        var scroll = $(window).scrollTop();
        if (scroll < 70) {
          $("#header-sticky").removeClass("sticky");
        } else {
          $("#header-sticky").addClass("sticky");
        }
    });
    // sticky Header layout 2
    $(window).on('scroll', function () {
        var scroll = $(window).scrollTop();
        if (scroll < 70) {
          $("#mobile-header-sticky").removeClass("mobile-sticky");
        } else {
          $("#mobile-header-sticky").addClass("mobile-sticky");
        }
    });

/*---------------------------------------------------------------------------------------
    Slick Slider Active
-----------------------------------------------------------------------------------------*/  
// mainSlider
    function mainSlider() {
        var BasicSlider = $('.slider-active');
        BasicSlider.on('init', function (e, slick) {
            var $firstAnimatingElements = $('.single-slider:first-child').find('[data-animation]');
            doAnimations($firstAnimatingElements);
        });
        BasicSlider.on('beforeChange', function (e, slick, currentSlide, nextSlide) {
            var $animatingElements = $('.single-slider[data-slick-index="' + nextSlide + '"]').find('[data-animation]');
            doAnimations($animatingElements);
        });
        BasicSlider.slick({
            autoplay: true,
            autoplaySpeed: 10000,
            dots: true,
            fade: true,
            arrows: true,
            pauseOnHover:false,
            prevArrow:'<i class="fas fa-chevron-left"></i>',
            nextArrow:'<i class="fas fa-chevron-right"></i>',
            responsive: [
            {
              breakpoint: 993,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                infinite: true,
                arrows: false,
              }
            },
            {
              breakpoint: 767,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: false,
                dots: true,
              }
            },
            {
              breakpoint: 480,
              settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
                arrows: false,
                dots: true,
              }
            }
          ]
        });

        function doAnimations(elements) {
            var animationEndEvents = 'webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend';
            elements.each(function () {
                var $this = $(this);
                var $animationDelay = $this.data('delay');
                var $animationType = 'animated ' + $this.data('animation');
                $this.css({
                    'animation-delay': $animationDelay,
                    '-webkit-animation-delay': $animationDelay
                });
                $this.addClass($animationType).one(animationEndEvents, function () {
                    $this.removeClass($animationType);
                });
            });
        }
    }
    mainSlider();
/*---------------------------------------------------------------------------------------
    Team Member slider active
-----------------------------------------------------------------------------------------*/
    $('.team-member-active').slick({
        autoplay: false,
        infinite: true,
        slidesToShow: 4,
        slidesToScroll: 1,
        dots: false,
        arrows: true,
        autoplaySpeed: 10000,
        prevArrow:'<i class="fas fa-chevron-left"></i>',
        nextArrow:'<i class="fas fa-chevron-right"></i>',
        responsive: [
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 4,
            slidesToScroll: 1,
            infinite: true,
          }
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 576,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
    });
/*---------------------------------------------------------------------------------------
    Blog post slider active
-----------------------------------------------------------------------------------------*/
    $('.latest-blog-active').slick({
        autoplay: false,
        infinite: true,
        slidesToShow: 3,
        slidesToScroll: 3,
        dots: true,
        arrows: false,
        autoplaySpeed: 10000,
        prevArrow:'<i class="fas fa-chevron-left"></i>',
        nextArrow:'<i class="fas fa-chevron-right"></i>',
        responsive: [
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1,
            infinite: true,
          }
        },
        {
          breakpoint: 992,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
    });
/*---------------------------------------------------------------------------------------
    Brand Slider active
-----------------------------------------------------------------------------------------*/
    $('.brands-active').slick({
        autoplay: false,
        infinite: true,
        slidesToShow: 5,
        slidesToScroll: 2,
        dots: false,
        arrows: false,
        autoplaySpeed: 5000,
        responsive: [
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 4,
            slidesToScroll: 1,
            infinite: true,
          }
        },
        {
          breakpoint: 993,
          settings: {
            slidesToShow: 3,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 480,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
    });

/*---------------------------------------------------------------------------------------
    Author Review active
-----------------------------------------------------------------------------------------*/
    $('.testimonial-active').slick({
        autoplay: false,
        infinite: true,
        dots: true,
        arrows: false,
        slidesToScroll: 2,
        slidesToShow: 2,
        autoplaySpeed: 10000,
        prevArrow:'<i class="fas fa-chevron-left"></i>',
        nextArrow:'<i class="fas fa-chevron-right"></i>',
        responsive: [
        {
          breakpoint: 1200,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1,
            infinite: true,
          }
        },
        {
          breakpoint: 993,
          settings: {
            slidesToShow: 2,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 768,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        },
        {
          breakpoint: 576,
          settings: {
            slidesToShow: 1,
            slidesToScroll: 1
          }
        }
      ]
    });
/*---------------------------------------------------------------------------------------
    Magnific popup Active
-----------------------------------------------------------------------------------------*/
    // image popup
    $('.popup-pic').magnificPopup({
        type: 'image',
        gallery:{
            enabled:true
        }
    });
    // video popup
    $('.popup-video').magnificPopup({
        type: 'iframe'
    });
/*---------------------------------------------------------------------------------------
    Scroll to top Active
-----------------------------------------------------------------------------------------*/
    $.scrollUp({
        scrollName: 'scrollUp', // Element ID
        topDistance: '300', // Distance from top before showing element (px)
        topSpeed: 300, // Speed back to top (ms)
        animation: 'fade', // Fade, slide, none
        animationInSpeed: 200, // Animation in speed (ms)
        animationOutSpeed: 200, // Animation out speed (ms)
        scrollText: '<i class="fas fa-chevron-up"></i>', // Text for element
        activeOverlay: false, // Set CSS color to display scrollUp active point, e.g '#00FFFF'
    });
/*---------------------------------------------------------------------------------------
    Wow Animation Active
-----------------------------------------------------------------------------------------*/ 

    var wow = new WOW(
  {
    boxClass:     'wow',      // animated element css class (default is wow)
    animateClass: 'animated', // animation css class (default is animated)
    offset:       0,          // distance to the element when triggering the animation (default is 0)
    mobile:       true,       // trigger animations on mobile devices (default is true)
    live:         true,       // act on asynchronously loaded content (default is true)
    callback:     function(box) {
      // the callback is fired every time an animation is started
      // the argument that is passed in is the DOM node being animated
    },
    scrollContainer: null,    // optional scroll container selector, otherwise use window,
    resetAnimation: true,     // reset animation on end (default is true)
  }
);
wow.init();
/*---------------------------------------------------------------------------------------
    Preloader Active
-----------------------------------------------------------------------------------------*/
    function loader() {
        $(window).on('load', function () {
            $('body').addClass('loaded');
            $("#loading").fadeOut(500);
            // Una vez haya terminado el preloader aparezca el scroll

            if ($('body').hasClass('loaded')) {
                // Es para que una vez que se haya ido el preloader se elimine toda la seccion preloader
                $('#preloader').delay(900).queue(function () {
                    $(this).remove();
                });
            }
        });
    }
    loader();

})(jQuery); 

setTimeout(function(){
  $('#message').fadeOut('slow')
}, 10000)