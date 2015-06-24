$( document ).ready(function() {
// CSRF protection setup

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

// CSRF protection setup END


    $('a[act="runscript"]').click(function () {

        var script_id = $(this).attr("script_id")
        var spinner = '<i class="fa fa-cog fa-spin fa-2x"></i>'
        $('#stdOut').empty();
        $('#stdOut').html(spinner);
        $('#stdErr').html(spinner);

        $.ajax({
            url: '/',
            data: {
                script_id: script_id,
            },
            type: 'POST',
            dataType : 'json',
            success: function(data) {
                if (data.stdout){
                    $('#stdOut').empty();
                    $('#stdOut').html(data.stdout);
                } else {
                    $('#stdOut').html('No data.');
                }

                if (data.stderr) {
                    $('#stdErr').empty();
                    $('#stdErr').html(data.stderr);
                } else {
                    $('#stdErr').html('No data.');
                }
            },
            error: function( status, errorThrown ) {
                $('#stdOut').html('No data.');
                $('#stdErr').html('No data.');
                $('#appErr').show();
                $('#appErr').html("Web application error!" + "<br/><br/>" + "Error description: " + errorThrown );
                console.log( "Error: " + errorThrown );
                console.log( "Status: " + status );
            },
        });
    });

});