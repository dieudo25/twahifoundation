$(document).ready(function () {
  // get boutton
  btn = $("#hide-cookie-consent");

  // Assigning event listeners to the button

  btn.on("click", function () {
    setCookie("cookie_consent", true, 30);
    $("#cookie-consent").hide();
    console.log("ok");
  });
});

function setCookie(cname, cvalue, exdays) {
  var d = new Date();
  d.setTime(d.getTime() + exdays * 24 * 60 * 60 * 1000);
  var expires = "expires=" + d.toUTCString();
  document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
}
