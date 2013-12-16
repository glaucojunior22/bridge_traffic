# -*- coding: utf8 -*-
@auth.requires_membership('admin') #descomentar para habilitar segurança
def index():
    db.campanha.id.readable = False
    fields = (db.campanha.nome, db.campanha.data_inicio, db.campanha.data_fim)
    form = SQLFORM.grid(query=db.campanha, user_signature=False, csv=False, searchable=False, paginate=20, details=False, sortable=False, fields=fields)
    return dict(form=form)

'''
def index():
    db.campanha.id.readable = False
    query = ((db.campanha.id > 0))
    fields = (db.campanha.nome, db.campanha.data_inicio, db.campanha.data_fim)
    headers = {'campanha.nome': 'Nome', 'campanha.data_inicio': 'Data inicial', 'campanha.data_fim': 'Data final'}
    sort = [db.campanha.data_inicio]
    lista = SQLFORM.grid(query=query, fields=fields, headers=headers, orderby=sort, paginate=20)
    return dict(lista=lista)

def nova():
    form = SQLFORM(db.campanha)
    if form.accepts(request.vars, session):
        response.flash = 'Sucesso!'
    elif form.errors:
        response.flash = 'Erros!'
    else:
        response.flash = 'Preencha os campos!'
    return dict(form=form)

def editar():
    record = db.campanha(request.args(0)) or redirect(URL('index'))
    form = SQLFORM(db.campanha, record, deletable=True, upload = URL('download'))
    if form.accepts(request.vars, session):
        response.flash('Sucesso!')
    elif form.errors:
        response.flash('Erros!')
    return dict(form=form)
'''