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

        $.ajax({
            url: "/temperature-between-dates",
            type: 'GET',
            data: {
                start: startDay.getTime()/1000,
                end: endDay.getTime()/1000
            },

            success: function (resp) {
                var data = JSON.parse(resp);
                var data_arr = Object.keys( data ).map(function ( key ) { return data[key]; });
                console.log(data);

                // var t_scale_min = Math.min.apply(Math, data_arr) -2;
                // var t_scale_max = Math.max.apply(Math, data_arr) +2;

                var dates = [];
                Object.keys(data).map(function(key, index) {
                    var date = new Date(key*1000);
                    var curr_date = date.getDate();
                    var curr_month = date.getMonth() + 1;
                    var curr_year = date.getFullYear();
                    dates.push(curr_date + "." + curr_month + "." + curr_year);
                });
                console.log(dates);

                new Chart(document.getElementById("graph"), {
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
        });
    });

})( jQuery );