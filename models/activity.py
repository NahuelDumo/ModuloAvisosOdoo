import logging

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    def check_pending_activities(self):
        _logger.info('Verificando tareas pendientes para el usuario: %s', self.name)
        tasks = self.env['project.task'].search([
            ('user_id', '=', self.env.uid),
            ('stage_id', '=', False)
        ])
        if tasks:
            message = f'Tienes {len(tasks)} actividades pendientes.'
            self.notify_info(message)
            _logger.info('Usuario %s tiene %s tareas pendientes.', self.name, len(tasks))
        else:
            _logger.info('Usuario %s no tiene tareas pendientes.', self.name)
