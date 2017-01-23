(function() {

    $(document).on('click', 'input[type=checkbox]#id_same_number', function(){
        var $this = $(this),
            $mobileNumber = $('#id_mobile_number'),
            $whatsappNumber = $('#id_whatsapp_number');

        if ($(this).is(':checked')) {
            $whatsappNumber.val($mobileNumber.val());
            $whatsappNumber.attr('readonly', true);
        } else {
            $whatsappNumber.attr('readonly', false);
        }
    });


})()
