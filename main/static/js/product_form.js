function startLoadingButtonAnimation() {
    $('#register_service_form_submit_button span').fadeIn("slow", function () {
        document.getElementById("register_service_form_submit_button").disabled = true;
        $('#register_service_form_submit_button span').html('<div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>').addClass('me-2')
    })
}

function stopLoadingButtonAnimation() {
    $('#register_service_form_submit_button span').fadeOut("slow", function () {
        $('#register_service_form_submit_button span').html('').removeClass('me-2')
        document.getElementById("register_service_form_submit_button").disabled = false;
    });

}

async function RegisterClientService(data_Send_service) {
    let url = `/api/online-service-register/`
    return $.ajax({
        type: "POST",
        url: url,
        headers: {
            "Authorization": "Basic " + btoa("admin:123asdcvb")
        },
        data: data_Send_service,
        success: function () {
            $().msgpopup({
                text: "Форму успішно відправлено! Скоро наші спеціалісти зв'яжуться з вами!",
                type: 'success',
                time: 3500,
                x: true,
            });
            $('#form_service_register')[0].reset();
            stopLoadingButtonAnimation();
        },
        error: function () {
            $().msgpopup({
                text: "Щось пішло не так. Спробуй пізніше!",
                type: 'error',
                time: 3500,
                x: true,
            });
            stopLoadingButtonAnimation();
        }

    })
}

$(document).on("click", "#register_service_form_submit_button", async function () {
    let required_elems_service = $('#form_service_register .required_input_service')
    let service_valid = false
    required_elems_service.each(function () {
        if ($(this).val().length === 0) {
            $(this).css("border-bottom", "1px solid red")
            $().msgpopup({
                text: $(this).attr('placeholder'), type: 'error', time: 3500, x: true,
            });
        } else {
            $(this).css("border-bottom", "1px solid #b8da46")
        }
    });
    if ($('#firstname_service').val().length !== 0 && $('#phone_service').val().length !== 0) {
        service_valid = true
    }
    if (service_valid === true) {
        startLoadingButtonAnimation()
        let data_register_service = $('#form_service_register').serialize();
        await RegisterClientService(data_register_service)
    }
})
