$(function () {
    $(document).scroll(function () {
      var $nav = $(".nav-wrapper");
      var $splash = $(".parallax")
      $nav.toggleClass('scrolled', $(this).scrollTop() > $splash.height() - $nav.height());
    });
  });