$(document).ready(function() {
//open challenges
$('.open-challenges table tr').each(function(){
$(this).find('th:last').addClass('take');
$(this).find('td:nth-child(1)').addClass('name');
$(this).find('th:nth-child(2)').addClass('passed-ch');
$(this).find('th:nth-child(3)').addClass('summary');
$(this).find('td:nth-child(4)').addClass('success-rate');
$(this).find('th:nth-child(4)').addClass('success-rate');
});


// add class leader board page
$('.leaderboard-table table tbody tr:odd').addClass('odd');
$('.leaderboard-table table tbody tr:even').addClass('even');
    $('.leaderboard-table table tr').each(function(){
        $(this).find('th:nth-child(1)').addClass('rank');
        $(this).find('td:nth-child(1)').addClass('rank');
        $(this).find('th:nth-child(2)').addClass('name');
        $(this).find('td:nth-child(2)').addClass('name');
        $(this).find('th:nth-child(3)').addClass('rankingpoints');
        $(this).find('td:nth-child(3)').addClass('rankingpoints');
        $(this).find('th:nth-child(4)').addClass('location');
        $(this).find('td:nth-child(4)').addClass('location');
        $(this).find('th:nth-child(5)').addClass('languages');
        $(this).find('td:nth-child(5)').addClass('languages');
    });

    $('[data-element="dev-accept-invitations"], [data-element="dev-decline-invitations"]').click(function(){
        $.ajax({
            type: "POST",
            url: $(this).attr("x-data-url"),
            data: { action: $(this).attr("data-action") }
        })
        .done(function(data, textStatus, jqXHR) {
            if (data["success"] == true){
                location.reload();
            }
        })
        .fail(function() {
        })
        .always(function() {
        });
    });
});


