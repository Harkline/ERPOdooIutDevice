# -*- coding: utf-8 -*-
{
    'name': "IutDeviceYL",

    'summary': """This is my summary""",

    'description': """
        This is my description:
            - loutre
            - phoque
            - a
    """,

    'author': "Yanis Levesque",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    # Ajouter les vues ici (.xml)
    'data': [
        # 'security/ir.model.access.csv',
        'views/iut_it_device_view.xml',

        # 'views/iut_it_brand_view.xml',
        # 'views/arborescence_menu_view.xml',
        # 'views/iut_it_model_view.xml',
        # 'views/iut_model_type_view.xml',
        # 'views/res_partner.xml'

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo.xml',
    ],
}
