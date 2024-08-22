{
    'name': 'Project Activity Alert',
    'version': '1.0',
    'summary': 'Alert users with pending project activities upon login',
    'author': 'Nahuel Dumo',
    'category': 'Project',
    'depends': ['base', 'project'],
    'data': [
        'views/model_definition.xml',  # Definición del modelo
        'views/view.xml',               # Definición del cron job
    ],
    'installable': True,
    'application': False,
}
