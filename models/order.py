from odoo import api, fields, models
from odoo.exceptions import ValidationError


class OrderCuci(models.Model):
    _name = 'idita.laundry_order'
    _description = 'Orderan Laundry & Dry Idita'
    _order = 'id desc'

    name = fields.Many2one(comodel_name='res.partner', string='Customer', domain="[('is_customernya','=',True)]",
                           delegate=True)
    phone = fields.Char(compute='_compute_phone', string='Nomor Handphone')

    @api.depends('name')
    def _compute_phone(self):
        for record in self:
            record.phone = record.name.phone

    tanggal_pemesanan = fields.Datetime(default=fields.Datetime.now)
    tanggal_selesai = fields.Datetime(compute='_compute_tanggal', string='Tanggal Selesai')

    @api.model
    def _compute_tanggal(self):
        for record in self:
            tgl = self.env['idita.laundry_selesai'].search([('name', '=', record.id)]).mapped('tgl_selesai')
            if tgl:
                record.tanggal_selesai = tgl[0]
                record.selesai_cuci = True
            else:
                record.tanggal_selesai = 0
                record.selesai_cuci = False

    jumlah_pesanan = fields.Char(compute='_compute_jumlah_pesanan', string='Jumlah Pesanan')

    detailcucian_ids = fields.One2many(comodel_name='idita.laundry_detail', inverse_name='order_id',
                                       string='Detail Order')

    @api.depends('detailcucian_ids')
    def _compute_jumlah_pesanan(self):
        for record in self:
            record.jumlah_pesanan += len(record.detailcucian_ids)

    selesaicuci_ids = fields.One2many(
        comodel_name='idita.laundry_selesai', inverse_name='name', string='Penyelesaian Cucian')

    selesai_cuci = fields.Boolean(string='Sudah Selesai')

    masuk_akunting = fields.Boolean(string='Masuk Akunting')

    total_harga = fields.Integer(compute='_compute_total_harga', string='Total Harga')

    @api.model
    def _compute_total_harga(self):
        for record in self:
            total = sum(
                self.env['idita.laundry_detail'].search([('order_id', '=', record.id)]).mapped('jumlah_harga'))
            record.total_harga = total

    def confirm(self):
        for record in self:
            if record.tanggal_selesai:
                record.masuk_akunting = True
                self.env['idita.laundry_akunting'].create(
                    {'kredit': record.total_harga, 'name': record.name.display_name})
            else:
                raise ValidationError("Yang belum selesai dicuci tidak bisa masuk")

    def cancel(self):
        for record in self:
            record.masuk_akunting = False
            data = self.env['idita.laundry_akunting'].search([('name', '=', record.name.display_name)])
            data.unlink()


class DetailCucian(models.Model):
    _name = 'idita.laundry_detail'
    _description = 'Detail Laundry & Dry Idita'

    name = fields.Char(string='Kode Order')
    order_id = fields.Many2one(comodel_name='idita.laundry_order', string='Order Id')
    jenis = fields.Many2one(comodel_name='idita.jenis_laundry', string='Bahan Cucian')
    harga = fields.Integer(compute='_compute_harga', string='Harga per Kg')

    @api.depends('jenis')
    def _compute_harga(self):
        for record in self:
            record.harga = record.jenis.harga

    berat = fields.Integer(string='Berat Cucian')

    @api.depends('berat')
    def _compute_field_name(self):
        for record in self:
            record.jumlah_harga = record.berat * record.harga

    jumlah_harga = fields.Integer(compute='_compute_field_name', string='Jumlah Harga')
