$(document).ready(function () {
  $("#sidebarCollapse").on("click", function () {
    $("#sidebar").addClass("iq-sidebar-active");
    $("#over-lay").addClass("over-lay-active");
  });
});

$(document).ready(function () {
  $("#toggledelete").on("click", function () {
    $("#sidebar").removeClass("iq-sidebar-active");
    $("#over-lay").removeClass("over-lay-active");
  });

  $("#over-lay").on("click", function () {
    $("#sidebar").removeClass("iq-sidebar-active");
    $("#over-lay").removeClass("over-lay-active");
  });
});

/*---------------------------------------------------------------------
        Search input
        -----------------------------------------------------------------------*/
jQuery(document).on("click", function (e) {
  let myTargetElement = e.target;
  let selector, mainElement;
  if (
    jQuery(myTargetElement).hasClass("search-toggle") ||
    jQuery(myTargetElement).parent().hasClass("search-toggle") ||
    jQuery(myTargetElement).parent().parent().hasClass("search-toggle")
  ) {
    if (jQuery(myTargetElement).hasClass("search-toggle")) {
      selector = jQuery(myTargetElement).parent();
      mainElement = jQuery(myTargetElement);
    } else if (jQuery(myTargetElement).parent().hasClass("search-toggle")) {
      selector = jQuery(myTargetElement).parent().parent();
      mainElement = jQuery(myTargetElement).parent();
    } else if (
      jQuery(myTargetElement).parent().parent().hasClass("search-toggle")
    ) {
      selector = jQuery(myTargetElement).parent().parent().parent();
      mainElement = jQuery(myTargetElement).parent().parent();
    }
    if (
      !mainElement.hasClass("active") &&
      jQuery(".navbar-list li").find(".active")
    ) {
      jQuery(".navbar-list li").removeClass("iq-show");
      jQuery(".navbar-list li .search-toggle").removeClass("active");
    }

    selector.toggleClass("iq-show");
    mainElement.toggleClass("active");

    e.preventDefault();
  } else if (jQuery(myTargetElement).is(".search-input")) {
  } else {
    jQuery(".navbar-list li").removeClass("iq-show");
    jQuery(".navbar-list li .search-toggle").removeClass("active");
  }
});

/*---------------------------------------------------------------------
   Profile Image Edit
-----------------------------------------------------------------------*/

$(document).ready(function () {
  var readURL = function (input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();

      reader.onload = function (e) {
        $(".profile-pic").attr("src", e.target.result);
      };

      reader.readAsDataURL(input.files[0]);
    }
  };

  $(".file-upload").on("change", function () {
    readURL(this);
  });

  $(".upload-button").on("click", function () {
    $(".file-upload").click();
  });
});
