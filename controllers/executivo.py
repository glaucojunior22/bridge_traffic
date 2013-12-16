# -*- coding:utf-8 -*-
@auth.requires_membership('admin') #descomentar para habilitar segurança
def index():
	db.executivo.id.readable = False
	form = SQLFORM.grid(query=db.executivo, user_signature=False, csv=False, searchable=False, paginate=20, details=False, sortable=False)
	return dict(form=form)