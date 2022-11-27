# -*- coding: utf-8 -*-
# from odoo import http


# class IditaLaundry(http.Controller):
#     @http.route('/idita_laundry/idita_laundry/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/idita_laundry/idita_laundry/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('idita_laundry.listing', {
#             'root': '/idita_laundry/idita_laundry',
#             'objects': http.request.env['idita_laundry.idita_laundry'].search([]),
#         })

#     @http.route('/idita_laundry/idita_laundry/objects/<model("idita_laundry.idita_laundry"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('idita_laundry.object', {
#             'object': obj
#         })
