from odoo import fields, models, api


class policy(models.Model):
    _name = 'g.policy'
    product_ids = fields.Many2many('product.product')
    customer_ids = fields.Many2many('res.users')
    product_lot_ids = fields.Many2many('g.product_lot', 'policy_id')
