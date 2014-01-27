$(document).ready(function(){
    //Função para adicionar agência via ajax
    $('#campanha_agencia').parent().append('<p><a data-toggle="modal" href="#form-content" class="btn btn-primary">Nova Agência</a></p>');
    //Função para exibir o campo de editorias somente se a campanha for Patrocinio
    $('#campanha_editorias__row').hide();
    $('#campanha_tipo').change(function(){
        if($('#campanha_tipo option:selected').text() == 'Patrocinio'){
            $('#campanha_editorias__row').show();
        }else{
            $('#campanha_editorias__row').hide();
        }
        });
    //Função para listar os arquivos existentes
    $('#campanha_arquivos option:selected').each(function(){
        var file = $(this).text();
        $('#campanha_arquivos').parent().append('<p id="'+file+'"><a class="btn btn-success btn-download" href="http://'+window.location.host+'/traffic/default/download/'+file+'">Baixar Arquivo</a><button type="button" class="btn btn-danger excluir"><span class="icon-white icon-trash"></span></button></p>');
    });
    //Função para excluir os arquivos
    $('button.excluir').click(function(){
        var arq = $(this).parent().attr('id');
        $(this).parent().hide();
        $.ajax({
            url: 'http://'+window.location.host+'/traffic/default/delete_file/'+arq,
            type: 'post',
            data: arq,
            success: function(data){
                if (data != 'erro'){
                    $('#campanha_arquivos option:selected').each(function(){
                        var file = $(this).text();
                        if(file == data){
                        $(this).remove();
                        }
                    });
                }else{                            
                    alert('Erro ao excluir arquivo!');
                }
            },
            error: function(){
                alert('Erro ao excluir arquivo, verifique sua conexão!');
            }
        });
    });
    //Função para tratar os uploads via ajax
    arquivos = $('#campanha_arquivos');
    arquivos.parent().append('<input class="upload" id="file_upload" name="file_upload" type="file">');
    arquivos.hide();
    $('#file_upload').pekeUpload({
        btnText: 'Adicionar',
        url: 'http://' + window.location.host + '/traffic/default/upload_file',
        theme: 'bootstrap',
        showErrorAlerts: false,
        onFileError: function(file,error){
            $('#campanha_arquivos').append($('<option>', {value: error, text: error, selected: true}));
            $('div.pekecontainer').append('<div class="alert alert-success"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">×</button><p>'+file['name']+' adicionado com sucesso!</p></div>');
        }
    });
});