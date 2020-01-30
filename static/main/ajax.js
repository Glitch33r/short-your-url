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
            url: "/shot-url",
            headers: {
                "X-CSRFToken": Cookies.get('csrftoken')
            },
            data: {
                'url': $('#input-base').val()
            },
            success: function (data) {
                if (data.status) {
                    $('.blockquote').remove();
                    $(`<blockquote class="blockquote"><p class="mb-0"><a href="` + data.msg + `">` + data.msg + `</a></p></blockquote>`).insertAfter('#base');
                    btn.removeAttr('disabled');
                    btn.html(`Cut`);
                } else {
                    $('.blockquote').remove();
                    btn.removeAttr('disabled');
                    btn.html(`Cut`);
                    $(`<blockquote class="blockquote"><p class="mb-0">` + data.msg + `</p></blockquote>`).insertAfter('#base');
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
                'slug': $('#input-info').val()
            },
            success: function (data) {
                if (data.status) {
                    $('.blockquote').remove();
                    $(`<blockquote class="blockquote"><p class="mb-0"><a href="` + data.msg + `">` + data.msg + `</a></p></blockquote>`).insertAfter('#info');
                    btn.removeAttr('disabled');
                    btn.html(`Get info`);
                } else {
                    $('.blockquote').remove();
                    btn.removeAttr('disabled');
                    btn.html(`Get info`);
                    $(`<blockquote class="blockquote"><p class="mb-0">` + data.msg + `</p></blockquote>`).insertAfter('#info');
                }
            },
        });
    });
});