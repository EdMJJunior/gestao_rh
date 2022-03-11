function utilizouHoraExtra(id){
    console.log('função');
    token = document.getElementsByName("csrfmiddlewaretoken")[0].value;

    $.ajax({
        type: 'post',
        url: '/hora_extra/utilizou-hora-extra/' + id + '/',
        data: {
            csrfmiddlewaretoken: token
        },
        success: function(result){
            console.log('success');
            $("mensagem").text('Foi');
        },


    });

};