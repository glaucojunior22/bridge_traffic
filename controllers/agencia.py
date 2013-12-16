# coding: utf8
@auth.requires_membership('admin') #descomentar para habilitar segurança
def index():
    db.agencia.id.readable = False
    form = SQLFORM.grid(query=db.agencia, user_signature=False, csv=False, searchable=False, paginate=20, details=False, sortable=False)
    return dict(form=form)

'''
def nova():
    update = db.agencia(request.args())
    form = SQLFORM(db.agencia, update)
    if form.accepts(request.vars, session):
        response.flash = 'Sucesso!'
    elif form.errors:
        response.flash = 'Erros!'
    else:
        response.flash = 'Preencha os campos!'
    return dict(form=form)

def editar():
    record = db.agencia(request.args(0)) or redirect(URL('index'))
    form = SQLFORM(db.agencia, record)
    if form.accepts(request.vars, session):
        response.flash('Sucesso!')
    elif form.errors:
        response.flash('Erros!')
    return dict(form=form)
'''