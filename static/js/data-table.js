// (function($) {
//   'use strict';
//   $(function() {
//     $('.order-listing').DataTable({
//       "aLengthMenu": [
//         [5, 10, 15, -1],
//         [5, 10, 15, "All"]
//       ],
//       "iDisplayLength": 10,
//       "language": {
//         search: ""
//       },

//     });
//     $('.order-listing').each(function() {
//       var datatable = $(this);
//       // SEARCH - Add the placeholder for Search and Turn this into in-line form control
//       var search_input = datatable.closest('.dataTables_wrapper').find('div[id$=_filter] input');
//       search_input.attr('placeholder', 'Search');
//       search_input.removeClass('form-control-sm');
//       // LENGTH - Inline-Form control
//       var length_sel = datatable.closest('.dataTables_wrapper').find('div[id$=_length] select');
//       length_sel.removeClass('form-control-sm');
//     });
//   });
// })(jQuery);

// // 24 march 2024-> changed "#order-listing" to ".order-listring" and added the order-listing to all the targeted tables in html.


$(document).ready(function () {

  $(function () {
    // Select all tables with class 'order-listing'
    var oTables = $('.order-listing').DataTable({
      "oLanguage": {
        "sSearch": "Search" //Will appear on search form
      },
      fixedHeader: {
        header: true, //Table have header and footer
        footer: true
      },
      autoFill: true, // Autofills fields by dragging the blue dot at the bottom right of cells
      responsive: true, //  Resize table
      rowReorder: true, // Row can be reordered by dragging
      select: true, // selecting rows, cells or columns
      // colReorder: true // Reorders columns
    });
    
    // Loop through each table to add action buttons
    oTables.each(function(index, table) {
      var oTable = $(table).DataTable();
      
      // Adding action buttons to table
      new $.fn.dataTable.Buttons(oTable, {
        name: 'commands',
        buttons: [
          'copy', 'csv', 'excel', 'print'
        ]
      });
      
      // Appends the buttons to the selected element class called "action"
      oTable.buttons(0, null).containers().appendTo('.actions');
    });

    // Datepicker initialization and filtering
    $("#startdate, #enddate").datepicker({
      changeYear: true,
      changeMonth: true,
      dateFormat: "mm/dd/yy",
      onSelect: function (date) {
        var minDate = $("#startdate").datepicker("getDate");
        var maxDate = $("#enddate").datepicker("getDate");
        
        minDateFilter = minDate ? minDate.getTime() : "";
        maxDateFilter = maxDate ? maxDate.getTime() : "";
        
        oTables.each(function(index, table) {
          $(table).DataTable().draw();
        });
      }
    }).keyup(function () {
      var minDate = $("#startdate").datepicker("getDate");
      var maxDate = $("#enddate").datepicker("getDate");
      
      minDateFilter = minDate ? minDate.getTime() : "";
      maxDateFilter = maxDate ? maxDate.getTime() : "";
      
      oTables.each(function(index, table) {
        $(table).DataTable().draw();
      });
    });

  });

  // Date range filter
  minDateFilter = "";
  maxDateFilter = "";

  $.fn.dataTableExt.afnFiltering.push(
    function (oSettings, aData, iDataIndex) {
      if (typeof aData._date == 'undefined') {
        aData._date = new Date(aData[6]).getTime();
      }

      if (minDateFilter && !isNaN(minDateFilter)) {
        if (aData._date < minDateFilter) {
          return false;
        }
      }

      if (maxDateFilter && !isNaN(maxDateFilter)) {
        if (aData._date > maxDateFilter) {
          return false;
        }
      }
      return true;
    }
  );

});
