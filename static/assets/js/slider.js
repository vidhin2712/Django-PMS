if ($.fn.slick !== undefined && $(".top-projects").length > 0) {
    jQuery(".top-projects").slick({
        slidesToShow: 3,
        speed: 300,
        slidesToScroll: 1,
        focusOnSelect: true,
        autoplay: false,
        arrows: true,
        appendArrows: jQuery('#top-project-slick-arrow'),
        responsive: [
        {
            breakpoint: 1199,
            settings: {
            arrows: false,
            slidesToShow: 3,
            },
        },
        {
            breakpoint: 991,
            settings: {
            arrows: false,
            slidesToShow: 2,
            },
        },
        {
            breakpoint: 550,
            settings: {
            arrows: false,
            autoplay: true,
            slidesToShow: 1,
            },
        },
        ],
    });
}

var swiper = new Swiper(".home-slider", {
    spaceBetween: 20,
    grabCursor : true,
    loop: true,
    centeredSlides: true,
    autoplay: {
        delay: 9500,
        disableOnInteraction: false,
      }
  });
