# -*- coding:utf-8 -*-
@auth.requires_membership('admin') #descomentar para habilitar segurança
def index():
	db.atendimento.id.readable = False
	form = SQLFORM.grid(query=db.atendimento, user_signature=False, csv=False, searchable=False, paginate=20, details=False, sortable=False)
	return dict(form=form)
'''
def index():
	lista = db(db.atendimento.id>0).select()
	return dict(lista=lista)

def editar():
	db.atendimento.id.readable = False
	registro = db.atendimento(request.args(0))# or redirect(URL('index'))
	form = SQLFORM(db.atendimento, registro)
	form.add_button('Voltar', URL('index'))
	if form.process().accepted:
		#response.flash = 'Sucesso!'
		redirect(URL('index'))
	elif form.errors:
		response.flash = 'Erros encontrados!'
	return dict(form = form)

def excluir():
	pass
'''