# -*- coding: utf-8 -*-

from odoo import models, fields


class Player(models.Model):
    _name = 'player'
    _description = 'Player'

    name = fields.Char(string='PlayerName', required=True)
    image = fields.Binary(string='PlayerImage', attachment=True)
    country = fields.Char(string='PlayerCountry')
    gender = fields.Selection([('male', 'Male'),
                               ('female', 'Female')],
                              string='Gender', default='male')
    birthday = fields.Datetime(string='Day_of_Birth')
    position = fields.Char(string='Position')
    height = fields.Float(string='Height')
    weight = fields.Float(string='Weight')
