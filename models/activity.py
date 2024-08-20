from odoo import models, fields, api

class ActivityReminder(models.Model):
    _name = 'moduloavisosodoo.activity_reminder'  # ejemplo válido

    _description = 'Activity Reminder'

    message = fields.Char(string='Reminder Message', compute='_compute_reminder_message')

    @api.model
    def get_pending_activities(self):
        # Obtener las tareas pendientes del usuario actual
        tasks = self.env['project.task'].search([('user_id', '=', self.env.uid), ('stage_id', '=', False)])
        return len(tasks)

    @api.model
    def get_reminder_message(self):
        pending_activities = self.get_pending_activities()
        if pending_activities > 0:
            return f'Tienes {pending_activities} actividades pendientes. Por favor, revise las tareas asignadas.'
        else:
            return ''

    @api.model
    def get_reminder_color(self):
        pending_activities = self.get_pending_activities()
        if pending_activities > 0:
            return 'danger'  # Rojo
        else:
            return 'success'  # Verde