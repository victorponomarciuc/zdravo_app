function startLoadAnimation() {
    $('#check_up_form_send span').fadeIn("slow", function () {
        document.getElementById("check_up_form_send").disabled = true;
        $('#check_up_form_send span').html('<div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>').addClass('me-2')
    })
}

function stopLoadAnimation() {
    $('#check_up_form_send span').fadeOut("slow", function () {
        $('#check_up_form_send span').html('').removeClass('me-2')
        document.getElementById("check_up_form_send").disabled = false;
    });

}

async function checkUpForm(data_Send) {
    let url = `/api/check-up-form/`
    return $.ajax({
        type: "POST",
        url: url,
        headers: {
            "Authorization": "Basic " + btoa("admin:123asdcvb")
        },
        data: data_Send,
        success: function () {
            $().msgpopup({
                text: "Форму успішно відправлено! Скоро наші спеціалісти зв'яжуться з вами!",
                type: 'success',
                time: 3500,
                x: true,
            });
            $('#check_up_form')[0].reset();
            stopLoadAnimation();
        },
        error: function () {
            $().msgpopup({
                text: "Щось пішло не так. Спробуй пізніше!",
                type: 'error',
                time: 3500,
                x: true,
            });
            stopLoadAnimation();
        }

    })
}

$(document).on("click", "#check_up_form_send", async function () {
    let required_elems = $('#check_up_form .required_input_checkup')
    let check_up_form = false
    required_elems.each(function () {
        if ($(this).val().length === 0) {
            $(this).css("border-bottom", "1px solid red")
            $().msgpopup({
                text: $(this).attr('placeholder'), type: 'error', time: 3500, x: true,
            });
        } else {
            $(this).css("border-bottom", "1px solid #b8da46")
        }
    });
    if ($('#firstname_check_up').val().length !== 0 && $('#phone_check_up').val().length !== 0) {
        check_up_form = true
    }
    if (check_up_form === true) {
        startLoadAnimation()
        let data_check_up = $('#check_up_form').serialize();
        await checkUpForm(data_check_up)
    }
})
