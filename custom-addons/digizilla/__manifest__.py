{
    'name': 'Digizilla',
    'version': '1.0',
    'author': 'Your Name',
    'category': 'Custom',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/digizilla_views.xml',
        'reports/digizilla_report.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'digizilla/static/src/js/hide_create_button.js',
        ],
    },
    'installable': True,
    'application': True,
}
