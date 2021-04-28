from odoo import fields, models

#models.Model()
class IutItDevice(models.Model):
    _name = "iut.it.device"

    name = fields.Char(string='Iut_device', required=True)
    dateAllocation = fields.Date(string='allocation_date')
    serialNumber = fields.Char(string='serial_number', required=True)
    datePurchase = fields.Date(string='date_purchase')
    dateWarrantyEnd = fields.Date(string='Date_Warranty_end')

    # Permet de faire le lien BD *...1
    modelId = fields.Many2one('iut.it.model')
    #partnerId = fields.Many2one('res.partner')