  // Date filter
  /* 
      Copy this in the script tag of the target html page 
      and make sure to change the column number as the first argument
      in the call to filterByDate(column, startDate, endDate) (in line 32)
  */

  $(function () {
    // Basic Setup
    var $tableSel = $('.order-listing')
    $tableSel.dataTable({
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
      colReorder: true // Reorders columns
    });


    $('#filter').on('click', function (e) {
      e.preventDefault();
      var startDate = $('#start').val(),
        endDate = $('#end').val();

      filterByDate(7, startDate, endDate); // We call our filter function

      $tableSel.dataTable().fnDraw(); // Manually redraw the table after filtering
    });

    $('#clearFilter').on('click', function (e) {
      e.preventDefault();
      $.fn.dataTableExt.afnFiltering.length = 0;
      $tableSel.dataTable().fnDraw();
    });

  });

  function parseDate(str) {
    var parts = str.split('/');
    return new Date(parts[2], parts[1] - 1, parts[0]);
  }
  function normalizeDate(dateString) {
    var date = new Date(dateString);
    var normalized = date.getFullYear() + '' + (("0" + (date.getMonth() + 1)).slice(-2)) + '' + ("0" + date.getDate()).slice(-2);
    // console.log(normalized)
    return normalized;
  }
  var filterByDate = function (column, startDate, endDate) {
    // Custom filter syntax requires pushing the new filter to the global filter array
    $.fn.dataTableExt.afnFiltering.push(
      function (oSettings, aData, iDataIndex) {
        var rowDate = normalizeDate(parseDate(aData[column])),
          start = normalizeDate(startDate),
          end = normalizeDate(endDate);
        // If our date from the row is between the start and end
        if (start <= rowDate && rowDate <= end) {
          return true;
        } else if (rowDate >= start && end === '' && start !== '') {
          return true;
        } else if (rowDate <= end && start === '' && end !== '') {
          return true;
        } else {
          return false;
        }
      }
    );
  };
