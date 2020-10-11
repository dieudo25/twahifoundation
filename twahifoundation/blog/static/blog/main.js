$(document).ready(function () {
  var slider = $(".slider-form-langage");
  slider.slick({
    mobileFirst: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    swipeToSlide: true,
    autoplay: false,
    arrows: true,
    dots: true,
    customPaging: function (slider, i) {
      // this example would render "tabs" with titles
      return (
        '<span class="dot btn-black">' +
        $(slider.$slides[i]).attr("title") +
        "</span>"
      );
    },
    infinite: true,
    adaptiveHeight: false,
    prevArrow: $(".prev"),
    nextArrow: $(".next"),
  });
});
