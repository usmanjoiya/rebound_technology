# -*- coding: utf-8 -*-

from odoo import models, fields, api


class rebound_tech(models.Model):
    _name = 'rebound_tech.news'
    _description = 'rebound_tech.news'

    name = fields.Char()
    news_type =fields.Selection([('content','Content'), ('link', 'Link')], required=1, string="News Type")
    description = fields.Text()

