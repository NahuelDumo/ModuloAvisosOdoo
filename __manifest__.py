{
    'name': 'Project Activity Alert',
    'version': '1.0',
    'summary': 'Alert users with pending project activities upon login',
    'author': 'Nahuel Dumo',
    'category': 'Tools',
    'depends': ['base', 'web', 'project'],
    'data': [
        'views/task_notification_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}   
