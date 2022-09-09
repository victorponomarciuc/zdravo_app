function startLoadingAnimation() {
    $('#contact_form_submit_button span').fadeIn("slow", function () {
        document.getElementById("contact_form_submit_button").disabled = true;
        $('#contact_form_submit_button span').html('<div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>').addClass('me-2')
    })
}

function stopLoadingAnimation() {
    $('#contact_form_submit_button span').fadeOut("slow", function () {
        $('#contact_form_submit_button span').html('').removeClass('me-2')
        document.getElementById("contact_form_submit_button").disabled = false;
    });

}

function startLoadingAnimationFS() {
    $('#contact_service_form_submit_button span').fadeIn("slow", function () {
        document.getElementById("contact_service_form_submit_button").disabled = true;
        $('#contact_service_form_submit_button span').html('<div class="lds-roller"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>').addClass('me-2')
    })
}

function stopLoadingAnimationFS() {
    $('#contact_service_form_submit_button span').fadeOut("slow", function () {
        $('#contact_service_form_submit_button span').html('').removeClass('me-2')
        document.getElementById("contact_service_form_submit_button").disabled = false;
    });

}

async function getClients(data_Send) {
    let url = `/api/contact-form/`
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
            $('#form_contact')[0].reset();
            stopLoadingAnimation();
            stopLoadingAnimationFS();
        },
        error: function () {
            $().msgpopup({
                text: "Щось пішло не так. Спробуй пізніше!",
                type: 'error',
                time: 3500,
                x: true,
            });
            stopLoadingAnimation();
            stopLoadingAnimationFS();
        }

    })
}

$(document).on("click", "#contact_form_submit_button", async function () {
    let required_elems = $('#form_contact .required_input')
    let is_valid = false
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
    if ($('#firstname').val().length !== 0 && $('#phone').val().length !== 0) {
        is_valid = true
    }
    if (is_valid === true) {
        startLoadingAnimation()
        let data_Send = $('#form_contact').serialize();
        await getClients(data_Send)
    }
})
