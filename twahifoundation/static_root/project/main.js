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

  if ($(window).width() < 1200) {
    $(".task-column.task-todo .task-column-title").click(function () {
      $(".task-list.task-todo").toggleClass("task-toggle");
    });

    $(".task-column .task-column-title")
      .not(".task-column.task-todo .task-column-title")
      .click(function () {
        if ($(".task-list").hasClass("task-toggle")) {
          $(".task-list.task-todo").removeClass("task-toggle");
        }
      });

    $(".task-column.task-pending .task-column-title").click(function () {
      $(".task-list.task-pending").toggleClass("task-toggle");
    });

    $(".task-column .task-column-title")
      .not(".task-column.task-pending .task-column-title")
      .click(function () {
        if ($(".task-list").hasClass("task-toggle")) {
          $(".task-list.task-pending").removeClass("task-toggle");
        }
      });

    $(".task-column.task-progress .task-column-title").click(function () {
      $(".task-list.task-progress").toggleClass("task-toggle");
    });

    $(".task-column .task-column-title")
      .not(".task-column.task-progress .task-column-title")
      .click(function () {
        if ($(".task-list").hasClass("task-toggle")) {
          $(".task-list.task-progress").removeClass("task-toggle");
        }
      });

    $(".task-column.task-late .task-column-title").click(function () {
      $(".task-list.task-late").toggleClass("task-toggle");
    });

    $(".task-column .task-column-title")
      .not(".task-column.task-late .task-column-title")
      .click(function () {
        if ($(".task-list").hasClass("task-toggle")) {
          $(".task-list.task-late").removeClass("task-toggle");
        }
      });

    $(".task-column.task-done .task-column-title").click(function () {
      $(".task-list.task-done").toggleClass("task-toggle");
    });

    $(".task-column .task-column-title")
      .not(".task-column.task-done .task-column-title")
      .click(function () {
        if ($(".task-list").hasClass("task-toggle")) {
          $(".task-list.task-done").removeClass("task-toggle");
        }
      });
  }
});
