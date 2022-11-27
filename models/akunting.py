from odoo import api, fields, models


class Akunting(models.Model):
    _name = 'idita.laundry_akunting'
    _description = 'Akunting'
    _order = 'id asc'

    name = fields.Char(string='Nama', required=True)
    id_akunting = fields.Char(string='Kode Akunting')
    tanggal = fields.Datetime(string='Tanggal', default=fields.Datetime.now(), required=False)
    debet = fields.Integer(string='Debet', required=False)
    kredit = fields.Integer(string='Kredit', required=False)
    saldo = fields.Float(compute='_compute_saldo', string='Saldo')

    @api.depends('debet', 'kredit')
    def _compute_saldo(self):
        for record in self:
            prev = self.search_read([('id', '<', record.id)], limit=1, order='date desc')
            prev_saldo = prev[0]['saldo'] if prev else 0
            record.saldo = prev_saldo + record.kredit - record.debet

    @api.model
    def compute_id_akunting(self):
        for record in self.search([('id_akunting', '=', False)]):
            record.id_akunting = 'AK' + str(record.id)
