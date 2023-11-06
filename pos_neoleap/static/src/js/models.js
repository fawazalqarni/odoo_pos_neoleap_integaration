odoo.define('pos_neoleap.models', function (require) {

var models = require('point_of_sale.models');
var PaymentNeoleap = require('pos_neoleap.payment');

models.register_payment_method('neoleap', PaymentNeoleap);
});
