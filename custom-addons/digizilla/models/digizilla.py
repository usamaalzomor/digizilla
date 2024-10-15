# digizilla/models/digizilla.py
from odoo import models, fields

class Digizilla(models.Model):
    _name = 'digizilla.addon'
    _description = 'Digizilla'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'id desc'

    name = fields.Char(string='Name', required=True, tracking=True)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ], string='Gender',  tracking=True)
    country = fields.Many2one('res.country', string='Country', tracking=True)
    joining_date = fields.Date(string='Joining Date', tracking=True)
    tags = fields.Char(string='Tags', tracking=True)
    customer_ids = fields.Many2many(
        'res.partner',
        string='Customers',
        tracking=True
    )
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company, tracking=True)
    notes = fields.Text(string='Notes', tracking=True)
    comments = fields.Char(string='Comments', tracking=True)
