# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class ModelDasar(models.Model):
    _name = "idita.model_laundry"
    _description = "Tipe Pakaian Pencucian IDITA"

    size = fields.Char(string='Ukuran Bahan', required=True, )
    tipe = fields.Selection(string='Tipe atau Jenis Bahan',
                            selection=[('katun', 'Katun'), ('denim', 'Denim'), ('kulit', 'Kulit'),
                                       ('canvas', 'Canvas')])


class IditaLaundry(models.Model):
    _name = 'idita.jenis_laundry'
    _description = 'Daftar Jenis Laundry IDITA'
    _inherit = 'idita.model_laundry'

    name = fields.Char(string='Jenis Cucian', required=True)
    active = fields.Boolean(default=True)
    deskripsi = fields.Char(string='Deskripsi')
    teknik_id = fields.Many2one(comodel_name='idita.laundry_teknik', string='Teknik Pencucian', required=True, delegate=True)
    teknik_pencucian = fields.Char(compute='_compute_teknik_pencucian', string='Teknik Pencucian')

    @api.depends('teknik_id')
    def _compute_teknik_pencucian(self):
        for record in self:
            record.teknik_pencucian = record.teknik_id.teknikpencucian

    @api.onchange('tipe')
    def _onchange_field_name(self):
        if self.tipe == 'katun':
            return {
                'warning': {
                    'title': "Teknik Pencucian",
                    'message': "Rubah teknik pencucian ke golongan B"
                },
            }
        elif self.tipe == 'kulit':
            return {
                'warning': {
                    'title': "Teknik Pencucian",
                    'message': "Rubah teknik pencucian ke golongan A"
                }
            }

    @api.constrains('name')
    def _check_name(self):
        for record in self:
            bahan = self.env['idita.jenis_laundry'].search([('name', '=', record.name), ('id', '!=', record.id)])
            if bahan:
                raise ValidationError("Bahan %s sudah ada" % record.name)
