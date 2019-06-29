from odoo import fields,models,api
class policy(models.Model):
    _name = 'g.policy'
    product_ids = fields.Many2many('product.product')
    customer_ids =fields.Many2many('res.users')
    

