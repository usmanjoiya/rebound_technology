# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rebound_technology(models.Model):
    _name = 'rebound_technology.news'
    _description = 'rebound_technology.news'

    name = fields.Char()
    news_type =fields.Selection([('content','Content'), ('link', 'Link')], required=1, string="News Type")
    description = fields.Text()

