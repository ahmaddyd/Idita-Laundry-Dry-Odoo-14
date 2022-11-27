from odoo import api, fields, models


class Suppliernya(models.Model):
    _name = 'idita.supplier_laundry'
    _description = 'Supplier Bahan Laundry Idita'

    name = fields.Char(string='Supplier')
    alamat = fields.Char(string='Alamat')
    cp = fields.Char(string='Contact Person')
    telp = fields.Char(string='Nomor Telepon')
    bahanalat = fields.One2many(comodel_name='idita.bahan_laundry', inverse_name='suppliernya', string='Bahan Supply')
