from odoo import fields, models


class product_cat(models.Model):
    _name = 'product.product_cat'
    name = fields.Char()
    product_ids = fields.One2many('product.product', 'product_cat_id')
    product_lot_ids = fields.One2many('g.product_lot', 'product_cat_id')
    product_ids = fields.One2many('product.product', 'product_cat_id')
