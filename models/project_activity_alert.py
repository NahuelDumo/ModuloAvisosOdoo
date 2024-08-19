from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class ResUsers(models.Model):
    _inherit = 'res.users'

    pending_activities_message = fields.Char(
        compute='_compute_pending_activities_message',
        store=False
    )

    @api.depends('id')
    def _compute_pending_activities_message(self):
        for user in self:
            pending_activities = self.env['project.task'].search([
                ('user_id', '=', user.id),
                ('stage_id.fold', '=', False),
                ('date_deadline', '<=', fields.Date.today()),
            ])

            if pending_activities:
                user.pending_activities_message = f'Tienes {len(pending_activities)} actividades pendientes en el proyecto.\nPor favor revísalas.'
                _logger.info(f"Usuario {user.name}: {user.pending_activities_message}")
            else:
                user.pending_activities_message = ''

