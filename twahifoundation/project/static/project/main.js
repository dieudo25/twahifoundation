$(document).ready(function () {
  var slider = $(".participant-list");
  slider.slick({
    mobileFirst: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    arrows: true,
    infinite: true,
    adaptiveHeight: true,
    swipeToSlide: true,
    prevArrow: $(".prev"),
    nextArrow: $(".next"),
    responsive: [
      {
        breakpoint: 767,
        settings: {
          slidesToShow: 3,
          slidesToScroll: 1,
        },
      },
      {
        breakpoint: 1199,
        settings: {
          slidesToShow: 4,
        },
      },
    ],
  });
});
