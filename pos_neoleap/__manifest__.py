# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'POS Neoleap',
    'version': '1.6',
    'category': 'Sales/Point Of Sale',
    'sequence': 6,
    'summary': 'Integrate your POS with a Neoleap payment terminal',
    'author': "Khaled Said (kerbrose => hotmail)",
    'website': "https://kerbrose.github.io/",
    'data': [
        'views/pos_payment_method_views.xml',
        'views/pos_order.xml',
    ],
    'depends': [
        'point_of_sale',
        'ob_pos_payment_reference',
    ],
    'installable': True,
    'license': 'LGPL-3',
    'assets': {
        'point_of_sale.assets': [
            'pos_neoleap/static/src/js/PaymentScreen.js',
            'pos_neoleap/static/src/js/Chrome.js',
            'pos_neoleap/static/src/js/payment_neoleap.js',
            'pos_neoleap/static/src/js/models.js',
            'pos_neoleap/static/src/xml/PaymentScreen.xml',
            'pos_neoleap/static/src/scss/pos.scss',
        ],
    }
}
