from odoo import api, fields, models


class BahanLaundry(models.Model):
    _name = 'idita.bahan_laundry'
    _description = 'Bahan Laundry'

    name = fields.Char(string='Name')
    harga = fields.Integer(string='Harga Satuan')
    unit = fields.Char(string='Unit Pengguna')
    stok = fields.Integer(string='Stok')
    suppliernya = fields.Many2one(
        comodel_name='idita.supplier_laundry',
        string='Supplier')
    telp = fields.Char(compute='_compute_telp', string='No.Telepon')

    @api.depends('suppliernya')
    def _compute_telp(self):
        for record in self:
            record.telp = record.suppliernya.telp
