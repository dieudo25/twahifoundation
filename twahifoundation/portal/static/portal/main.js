$(document).ready(function () {
  $("#portal-side-bar-minimize-btn").click(function () {
    $("div.text-wrapper").toggle(250);
    $("#portal-sidebar").toggleClass("portal-sidebar-collapsed");
    $("#toggle-collapse").toggleClass("rotateY180");
  });

  $("#portal-sidebar").click(function () {});
});
