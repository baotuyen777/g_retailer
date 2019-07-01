from odoo import fields,models,api
class product_lot(models.Model):
    _name = 'g.product_lot'
    product_ids = fields.Many2many('product.product')
    policy_ids = fields.Many2many('g.policy')
    product_cat_id = fields.Many2one('product.product_cat')
