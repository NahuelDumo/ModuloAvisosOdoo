from odoo import models, fields, api, _
import logging
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)

class ProjectActivityAlert(models.Model):
    _inherit = 'res.users'

    def check_pending_activities(self):
        user = self.env.user
        try:
            pending_activities = self.env['project.task'].search([
                ('user_id', '=', user.id),
                ('stage_id.fold', '=', False),
                ('date_deadline', '<=', fields.Date.today()),
            ])

            if pending_activities:
                return {
                    'type': 'ir.actions.client',
                    'tag': 'display_notification',
                    'params': {
                        'title': _('Actividades Pendientes'),
                        'message': _('Tienes %s actividades pendientes en el proyecto.\n Por favor revisalas.') % len(pending_activities),
                        'sticky': False,
                    }
                }
        except Exception as e:
            _logger.error("Error checking pending activities for user %s: %s", user.id, str(e))
            raise UserError(_('Ha ocurrido un error al verificar las actividades pendientes: %s') % str(e))

    @api.model
    def _check_user_activities(self):
        try:
            users = self.env['res.users'].search([])
            for user in users:
                self.with_user(user).check_pending_activities()
        except Exception as e:
            _logger.error("Error during scheduled activity check: %s", str(e))
