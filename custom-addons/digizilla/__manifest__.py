# digizilla/__manifest__.py
{
    'name': 'Digizilla Module',
    'version': '1.0',
    'license': 'LGPL-3',
    'summary': 'Module for managing Digizilla records',
    'description': """
        A module to manage Digizilla records with Kanban, Form, and List views.
        Includes features like message logging, custom PDF reports, and UI enhancements.
    """,
    'author': 'Usama Alzomor',
    'website': 'https://digizilla.com',
    'category': 'Tools',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/digizilla_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
