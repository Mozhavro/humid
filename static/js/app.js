// TODO check if selected date is bigger than today
(function( $ ) {

    $(window).on('load', function(){
        // Initial data
        var d = new Date();
        var current_month = d.getMonth();
        var current_year = d.getFullYear();

        var past_month = current_month - 1;
        var year = current_year;
        if(past_month < 1) {
            past_month = 12 - past_month;
            year -= 1;
        }

        // start and end dates of last month
        var startDay = new Date(year, past_month, 1);
        var endDay = new Date(year, past_month + 1, 0);

        updateGraphForPeriod(startDay, endDay);

        $('#month').on('change', function () {
            var selected = $(this).val();

            var d = new Date(selected),
                month = d.getMonth(),
                year = d.getFullYear();

            var startDay = new Date(year, month, 1);
            var endDay = new Date(year, month+1, 0, 0);

            updateGraphForPeriod(startDay, endDay);
        });
    });

})( jQuery );


function updateGraphForPeriod(startDate, endDate) {
    $.ajax({
        url: "/temperature-between-dates",
        type: 'GET',
        data: {
            start: startDate.getTime()/1000,
            end: endDate.getTime()/1000
        },

        success: function (resp) {
            var data = JSON.parse(resp);
            updateGraph("graph", data);
        }
    });
}


function updateGraph(id, data, label, color) {
    if(label === undefined)
        label = "Temperature";

    if(color === undefined)
        color = "#3e95cd";

    var data_arr = Object.keys( data ).map(function ( key ) { return data[key]; });

    var dates = [];
    Object.keys(data).sort().map(function(key, index) {
        var date = new Date(key*1000);
        var curr_date = date.getDate();
        var curr_month = date.getMonth() + 1;
        var curr_year = date.getFullYear();
        dates.push(curr_date + "." + curr_month + "." + curr_year);
    });

    new Chart(document.getElementById(id), {
      type: 'line',
      data: {
        labels: dates,
        datasets: [{
            data: data_arr,
            label: "Temperature",
            borderColor: "#3e95cd",
            fill: false
          },
        ]
      },
    });
}