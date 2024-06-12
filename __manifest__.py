# -*- coding: utf-8 -*-
{
    'name': "rebound_technology",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'crm'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/footer.xml',
        'data/rebound_home.xml',
        'data/technology.xml',
        'data/sustainability.xml',
        'data/team.xml',
        'data/news.xml',
        'data/contact_us.xml',
        'data/sub_news.xml',
        'views/rebound_news_form.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
