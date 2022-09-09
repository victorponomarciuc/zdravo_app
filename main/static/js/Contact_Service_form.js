$(document).on("click", "#contact_service_form_submit_button", async function () {
    let service_form = $('#form_service_contact .required_input_fs')
    let is_valid_sf = false
    service_form.each(function () {
        if ($(this).val().length === 0) {
            $(this).css("border-bottom", "1px solid red")
            $().msgpopup({
                text: $(this).attr('placeholder'), type: 'error', time: 3500, x: true,
            });
        } else {
            $(this).css("border-bottom", "1px solid #b8da46")
        }
    });
    if ($('#firstname_fs').val().length !== 0 && $('#phone_fs').val().length !== 0) {
        is_valid_sf = true
    }
    if (is_valid_sf === true) {
        startLoadingAnimationFS()
        let data_Send_fs = $('#form_service_contact').serialize();
        await getClients(data_Send_fs)
    }
})