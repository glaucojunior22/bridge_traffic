# coding: utf8
#validador pré-definido
not_empty = IS_NOT_EMPTY(error_message=msg_erro['empty'])
#tabela de agências
db.define_table('agencia',
                Field('agencia', notnull=True),
                Field('nome', notnull=True),
                Field('email', notnull=True),
                format='%(nome)s - %(agencia)s')
#validadores da tabela agencia
db.agencia.email.requires = IS_EMAIL(error_message=msg_erro['email'])
#tabela executivo
db.define_table('executivo',
                Field('nome', notnull=True),
                Field('email', notnull=True),
                format='%(nome)s')
#validadores tabela executivo
db.executivo.email.requires = IS_EMAIL(error_message=msg_erro['email'])
#tabela atendimento
db.define_table('atendimento',
                Field('nome', notnull=True),
                Field('email', notnull=True),
                format='%(nome)s')
#validadores tabela executivo
db.atendimento.email.requires = IS_EMAIL(error_message=msg_erro['email'])

#tabela de campanhas
db.define_table('campanha',
                Field('nome', notnull=True),
                Field('cliente', notnull=True),
                Field('agencia', 'reference agencia'),
                Field('executivo', 'reference executivo', notnull=True),
                Field('atendimento', 'reference atendimento', notnull=True),
                Field('data_inicio', 'date', notnull=True),
                Field('data_fim', 'date', notnull=True),
                Field('tipo', 'list:string'),
                Field('editorias', 'list:string'),
                Field('rede', 'list:string'),
                Field('pontos', 'list:reference ponto'),
                Field('arquivo', 'upload'),
                Field('observacoes', 'text'),
                format='%(nome)s %(data_inicio)s - %(data_fim)s'
                )

#validadores tabela campanha
db.campanha.nome.requires = not_empty
db.campanha.cliente.requires = not_empty
db.campanha.agencia.requires = IS_IN_DB(db, 'agencia.id', '%(nome)s - %(agencia)s', multiple=True, error_message=msg_erro['not_in_db'])
db.campanha.executivo.requires = IS_IN_DB(db, 'executivo.id', 'executivo.nome', error_message=msg_erro['not_in_db'])
db.campanha.atendimento.requires = IS_IN_DB(db, 'atendimento.id', 'atendimento.nome', error_message=msg_erro['not_in_db'])
db.campanha.data_inicio.requires = IS_DATE(format=T('%d/%m/%Y'), error_message='formato incorreto: dd/mm/yyyy')
db.campanha.data_fim.requires = IS_DATE(format=T('%d/%m/%Y'), error_message='formato incorreto: dd/mm/yyyy')
db.campanha.rede.requires = IS_IN_SET(redes, multiple=True, error_message=msg_erro['not_in_set'])
db.campanha.pontos.requires = IS_IN_DB(db, 'ponto.id', 'ponto.cod_player', multiple=True, error_message=msg_erro['not_in_db'])
db.campanha.tipo.requires = IS_IN_SET(tipo_campanha, error_message=msg_erro['not_in_set'])

#tabela ponto

db.define_table('ponto',
                Field('cod_rede', notnull=True),
                Field('cod_ponto', notnull=True),
                Field('cod_player', notnull=True),
                Field('segmento', notnull=True),
                Field('pais'),
                Field('estado'),
                Field('cidade'),
                Field('total_telas', 'integer'),
                format='%(cod_player)s'
                )
#validadores da tabela ponto
db.ponto.cod_rede.requires = not_empty
db.ponto.cod_ponto.requires = not_empty
db.ponto.cod_player.requires = not_empty
db.ponto.segmento.requires = not_empty
