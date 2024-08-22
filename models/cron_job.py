# file: models/cron_job.py
import logging
from odoo import models, fields

# Configura el logger
_logger = logging.getLogger(__name__)

class MyModuleCron(models.Model):
    _name = 'my.module.cron'

    def cron_check_pending_activities(self):
        _logger.info('Iniciando la verificación de actividades pendientes.')

        users = self.env['res.users'].search([])
        _logger.info(f'Número de usuarios encontrados: {len(users)}')

        for user in users:
            # Convertir el ID del usuario a una lista para el operador 'in'
            user_ids = [user.id]

            tasks = self.env['project.task'].search([
                ('user_ids', 'in', user_ids),
            ])
            _logger.info(f'Usuario {user.name} tiene {len(tasks)} tareas pendientes.')

            if tasks:
                message = f'Tienes {len(tasks)} actividades pendientes.'
                _logger.info(f'Enviando notificación al usuario {user.name}: {message}')
                user.notify_info(message)
            else:
                _logger.info(f'No hay tareas pendientes para el usuario {user.name}.')
        
        _logger.info('Finalizó la verificación de actividades pendientes.')
