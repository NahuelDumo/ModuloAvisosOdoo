from odoo import models, fields, api
import logging
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class ProjectActivityAlert(models.Model):
    _inherit = 'res.users'

    @api.model
    def check_pending_activities(self):
        try:
            user = self.env.user
            pending_activities = self.env['project.task'].search([
                ('user_id', '=', user.id),
                ('stage_id.fold', '=', False),
                ('date_deadline', '<=', fields.Date.today()),
            ])

            if pending_activities:
                # Mostrar notificación al usuario
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': 'Actividades Pendientes',
                        'message': f'Tienes {len(pending_activities)} actividades pendientes en el proyecto.\n Por favor revisalas.',
                        'sticky': False,
                    }
                }
        except Exception as e:
            _logger.error("Error checking pending activities for user %s: %s", self.env.user.id, str(e))
            raise UserError(_('Ha ocurrido un error al verificar las actividades pendientes: %s') % str(e))

    @api.model
    def _check_user_activities(self):
        try:
            users = self.env['res.users'].search([])
            for user in users:
                # Reconfiguramos el entorno para el usuario actual
                self = user
                self.check_pending_activities()
        except Exception as e:
            _logger.error("Error during scheduled activity check: %s", str(e))
            # Opcional: Puedes registrar un mensaje de error más general o específico
