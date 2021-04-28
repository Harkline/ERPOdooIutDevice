from odoo import api, fields, models

class IutItModel():

    _name = "iut.it.model"

    #Rajouter la constrainte sql de clef unique sur un champ
    _python_sql_constraints_Unique_Key = [('ref_uniq', 'unique (ref)', 'ref is a unique key, violation of constraint !')]


    name = fields.Char(string='name', required=True)
    ref = fields.Char(string='ref')

    #Permet de faire le lien BD *...* ou *...1 ou 1..*
    typeIds = fields.Many2many('iut.model.type')
    brandId = fields.Many2one('iut.it.brand')
    deviceId = fields.One2many('iut.it.device', 'iut_it_device.IutItDevice.modelId')

