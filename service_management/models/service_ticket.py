# -*- coding: utf-8 -*-

from odoo import api, fields, models, _

class ServiceTicket(models.Model):
	_name = 'service.ticket'
	_inherit = ['mail.thread', 'mail.activity.mixin',]
	_description = 'Service Ticket'

	name = fields.Char(string='Ticket Name', required=True, tracking=True)
	description = fields.Text(string='Ticket Description')
	customer_id = fields.Many2one('res.partner', string='Customer')
	assigned_user_id = fields.Many2one('res.users', string='Assigned To')
	priority = fields.Selection([
		('low','Low'),
		('medium', 'Medium'),
		('high', 'High')
	], default='medium', tracking=True)
	state = fields.Selection([
		('new', 'New'),
		('inprogress', 'In Progress'),
		('resolved', 'Resolved'),
		('cancelled', 'Cancelled')
	], string='Status', default='new', tracking=True)
	date_requested = fields.Datetime(string='Request Date', default=fields.Datetime.now())
	date_resolved = fields.Datetime(string='Resolved Date')

	def action_start(self):
		for record in self:
			record.write({'state': 'inprogress'})

	def action_draft(self):
		for record in self:
			record.write({'state': 'new'})

	def action_cancel(self):
		for record in self:
			record.write({'state': 'cancelled'})

	def action_done(self):
		for record in self:
			mail_template = self.env.ref('service_management.service_ticket_resolved')
			record.with_context(force_send=True).message_post_with_source(
				mail_template,
				email_layout_xmlid='mail.mail_notification_layout_with_responsible_signature',
				subtype_xmlid='mail.mt_comment',
			)
			record.write({'state': 'resolved', 'date_resolved': fields.Datetime.now()})