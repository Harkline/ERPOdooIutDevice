from odoo import api, fields, models

class IutItBrand():

    _name = ""
    _warranty_delay_month = ""
    _support_phone = ""

    name = fields.Char(required=True)
    warrantyDelayMonth = fields.Integer()
    supportPhone = fields.Integer()
