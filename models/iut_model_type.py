from odoo import fields, models

class IutItModelType(models.Model):

    _name = "iut.model.type"

    _python_sql_constraints_Unique_Key = [('name_uniq', 'unique (name)', 'name is a unique key, violation of constraint !')]

    name = fields.Char(string="name", required=True)

    # Permet de faire le lien BD *...*, ici avec la classe model
    modelIds = fields.Many2many('iut.it.model')