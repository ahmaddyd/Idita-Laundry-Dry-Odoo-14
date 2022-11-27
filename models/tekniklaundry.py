# -*- coding: utf-8 -*-
from odoo import models, fields


class LaundryTeknik(models.Model):
    _name = 'idita.laundry_teknik'
    _description = 'List Tekni Pencucian'

    name = fields.Selection(string='Nama Teknik',
                            selection=[('light A', 'Light A'), ('light B', 'Light B'), ('medium A', 'Medium A'),
                                       ('medium B', 'Medium B'), ('heavy A', 'Heavy A'), ('heavy B', 'Heavy B'),
                                       ('Super', 'Super')])

    metode_laundry = fields.Selection(string='Jenis Teknik Laundry',
                                      selection=[('laundry kiloan', 'Laundry Kiloan'), ('dry cleaning', 'Dry Cleaning'),
                                                 ('laundry express', 'Laundry Express'),
                                                 ('laundry super wangi', 'Laundry Super Wangi')],
                                      required=True)

    harga = fields.Integer(string='Harga Laundry', required=True)

    tingkat_kotor = fields.Selection(string='Tingkat Kotoran',
                                     selection=[('ringan', 'Ringan'), ('sedang', 'Sedang'), ('berat', 'Berat')],
                                     required=True)

    available = fields.Boolean(string='Tersedia', default=True)

    teknikpencucian = fields.Char(string='Deskripsi Teknik Pencucian',
                                  help='isi dengan alat yang digunakan untuk mencuci')

    models_ids = fields.One2many(comodel_name='idita.jenis_laundry', inverse_name='teknik_id', string='Jenis Cucian')

    pegawai_id = fields.Many2one(comodel_name='res.partner', string='MANAGER', domain="[('is_pegawainya','=',True)]")
