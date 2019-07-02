# -*- coding: utf-8 -*-
from odoo import fields, models


class agency(models.Model):
    _name = 'g.agency'
    name = fields.Char('Tên chi nhánh')
    admin_id = fields.Many2one('res.users', 'Quản lý')
    customer_ids = fields.One2many('res.users', 'agency_id', 'Khách hàng')
    sale_program_id = fields.Many2one('g.sale_program', 'Chương trình')
    policy_id = fields.Many2many('g.policy', string='Chính sách')
