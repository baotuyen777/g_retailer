from odoo import fields, models, api


class users(models.Model):
    _inherit = 'res.users'
    agency_id = fields.Many2one('g.agency')
