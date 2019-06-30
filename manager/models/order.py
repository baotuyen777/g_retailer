from odoo import fields,models,api
class order(models.Model):
    _name = 'g.order'
    product_ids = fields.One2many('product.product','order_id')
    customer_id = fields.Many2one('res.users')
    state = fields.Selection(string='state',selection=[('khoitao','khoi tao'),('cholayhang','cho lay hang'),('dagiaohang','da giaohang'),
                                                    ('dathutien','da thu tien'),('hoanthanh','hoan thanh')],default='khoitao')

