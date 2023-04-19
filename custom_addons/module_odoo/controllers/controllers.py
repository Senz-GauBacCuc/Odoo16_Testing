# -*- coding: utf-8 -*-
# from odoo import http


# class ModuleOdoo(http.Controller):
#     @http.route('/module_odoo/module_odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/module_odoo/module_odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('module_odoo.listing', {
#             'root': '/module_odoo/module_odoo',
#             'objects': http.request.env['module_odoo.module_odoo'].search([]),
#         })

#     @http.route('/module_odoo/module_odoo/objects/<model("module_odoo.module_odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('module_odoo.object', {
#             'object': obj
#         })
