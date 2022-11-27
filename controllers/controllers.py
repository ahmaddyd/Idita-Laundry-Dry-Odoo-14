from odoo import http, models, fields
from odoo.http import request
import json


class Iditalaundry(http.Controller):
    @http.route('/bahanlaundry', auth='public')
    def get_models(self, **kwargs):
        order = request.env['idita.jenis_laundry'].search([])
        value = []
        for ord in order:
            value.append({
                'nama': ord.name,
                'size': ord.size,
                'type': ord.type
            })
        return json.dumps(value)

    @http.route('/tekniklaundry', auth='public')
    def get_laundryteknik(self, **kwargs):
        laundryteknik = request.env['idita.laundry_teknik'].search([])
        value = []
        for ab in laundryteknik:
            value.append({
                'nama': ab.name,
                'tingkat_kotor': ab.tingkat_kotor,
                'metode_laundry': ab.metode_laundry,
                'harga_per_kg': ab.harga
            })
        return json.dumps(value)

    @http.route('/akunting', auth='public')
    def get_akunting(self, **kwargs):
        akunting = request.env['idita.laundry_akunting'].search([])
        value = []
        for ak in akunting:
            value.append({
                'nama': ak.name,
                'tanggal': str(ak.date),
                'debet': ak.debet,
                'kredit': ak.kredit,
                'saldo': ak.saldo
            })
        return json.dumps(value)
