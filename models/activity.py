import logging
from odoo import models, api

# Crear un logger
_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    def check_credentials(self, password):
        """Sobreescribimos el método check_credentials para ejecutar la acción después de la autenticación"""
        _logger.info("Ejecutando check_credentials para el usuario: %s", self.name)
        super(ResUsers, self).check_credentials(password)
        _logger.info("Autenticación completada para el usuario: %s", self.name)
        self.check_pending_activities()

    def check_pending_activities(self):
        _logger.info("Verificando actividades pendientes para el usuario: %s", self.name)
        tasks = self.env['project.task'].search([
            ('user_id', '=', self.env.uid),
            ('stage_id', '=', False)
        ])
        _logger.info("Número de tareas pendientes encontradas: %s", len(tasks))
        if tasks:
            message = f'Tienes {len(tasks)} actividades pendientes.'
            _logger.info("Notificando al usuario: %s con el mensaje: %s", self.name, message)
            self.notify_info(message)
        else:
            _logger.info("No se encontraron actividades pendientes para el usuario: %s", self.name)
