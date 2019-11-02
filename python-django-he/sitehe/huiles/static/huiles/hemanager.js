$(document).ready(
function(){

  // Main tabs
  var main_tabs = $("#tabs").tabs({"active": 0});
  var current_search = $(location).attr('search');
  if (current_search != "") {
    main_tabs.tabs({"active": 1});
  }

  // Main accordion
  $("#he-list").accordion({
      heightStyle: "content",
      active: false,
      collapsible: true
  });

  // Tableaux des familles
  $('.famille-display').DataTable({
        "paging":   false,
        "ordering": false,
        "info":     false,
        "searching": false,
        "columnDefs": [
            { className: "dt-body-center", "targets": [ 0, 1, 2 ] }
        ]
  });
  $('.proprietes-display').DataTable({
        "paging":   false,
        "ordering": false,
        "info":     false,
        "searching": false,
        "columnDefs": [
            { className: "dt-body-center", "targets": [ 0, 1 ] }
        ]
  });
  $('.dataTables_wrapper').css("width","600px")

  // Filtering - Contre Indication menu
  $("select#contre_indic").multiselect();
  $("select#property").multiselect();
  $("select#family").multiselect();

  // Submit filtering
  $(".he-search input[type=submit]").button();

})