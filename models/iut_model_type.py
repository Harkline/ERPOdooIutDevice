from odoo import api, fields, models

class IutItModeleType():

    _name = "iut.it.model"

    name = fields.Char(string="name", required=True)

    # Permet de faire le lien BD *...*, ici avec la classe model
    modelIds = fields.Many2many('iut.it.model')