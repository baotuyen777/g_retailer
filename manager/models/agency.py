from odoo import fields,models,api
class agency(models.Model):
    _name = 'g.agency'
    name = fields.Char('name')
    admin_id = fields.Many2one('res.users')
    customer_ids = fields.One2many('res.users','agency_id')
    sale_program_id = fields.Many2one('g.sale_program')
    policy_id = fields.Many2one('g.policy')
