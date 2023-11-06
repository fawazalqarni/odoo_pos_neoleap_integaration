from odoo import models, fields, api


class PosPayment(models.Model):
    _inherit = 'pos.payment'

    @api.model_create_multi
    def create(self, vals_list):
        for pos_payment in vals_list:
            if 'payment_reference' in pos_payment:
                pos_payment['ticket'] = pos_payment['payment_reference']
        return super(PosPayment, self).create(vals_list)
