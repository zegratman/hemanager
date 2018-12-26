$(document).ready(
function(){

  // Main tabs
  $("#tabs").tabs({"active": 0});

  var form_array = $('form').serializeArray()
  if (form_array.length != 0) {
    $("#tabs").tabs("option", "active", 1);
  }

  // Main accordion
  $("#he-list").accordion();

  // Filtering - Contre Indication menu
  $("#contre_indic").selectmenu();

  // Submit filtering
  $(".he-search input[type=submit]").button();

})