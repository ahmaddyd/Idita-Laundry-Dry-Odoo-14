from odoo import api, fields, models
from odoo.exceptions import ValidationError


class PemesananLaundry(models.Model):
    _name = 'idita.pemesanan_laundry'
    _description = 'Pemesanan Laundry'

    name = fields.Many2one(comodel_name='idita.bahan_laundry', string='Nama Barang')

    supplier = fields.Char(compute='_compute_supplier', string='Supplier')

    @api.depends('name')
    def _compute_supplier(self):
        for record in self:
            record.supplier = record.name.suppliernya.name

    contact = fields.Char(compute='_compute_contact', string='No. Telp Supplier')

    @api.depends('name')
    def _compute_contact(self):
        for record in self:
            record.contact = record.name.suppliernya.telp

    tanggal_pesan = fields.Date(string='Tanggal Pesan', default=fields.Datetime.now)
    tanggal_masuk = fields.Char(compute='_compute_tanggal_masuk', string='Tanggal Barang Datang')

    @api.model
    def _compute_tanggal_masuk(self):
        for record in self:
            tgl = self.env['idita.barang_masuk_laundry'].search([('name', '=', record.id)]).mapped('tgl_datang')
            if tgl:
                record.tanggal_masuk = tgl[0]
                record.sudah_masuk = True
            else:
                record.tanggal_masuk = 0
                record.sudah_masuk = False

    jumlah_pesanan = fields.Integer(string='Jumlah Pemesanan')
    tagihan_supplier = fields.Float(compute='_compute_tagihan_supplier', string='Tagihan Supplier')

    @api.depends('jumlah_pesanan')
    def _compute_tagihan_supplier(self):
        for record in self:
            record.tagihan_supplier = record.name.harga * record.jumlah_pesanan

    masuk_akunting = fields.Boolean(string='Masuk Akunting')
    sudah_masuk = fields.Boolean(string='Barang Sudah Masuk')

    def masukakunting(self):
        for record in self:
            tgl = self.env['idita.barang_masuk_laundry'].search([('name', '=', record.id)]).mapped('tgl_datang')
            if tgl:
                record.masuk_akunting = True
                self.env['idita.laundry_akunting'].create({'debet': record.tagihan_supplier, 'name': record.name.name})
            else:
                raise ValidationError("Barang belum datang, tidak bisa masuk akunting")

    def keluarakunting(self):
        for record in self:
            record.masuk_akunting = False
            data = self.env['idita.laundry_akunting'].search([('name', '=', record.name.name)])
            data.unlink()
