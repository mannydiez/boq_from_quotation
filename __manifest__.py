# -*- coding: utf-8 -*-

{
    'name': 'BOQ from Quotation',
    'version': '0.1',
    'category': 'Sales/Accounting',
    'summary': 'Change Quotation name into Bill of Quantity',
    'description': """Change Quotation name into Bill of Quantity""",
    'website':"www.hashmicro.com",
    'author': 'HashMicro / Emmanuel Diez',
    'depends': ['job_costing_management_extension'],
    'data': [
        'views/boq.xml',
    ],    
    'installable': True,
    'application': False,
    
}