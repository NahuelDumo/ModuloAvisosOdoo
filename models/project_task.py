from odoo import models, fields, api
from datetime import timedelta, datetime

class ProjectTask(models.Model):
    _inherit = 'project.task'

    is_due_soon = fields.Boolean(compute='_compute_is_due_soon')

    @api.depends('date_deadline')
    def _compute_is_due_soon(self):
        for task in self:
            if task.date_deadline:
                # Si la tarea está por vencer en 3 días o menos
                due_date = fields.Date.from_string(task.date_deadline)
                today = fields.Date.today()
                task.is_due_soon = (due_date - today).days <= 3
            else:
                task.is_due_soon = False
