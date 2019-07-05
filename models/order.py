# -*- coding: utf-8 -*-
from odoo import fields, models,api
from openerp.exceptions import except_orm, Warning, RedirectWarning


class order(models.Model):
    _name = 'g.order'
    product_ids = fields.One2many('product.product', 'order_id')
    code = fields.Char()
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
        if self.state == 'create':
            self.state = 'pending'
        else :
            raise Warning("loi qui trinh")
# da thu tien va hoan thanh,thi khong the huy
    def cancel(self):
        if self.state in ['paid','completed'] :
            raise Warning('khong the xoa')
        return models.Model.unlink(self)
# neu khong co hang,thi khong cho giao hang
    def delivering(self):
        k = 0
        for x in self :
            if x.product_ids :
                k = 1
        if self.state == 'pending' and k == 1:
            self.state = 'delivering'
        else :
            raise Warning("loi qui trinh")

# giao hang xong thi moi thu tien
    def paid(self):
        if self.state == 'delivering':
            self.state = 'paid'
        else :
            raise Warning("loi qui trinh")

# thu tien xong thi moi duoc hoan thanh
    def completed(self):
        if self.state == 'paid':
            self.state = 'completed'
        else :
            raise Warning("loi qui trinh")

