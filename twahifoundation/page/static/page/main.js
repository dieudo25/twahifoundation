$(document).ready(function () {
  var slider = $("#projects-section .projects-list");
  slider.slick({
    mobileFirst: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    swipeToSlide: true,
    autoplay: false,
    arrows: true,
    infinite: true,
    adaptiveHeight: true,
    prevArrow: $(".prev"),
    nextArrow: $(".next"),
  });

  // Add slideDown animation to Bootstrap dropdown when expanding.
  $(".dropdown").on("show.bs.dropdown", function () {
    $(this).find(".dropdown-menu").first().stop(true, true).slideDown();
  });

  // Add slideUp animation to Bootstrap dropdown when collapsing.
  $(".dropdown").on("hide.bs.dropdown", function () {
    $(this).find(".dropdown-menu").first().stop(true, true).slideUp();
  });
});
