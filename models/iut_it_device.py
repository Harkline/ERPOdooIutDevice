from odoo import api, fields, models

class IutItDevice(models.Model()): #
    _name = "IutItDevice"
    _dateAllocation="DateAllocation"
    _serialNumber="SerialNumber"
    _datePurchase="DatePurchase"
    _dateWarrantyEnd="DateWarrantyEnd"

    name = fields.Char(string='Iut_device', required=True)
    dateAllocation = fields.Date(string='allocation_date')
    serialNumber = fields.Char(string='serial_number', required=True)
    datePurchase = fields.Date(string='date_purchase')
    dateWarrantyEnd = fields.Date(string='Date_Warranty_end')