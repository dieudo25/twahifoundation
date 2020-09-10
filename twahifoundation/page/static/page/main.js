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
});

// Render the PayPal button into #paypal-button-container
paypal
  .Buttons({
    // Set up the transaction
    createOrder: function (data, actions) {
      return actions.order.create({
        purchase_units: [
          {
            amount: {
              value: "0.01",
            },
          },
        ],
      });
    },

    // Finalize the transaction
    onApprove: function (data, actions) {
      return actions.order.capture().then(function (details) {
        // Show a success message to the buyer
        alert(
          "Transaction completed by " + details.payer.name.given_name + "!"
        );
      });
    },
  })
  .render("#paypal-button-container");
