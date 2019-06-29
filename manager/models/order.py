from odoo import fields,models,api
class order(models.Model):
    _name = 'g.order'
    product_ids = fields.One2many('product.product','order_id')
    customer_id = fields.Many2one('res.users')