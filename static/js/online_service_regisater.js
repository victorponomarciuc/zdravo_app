function sla() {
    $('#online_register_form_submit_button_custom span').fadeIn("slow", function () {
        document.getElementById("online_register_form_submit_button_custom").disabled = true;
        $('#online_register_form_submit_button_custom span').html('<div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>').addClass('me-2')
    })
}

function stopLA() {
    $('#online_register_form_submit_button_custom span').fadeOut("slow", function () {
        $('#online_register_form_submit_button_custom span').html('').removeClass('me-2')
        document.getElementById("online_register_form_submit_button_custom").disabled = false;
    });

}

async function RegisterClientOnlineService(data_Send_service) {
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
            $('#form_online_register_new')[0].reset();
            stopLA();
        },
        error: function () {
            $().msgpopup({
                text: "Щось пішло не так. Спробуй пізніше!",
                type: 'error',
                time: 3500,
                x: true,
            });
            stopLA();
        }

    })
}

$(document).on("click", "#online_register_form_submit_button_custom", async function () {
    let required_form_elem_service = $('#form_online_register_new .required_input_online_register_new')
    let service_online_valid = false
    required_form_elem_service.each(function () {
        if ($(this).val().length === 0) {
            $(this).css("border-bottom", "1px solid red")
        } else {
            $(this).css("border-bottom", "1px solid #b8da46")
        }
    });
    if ($('#firstname_online_register_new').val().length !== 0 && $('#phone_online_register_number_new').val().length !== 0) {
        service_online_valid = true
    }
    if (service_online_valid === true) {
        sla()
        let data_register_online_service = $('#form_online_register_new').serialize();
        await RegisterClientOnlineService(data_register_online_service)
    }
})
