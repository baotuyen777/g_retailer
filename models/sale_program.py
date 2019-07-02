from odoo import fields, models


class sale_program(models.Model):
    _name = 'g.sale_program'
    customer_ids = fields.Many2many('res.users')
