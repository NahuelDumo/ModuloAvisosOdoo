from odoo import models, fields, api

class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.model
    def check_pending_activities(self):
        user_id = self.env.uid
        tasks = self.env['project.task'].search([('user_id', '=', user_id), ('stage_id', '=', False)])
        pending_activities = len(tasks)
        
        if pending_activities > 0:
            message = f'Tienes {pending_activities} actividades pendientes. Por favor, revise las tareas asignadas.'
            self.env.user.notify_warning(message)
        else:
            message = 'No tienes actividades pendientes.'
            self.env.user.notify_info(message)
