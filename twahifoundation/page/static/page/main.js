$(document).ready(function () {
  var slider = $("#projects-section .projects-list");
  slider.slick({
    mobileFirst: true,
    slidesToShow: 1,
    slidesToScroll: 1,
    swipeToSlide: true,
    autoplay: true,
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

  var scroll = $("portal-section").scrollTop();

  $(window)
    .scroll(function () {
      if ($(this).scrollTop() > 75) {
        $("a[href='#top']").fadeIn();
      } else {
        $("a[href='#top']").fadeOut();
      }
    })
    .trigger("scroll");

  // Scroll to the top
  $("a[href='#top']").click(function () {
    $("section.portal-section").animate({ scrollTop: 0 }, "fast");
    $("html, body").animate({ scrollTop: 0 }, "slow");
    return false;
  });
});
