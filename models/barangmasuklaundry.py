from odoo import api, fields, models


class BarangMasuk(models.Model):
    _name = 'idita.barang_masuk_laundry'
    _description = 'Kedatangan Barang dari Supplier'

    name = fields.Many2one(comodel_name='idita.pemesanan_laundry', string='Nama Barang',
                           domain="[('sudah_masuk','=',False)]")
    tgl_pesan = fields.Char(compute='_compute_tgl_pesan', string='Tanggal Pemesanan')

    @api.depends('name')
    def _compute_tgl_pesan(self):
        for record in self:
            record.tgl_pesan = record.name.tanggal_pesan

    tgl_datang = fields.Datetime(
        string='Tanggal Barang Datang',
        default=fields.Datetime.now())

    tagihan = fields.Float(compute='_compute_tagihan', string='Jumlah Tagihan')

    @api.depends('name')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.name.tagihan_supplier

    suppliernya = fields.Char(compute='_compute_suppliernya', string='Supplier')

    @api.depends('name')
    def _compute_suppliernya(self):
        for record in self:
            record.suppliernya = record.name.supplier
