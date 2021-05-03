from odoo import fields, models

class IutItBrand(models.Model):

    _name = "iut.it.brand"

    _python_sql_constraints_Unique_Key = [('name_uniq', 'unique (name)', 'name is a unique key, violation of constraint !')]

    name = fields.Char(string="Name", required=True)
    warrantyDelayMonth = fields.Integer(string="Warranty delay Month")
    supportPhone = fields.Integer(string="Phone support")

    #Permet de faire le lien BD 1...*              ids
    modelId = fields.One2many('iut.it.model', 'brandId');
