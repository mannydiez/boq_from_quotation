# -*- coding: utf-8 -*-
 
from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError
import logging 
log = logging.getLogger(__name__)

class boq_from_quotation_sale_order_extention(models.Model):
	_inherit = "sale.order"

	state = fields.Selection([
        ('draft', 'BoQ Created'),
        ('sent', 'BoQ Sent'),
        ('sale', 'Sales Order'),
        ('done', 'Locked'),
        ('cancel', 'Cancelled'),
        ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')


class boq_from_quotation_sale_estimate_job_extention(models.Model):
	_inherit = "sale.estimate.job"

	state = fields.Selection([
        ('draft', 'Draft'),
        ('sent', 'Estimate Sent'),
        ('confirm', 'Confirmed'),
        ('approve', 'Approved'),
        ('reject', 'Rejected'),
        ('quotesend', 'BoQ Created'),
        ('cancel', 'Cancelled')],
        default='draft',
        track_visibility='onchange',
        copy='False',
    )

	