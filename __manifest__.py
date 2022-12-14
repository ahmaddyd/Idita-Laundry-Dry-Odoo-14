# -*- coding: utf-8 -*-
{
    'name': "IDITA LAUNDRY",

    'summary': """
        Sistem Aplikasi ERP pencucian baju idita""",

    'description': """
        Sistem Aplikasi ERP pencucian baju idita
    """,

    'author': "Ahmad Yulian Dinata",
    'website': "https://www.linkedin.com/in/ahmaddyd/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Productivity',
    'version': '0.1',
    'application': True,

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/jenis_laundry_views.xml',
        'views/teknik_laundry_views.xml',
        'views/order_views.xml',
        'views/laundry_contact_views.xml',
        'views/laundry_contact_pegawai_views.xml',
        'views/bahan_laundry_views.xml',
        'views/supplier_laundry_views.xml',
        'views/laundry_selesai_views.xml',
        'views/akunting_views.xml',
        'views/pemesanan_laundry_views.xml',
        'views/barang_masuk_laundry_views.xml',
        'report/report.xml',
        'report/laundry_order_report.xml',
        'views/views.xml',
        'views/templates.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
