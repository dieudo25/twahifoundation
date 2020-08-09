$(document).ready(function () {
  /* $("#portal-side-bar-minimize-btn").click(function () {
    $("div.text-wrapper").toggle(250);
    $("#portal-sidebar").toggleClass("portal-sidebar-collapsed");
    $("#toggle-collapse").toggleClass("rotateY180");
  }); */

  var sidebarState = sessionStorage.getItem("sidebarState");

  windowWidth = $(window).width();

  $(window).resize(function () {
    windowWidth = $(window).width();

    if (windowWidth < 992) {
      //992 is the value of $screen-md-min in boostrap variables.scss
      $("#portal-sidebar").addClass("portal-sidebar-collapsed");
      $("#toggle-collapse").addClass("rotateY180");
      $("div.text-wrapper").addClass("hide");
    } else {
      if (sidebarState) {
        $("#portal-sidebar").addClass("portal-sidebar-collapsed");
        $("#toggle-collapse").addClass("rotateY180");
        $("div.text-wrapper").addClass("hide");
      } else {
        $("#portal-sidebar").removeClass("portal-sidebar-collapsed");
        $("#toggle-collapse").removeClass("rotateY180");
        $("div.text-wrapper").removeClass("hide");
      }
    }
  });

  function setSidebarState(value) {
    sessionStorage.setItem("sidebarState", value);
  }

  function clearSidebarState() {
    sessionStorage.removeItem("sidebarState");
  }

  function collapseSidebar() {
    $("#portal-sidebar").addClass("portal-sidebar-collapsed");
    $("#toggle-collapse").addClass("rotateY180");
    $("div.text-wrapper").addClass("hide");
  }

  function expandSidebar() {
    $("#portal-sidebar").removeClass("portal-sidebar-collapsed");
    $("#toggle-collapse").removeClass("rotateY180");
    $("div.text-wrapper").removeClass("hide");
  }

  $(function () {
    /** check sessionStorage to expand/collapse sidebar onload **/

    if (sidebarState == "collapsed") {
      collapseSidebar();
    } else {
      if (windowWidth < 992) {
        //992 is the value of $screen-md-min in boostrap variables.scss
        $("#portal-sidebar").addClass("portal-sidebar-collapsed");
        $("#toggle-collapse").addClass("rotateY180");
        $("div.text-wrapper").addClass("hide");
      } else {
        if (sidebarState) {
          $("#portal-sidebar").addClass("portal-sidebar-collapsed");
          $("#toggle-collapse").addClass("rotateY180");
          $("div.text-wrapper").addClass("hide");
        } else {
          $("#portal-sidebar").removeClass("portal-sidebar-collapsed");
          $("#toggle-collapse").removeClass("rotateY180");
          $("div.text-wrapper").removeClass("hide");
        }
      }
    }

    /** collapse the sidebar navigation **/

    $("#toggle-collapse").click(function () {
      if (!$("#portal-sidebar").hasClass("portal-sidebar-collapsed")) {
        // if sidebar is not yet collapsed
        collapseSidebar();
        setSidebarState("collapsed");
      } else {
        expandSidebar();
        clearSidebarState();
      }
      return false;
    });
  });
});
