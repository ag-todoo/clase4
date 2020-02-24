# -*- coding: utf-8 -*-
#BY: ING.LUIS FELIPE PATERNINA VITAL - TODOO SAS.

from odoo import fields,models,api
import re
from odoo.exceptions import ValidationError




class Todoo(models.Model):
    _inherit = 'project.task'
    
    name1 = fields.Char(string="Primer Apellido")
    name2 = fields.Char(string="Segundo Apellido")
    name3 = fields.Char(string="Primer Nombre")
    name4 = fields.Char(string="Segundo Nombre")
    
    compania=fields.Many2one('res.partner')
    con1=fields.Char(string="Contacto 1")
    correo1=fields.Char(string="Correo del Contacto 1")
    
    incot=fields.Many2one('account.incoterms')

    age=fields.Selection([('Si', 'Si'),('No', 'No')])
    city=fields.Char(string="Ciudad")

    seg=fields.Selection([('Si', 'Si'),('No', 'No')])
    valor=fields.Char(string="Valor Asegurado")

    tipo=fields.Selection([('Si', 'Si'),('No', 'No')])
    Tipoa=fields.Selection([('Simple', 'Simple'),('Deposito Habilitado', 'Deposito Habilitado'),('Deposito Franco', 'Deposito Franco')])