$(document).ready(function () {
  $("#portal-side-bar-minimize-btn").click(function () {
    $("div.text-wrapper").toggleClass("hide");
    $("#portal-sidebar").toggleClass("portal-sidebar-collapsed");
    $("#toggle-collapse").toggleClass("rotateY180");
  });

  $(".super").click(function () {
    $("#portal-sidebar").addClass("portal-sidebar-collapsed");
    $("#toggle-collapse").addClass("rotateY180");
    $("div.text-wrapper").addClass("hide");
  });

  // Add slideDown animation to Bootstrap dropdown when expanding.
  $(".dropdown").on("show.bs.dropdown", function () {
    $(this).find(".dropdown-menu").first().stop(true, true).slideDown();
  });

  // Add slideUp animation to Bootstrap dropdown when collapsing.
  $(".dropdown").on("hide.bs.dropdown", function () {
    $(this).find(".dropdown-menu").first().stop(true, true).slideUp();
  });
  console.log($("#portal-sidebar"));
  if ($("#portal-sidebar").length != 1) {
    $(".sidebar-clearfix").css({ "margin-left": "0" });
  }
});
