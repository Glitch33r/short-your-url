$(document).ready(function () {
    $("#btnCut").click(function () {
        let btn = $(this);
        $(this).prop("disabled", true);
        // add spinner to button
        $(this).html(
            `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...`
        );

        $.ajax({
            type: "POST",
            url: "/generate",
            headers: {
                "X-CSRFToken": Cookies.get('csrftoken')
            },
            data: {
                'url': $('#input-base').val()
            },
            success: function (data) {
                if (data.status) {
                    console.log(data.msg);
                    btn.removeAttr('disabled');
                    btn.html(`Cut`);
                } else {
                    btn.removeAttr('disabled');
                    btn.html(`Cut`);
                    alert(data.msg);
                }
            }
        });
    });
});

$(document).ready(function () {
    $("#btnInfo").click(function () {
        let btn = $(this);
        // disable button
        $(this).prop("disabled", true);
        // add spinner to button
        $(this).html(
            `<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Loading...`
        );

        $.ajax({
            type: "POST",
            url: "/get-info",
            headers: {
                "X-CSRFToken": Cookies.get('csrftoken')
            },
            data: {
                'url': $('#input-base').val()
            },
            success: function (data) {
                if (data.status) {
                    console.log(data.msg);
                    btn.removeAttr('disabled');
                    btn.html(`Get info`);
                } else {
                    alert(data.msg);
                }

            },
        });
    });
});