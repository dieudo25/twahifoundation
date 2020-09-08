$(document).ready(function () {
  $("#portal-side-bar-minimize-btn").click(function () {
    $("div.text-wrapper").toggleClass("hide");
    $("#portal-sidebar").toggleClass("portal-sidebar-collapsed");
    $("#toggle-collapse").toggleClass("rotateY180");
  });

  $(".super").click(function () {
    console.log("heheheh");
    $("#portal-sidebar").addClass("portal-sidebar-collapsed");
    $("#toggle-collapse").addClass("rotateY180");
    $("div.text-wrapper").addClass("hide");
  });
});
