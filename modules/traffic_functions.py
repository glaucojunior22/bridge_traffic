# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

from gluon.html import *

def build_carousel_item(db_element, len_list):
	'''
	return an item for bootstrap carousel
	'''
	cl = "item" if len_list else "item active"
	carousel_item = DIV(
						IMG(_src=URL('default','download',args=db_element.t_photos['f_photo']),_style="width:100%;height:auto;"),
						DIV(
								H4(XML("<span style='font-style:italic'>%s</span>&nbsp;&nbsp;-&nbsp;%s"%(db_element.t_photos['f_title'],db_element.t_trip['f_trip_in']))),
								P(db_element.t_trip['f_trip_description']),
							**{'_class':"carousel-caption"}),
						_class=cl)
	return carousel_item

def bootstrap_form(w2p_form,not_show_action_buttons=True):
	form = w2p_form
	components = form.components[0][:] if not_show_action_buttons else form.components[0][:-1] 
	if isinstance(form,FORM):
		form['_class'] = 'form-horizontal well'
		i = -1
		for component in components:
			i += 1
			ctrl_label = form.components[0][i][0][0] # label
			ctrl_input = form.components[0][i][1][0] # input
			ctrl_label['_class'] = "control-label"
			ctrl_wrapper = DIV(ctrl_label,DIV(ctrl_input,_class="controls"),_class="control-group")
			form.components[0][i] = ctrl_wrapper
		if not_show_action_buttons == False:
			form.components[0][-1] = XML('<div class="form-actions"><button type="submit" class="btn btn-primary">Submit</button>&nbsp;<button type="reset" class="btn">Cancel</button></div>')
	return form