$(document).ready(function () {
     $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },

    });
    // siri configuration
     var siriWave = new SiriWave({
    container: document.getElementById("siri-container"),
    width: 800,
    height: 200,
    speed: 0.30,
    amplitude: 1,
    autostart: true,
    style:"ios9"
  });

  // siri message
  $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,

        },
        out: {
             effect: "fadeOutUp",
            sync: true,
        },

    });

});