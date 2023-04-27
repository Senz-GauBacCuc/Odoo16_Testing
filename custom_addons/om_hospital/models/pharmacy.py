from odoo import api, models, fields

class AppointmentPharmacyLines(models.Model):
    _name = "appointment.pharmacy.lines"
    _description = "Appointment Pharmacy Lines"

    product_id = fields.Many2one(comodel_name='product.product', required=True)
    price_unit = fields.Float(related='product_id.lst_price', string='Price per Unit')
    qty = fields.Integer(string='Quantity', tracking=True)
    price = fields.Float(string='Price', compute='_compute_price_on_qty')
    appointment_id = fields.Many2one(comodel_name='hospital.appointment', string='Appointment')

    @api.depends('qty')
    def _compute_price_on_qty(self):
        for rec in self:
            if rec.qty <= 0:
                rec.price = 0.0
            else:
                rec.price = rec.price_unit * rec.qty
