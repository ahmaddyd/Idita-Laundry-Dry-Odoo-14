from odoo import api, fields, models


class LaundrySelesai(models.Model):
    _name = 'idita.laundry_selesai'
    _description = 'Laundry Selesai'

    name = fields.Many2one(comodel_name='idita.laundry_order', string='Customer',
                           domain="[('selesai_cuci','=',False)]", )
    tanggal_pemesanan = fields.Char(compute='_compute_tanggal_pemesanan', string='Tanggal Pemesanan')

    @api.depends('name')
    def _compute_tanggal_pemesanan(self):
        for record in self:
            record.tanggal_pemesanan = record.name.tanggal_pemesanan

    tanggal_selesai = fields.Datetime(string='Tanggal Selesai',default=fields.Datetime.now())

    tagihan = fields.Integer(compute='_compute_tagihan',string='Total Pembayaran',store=True)

    @api.depends('name')
    def _compute_tagihan(self):
        for record in self:
            record.tagihan = record.name.total_harga
