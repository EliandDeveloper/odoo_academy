# -*- coding: utf-8 -*-

from odoo import models, fields, api


class academy(models.Model):
     _name = 'academy.task'
     _description = 'academy.task'

     name = fields.Char()
     last_name = fields.Char()
     age = fields.Integer()
     enrollment_date = fields.Date()
     calification = fields.Selection([
          ('A', 'A'),
          ('B', 'B'),
          ('C', 'C'),
          ('F', 'F'),
     ], string='Calification')
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
