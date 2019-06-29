from odoo import fields,models,api
class customer(models.Model):
    _inherit = 'res.users'
    agency_id = fields.Many2one('g.agency')