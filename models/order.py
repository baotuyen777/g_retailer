# -*- coding: utf-8 -*-
from odoo import fields, models


class order(models.Model):
    _name = 'g.order'
    product_ids = fields.One2many('product.product', 'order_id')
    customer_id = fields.Many2one('res.users','Khách hàng')
    state = fields.Selection(selection=[
        ('create', 'Khởi tạo'),
        ('pending', 'Chờ lấy hàng'),
        ('cancel', 'Hủy'),
        ('delivering', 'Đang giao hàng'),
        ('paid', 'Đã thu tiền'),
        ('completed', 'Hoàn thành')
    ], default='create',string='Trạng thái')

    def pending(self):
        self.state='pending'