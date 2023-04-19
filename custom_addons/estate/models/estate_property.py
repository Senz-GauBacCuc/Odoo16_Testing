from odoo import fields, models

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Test module"

    name = fields.Char(string='Property Name',required=True)
    description = fields.Text(string='Description')
    postcode = fields.Char('Postcode',)
    date_availability = fields.Date('Date Availability')
    expected_price = fields.Float('Expected Price',required=True)
    selling_price = fields.Float('Selling Price')
    bedrooms = fields.Integer('Bedrooms large')
    living_area = fields.Integer('Living Area')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area')
    garden_orientation = fields.Selection(
        string= 'Type',
        selection= [('north','North'),
                    ('south','South'),
                    ('east','East'),
                    ('west','West')]
    )