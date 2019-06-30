from odoo import fields,models,api
class product_lot(models.Model):
    _name = 'g.product_lot'
    product_ids = fields.Many2many('product.product')
    policy_id = fields.Many2one('g.policy')
