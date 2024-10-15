# simple_module/__manifest__.py
{
    'name': 'Simple Module',
    'version': '1.0',
    'summary': 'A simple Odoo module with a basic model',
    'description': """
        This is a simple Odoo module that introduces a basic model named 'Simple Model'.
    """,
    'author': 'Usama Alzomor',
    'website': 'https://yourwebsite.com',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/simple_model_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
