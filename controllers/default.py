# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## This is a sample controller
## - index is the default action of any application
## - user is required for authentication and authorization
## - download is for downloading files uploaded in the db (does streaming)
## - call exposes all registered services (none by default)
#########################################################################
import gluon.contrib.simplejson

@auth.requires_membership('admin') #descomentar para habilitar segurança
def index():
    """
    example action using the internationalization operator T and flash
    rendered by views/default/index.html or views/generic.html

    if you need a simple wiki simply replace the two lines below with:
    return auth.wiki()
    """    
    return dict()


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/manage_users (requires membership in
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    """
    return dict(form=auth())


@auth.requires_membership('admin') #descomentar para habilitar segurança
def usuarios():
    #db.auth_user.id.readable = False
    btn = lambda row: A(T('Edit'), _href=URL('manage_user', args=row.auth_user.id))
    db.auth_user.edit = Field.Virtual(btn)
    rows = db(db.auth_user).select()
    headers = ['Name', 'Last Name', 'Email', 'Edit']
    fields = ['first_name', 'last_name', 'email', 'edit']
    table = TABLE(THEAD(TR(*[B(header) for header in headers])),
        TBODY(*[TR(*[TD(row[field]) for field in fields]) for row in rows]))
    table['_class'] = 'table table-striped table-condensed'
    return dict(table=table)


@auth.requires_membership('admin') #descomentar para habilitar segurança
def manage_user():
    user_id = request.args(0) or redirect(URL('usuarios'))
    db.auth_user.id.readable = False
    form = SQLFORM(db.auth_user, user_id)
    if form.accepts(request.vars, session):
        redirect(URL('usuarios'))
    membership_panel = LOAD(request.controller,
                            'manage_membership',
                            args=[user_id],
                            ajax=True)
    return dict(form=form, membership_panel=membership_panel)


@auth.requires_membership('admin') #descomentar para habilitar segurança
def manage_membership():
    user_id = request.args(0) or redirect(URL('usuarios'))
    db.auth_membership.user_id.default = int(user_id)
    db.auth_membership.user_id.writable = False
    db.auth_membership.id.readable = False
    form = SQLFORM.grid(db.auth_membership.user_id == user_id,
                        args=[user_id],
                        searchable=False,
                        deletable=False,
                        details=False,
                        selectable=False,
                        sortable=False,
                        csv=False)
    return form

@auth.requires_membership('admin') #descomentar para habilitar segurança
def grupos():
    db.auth_group.id.readable = False
    form = SQLFORM.grid(db.auth_group, searchable=False, deletable=False, details=False, selectable=False, csv=False)
    return dict(form=form)


@auth.requires_membership('admin') #descomentar para habilitar segurança
def novo_usuario():
    form = SQLFORM(db.auth_user)
    if form.accepts(request.vars, session):
        user_id = form.vars.id
        #torna o novo usuário membro do grupo admin
        auth.add_membership(2, user_id)
        redirect(URL('usuarios'))
    return dict(form=form)

@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()


@auth.requires_signature()
def data():
    """
    http://..../[app]/default/data/tables
    http://..../[app]/default/data/create/[table]
    http://..../[app]/default/data/read/[table]/[id]
    http://..../[app]/default/data/update/[table]/[id]
    http://..../[app]/default/data/delete/[table]/[id]
    http://..../[app]/default/data/select/[table]
    http://..../[app]/default/data/search/[table]
    but URLs must be signed, i.e. linked with
      A('table',_href=URL('data/tables',user_signature=True))
    or with the signed load operator
      LOAD('default','data.load',args='tables',ajax=True,user_signature=True)
    """
    return dict(form=crud())

def upload_file():
    """
    File upload handler for the ajax form of the plugin jquery-file-upload
    Return the response in JSON required by the plugin
    """
    try:
        # Get the file from the form
        #f = request.vars['arquivos']
        
        # Store file
        id = db.arquivo.insert(arquivo = db.arquivo.arquivo.store(request.vars.file, request.vars.filename))
         
        # Compute size of the file and update the record
        # record = db.arquivos[id]
        # path_list = []
        # path_list.append(request.folder)
        # path_list.append('uploads')
        # path_list.append(record['arquivo'])
        # size =  shutil.os.path.getsize(shutil.os.path.join(*path_list))
        # File = db(db.arquivos.id==id).select()[0]
        # db.arquivos[id] = dict(tamanho=size)
        # db.arquivos[id] = dict(id_secao=response.session_id)
         
        # res = dict(files=[{"name": str(f.filename), "size": size, "url": URL(f='download', args=[File['arquivo']]), "thumbnail_url": URL(f='download', args=[File['thumb']]), "delete_url": URL(f='delete_file', args=[File['arquivo']]), "delete_type": "DELETE" }])
        #res = dict(id=id)
        #return gluon.contrib.simplejson.dumps(res, separators=(',',':'))
        return id

    except:
        return dict(message=T('Upload error'))

 
def delete_file():
        """
        Delete an uploaded file
        """
        try:
            name = request.args[0]
            db(db.arquivo.arquivo==name).delete()
            return name
        except:
            return 'erro'
 
 
def upload():
        return dict()