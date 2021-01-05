
function gestionForm(url, formulario){    
    $.ajax({
        type: 'POST',
        url: url,
        data: formulario,            
        success: function(data){
            $('#modal').modal('toggle');
            swal({
                icon: data.icon,
                title: data.title,
                text: data.text
            })
            .then(() => {
                location.reload();
            });
        }
    });
}

function ejecutarModal(url){
    $("#modal").load(url, function(){
        $(this).modal('show')  
    }) 
}