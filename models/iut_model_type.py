from odoo import api, fields, models

class IutItModeleType():

    _name = ""
    _model_ids = ""

    name = fields.Char(required=True)
    modelIds = fields.Integer()