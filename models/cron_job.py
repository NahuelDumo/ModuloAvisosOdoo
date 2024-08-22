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
            # Asegúrate de que el usuario tenga un partner_id
            if not user.partner_id:
                _logger.warning(f'El usuario {user.name} no tiene un partner_id asociado.')
                continue

            tasks = self.env['project.task'].search([
                ( 'user_ids, "in" ,'user.id ),  # Cambiado a user_id
            ])
            _logger.info(f'Usuario {user.name} tiene {len(tasks)} tareas pendientes.')

            if tasks:
                message = f'Tienes {len(tasks)} actividades pendientes.'
                _logger.info(f'Enviando notificación al usuario {user.name}: {message}')
                
                try:
                    # Enviar notificación al usuario a través del canal 'bus.bus'
                    self.env['bus.bus']._sendone(
                        (self._cr.dbname, 'res.partner', user.partner_id.id), 
                        {
                            'type': 'simple_notification',
                            'title': 'Actividades Pendientes',
                            'message': message,
                            'sticky': False,  # Cambia a True si quieres que la notificación se quede en pantalla
                        }
                    )
                except Exception as e:
                    _logger.error(f'Error al enviar notificación al usuario {user.name}: {e}')
            else:
                _logger.info(f'No hay tareas pendientes para el usuario {user.name}.')
        
        _logger.info('Finalizó la verificación de actividades pendientes.')