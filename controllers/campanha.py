# -*- coding: utf8 -*-
@auth.requires_membership('admin') #descomentar para habilitar segurança
def index():
    if len(request.args)>1 and request.args[-2] == 'new':
        js = '''
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
            //Função para tratar os uploads via ajax
            arquivos = $('#campanha_arquivos');
            arquivos.parent().append('<input class="upload" id="file_upload" name="file_upload" type="file">');
            //arquivos.css({'width':'1px','height':'1px','visibility':'hidden'});
            arquivos.hide();
            $('#file_upload').pekeUpload({
                btnText: 'Adicionar',
                url: 'http://' + window.location.host + '/traffic/default/upload_file',
                theme: 'bootstrap',
                showErrorAlerts: false,
                onFileError: function(file,error){
                    $('#campanha_arquivos').append($('<option>', {value: error, text: error, selected: true}));
                }
                });
            '''
    elif len(request.args)>1 and request.args[-3] == 'edit':
        js = '''
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
                $('#campanha_arquivos').parent().append('<p id="'+file+'"><a href="http://'+window.location.host+'/traffic/default/download/'+file+'">ARQUIVO</a> <button type="button" class="btn-xs btn-danger excluir"><span class="icon-white icon-trash"></span></button></p>');
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
                            //$('#campanha_arquivos option[value='+data+']').remove();
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
            //arquivos.css({'width':'1px','height':'1px','visibility':'hidden'});
            arquivos.hide();
            $('#file_upload').pekeUpload({
                btnText: 'Adicionar',
                url: 'http://' + window.location.host + '/traffic/default/upload_file',
                theme: 'bootstrap',
                showErrorAlerts: false,
                onFileError: function(file,error){
                    $('#campanha_arquivos').append($('<option>', {value: error, text: error, selected: true}));
                    //$('div.pekecontainer').hide();
                    //$('div.alert-error').css('display','none');
                }
                });

            '''
                    
    else:
        js = ''
    script = SCRIPT(js, _type="text/javascript")
    db.campanha.id.readable = False
    fields = (db.campanha.nome, db.campanha.data_inicio, db.campanha.data_fim)
    form = SQLFORM.grid(query=db.campanha, user_signature=False, csv=False,
                        searchable=False, paginate=20, sortable=False, details=False,
                        fields=fields, orderby=[~db.campanha.data_inicio, ~db.campanha.data_fim])
    return dict(form=form, script=script)

'''
@auth.requires_membership('admin') #descomentar para habilitar segurança
def index():
    db.campanha.id.readable = False
    query = ((db.campanha.id > 0))
    fields = (db.campanha.nome, db.campanha.data_inicio, db.campanha.data_fim)
    headers = {'campanha.nome': 'Nome', 'campanha.data_inicio': 'Data inicial', 'campanha.data_fim': 'Data final'}
    sort = [db.campanha.data_inicio]
    lista = SQLFORM.grid(query=query, fields=fields, headers=headers, orderby=sort, paginate=20)
    return dict(lista=lista)

@auth.requires_membership('admin') #descomentar para habilitar segurança
def nova():
    form = SQLFORM(db.campanha)
    if form.accepts(request.vars, session):
        response.flash = 'Sucesso!'
    elif form.errors:
        response.flash = 'Erros!'
    else:
        response.flash = 'Preencha os campos!'
    return dict(form=form)

@auth.requires_membership('admin') #descomentar para habilitar segurança
def editar():
    record = db.campanha(request.args(0)) or redirect(URL('index'))
    form = SQLFORM(db.campanha, record, deletable=True, upload = URL('download'))
    if form.accepts(request.vars, session):
        response.flash('Sucesso!')
    elif form.errors:
        response.flash('Erros!')
    return dict(form=form)
'''