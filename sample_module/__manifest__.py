
{
    'name': 'sample_module',
    'version': '18.0.0.0',
    'summary': 'madre mia',
    'description': """ This Module for training purposes.
    """,
    'category':'Training',
    'author': 'Nagabhushan',
    'website': 'www.zbeanztech.com',
    "license": "LGPL-3",
    'depends': ['base','sale','sale_management','account','contacts'],
    'data': [
				'security/security.xml', # Always keep security fiels @ top
                'security/ir.model.access.csv', # Always keep security fiels @ top
				'views/model_one_view.xml',
                'views/food.xml',
				'views/menu.xml',
                'views/car_rental.xml'
				
        ],
    'test': [],
    'demo': [],
    'installable': True,
    'auto_install': False,
    'application': False,
}
