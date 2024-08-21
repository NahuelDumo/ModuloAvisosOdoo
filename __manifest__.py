{
    'name': 'Project Activity Alert',
    'version': '1.0',
    'summary': 'Alert users with pending project activities upon login',
    'author': 'Nahuel Dumo',
    'category': 'Project',
    'depends': ['base', 'project'],
    'data': [
        'views/model_definition.xml',  # Archivo donde defines el modelo
        'views/view.xml'               # Archivo donde defines el cron job
    ],
    'installable': True,
    'application': False,
}
