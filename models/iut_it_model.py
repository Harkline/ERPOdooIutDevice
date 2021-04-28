from odoo import api, fields, models

class IutItModel():

    _name = ""
    _ref = ""
    _type_ids = ""

    name = fields.Char(required=True)
    ref = fields.Char(required=True)
    type_ids = fields.Integer()
