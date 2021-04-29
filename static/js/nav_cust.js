$(document).ready(function () {
  $("#sidebarCollapse").on("click", function () {
    $("#sidebar").addClass("iq-sidebar-active");
  });
});

$(document).ready(function () {
  $("#toggledelete").on("click", function () {
    $("#sidebar").removeClass("iq-sidebar-active");
  });
});
