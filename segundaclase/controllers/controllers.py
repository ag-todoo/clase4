# -*- coding: utf-8 -*-
# from odoo import http


# class Segundaclase(http.Controller):
#     @http.route('/segundaclase/segundaclase/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/segundaclase/segundaclase/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('segundaclase.listing', {
#             'root': '/segundaclase/segundaclase',
#             'objects': http.request.env['segundaclase.segundaclase'].search([]),
#         })

#     @http.route('/segundaclase/segundaclase/objects/<model("segundaclase.segundaclase"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('segundaclase.object', {
#             'object': obj
#         })
