from odoo import fields,models,api
class product(models.Model):
    _inherit = 'product.product'
    image = fields.Binary()
    name = fields.Char()
    policy_ids = fields.Many2many('g.policy')
    order_id = fields.Many2one('g.order')
    product_lot_ids = fields.Many2many('g.product_lot')

