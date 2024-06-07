# -*- coding: utf-8 -*-
from odoo import http

class ReboundTech(http.Controller):

    @http.route('/', auth='public', website=True)
    def rebound_technology_home(self, **kw):
        return http.request.render('rebound_technology.rebound_technology_home')

    @http.route('/technology', auth='public', website=True)
    def technology_func(self, **kw):
        return http.request.render('rebound_technology.technology')

    @http.route('/sustainability', auth='public', website=True)
    def sustainability_func(self, **kw):
        return http.request.render('rebound_technology.sustainability')

    @http.route('/team', auth='public', website=True)
    def team_func(self, **kw):
        return http.request.render('rebound_technology.team')

    @http.route('/news', auth='public', website=True)
    def news_func(self, **kw):
        return http.request.render('rebound_technology.news')

    @http.route('/contact_us', auth='public', website=True)
    def contact_us_func(self, **kw):
        return http.request.render('rebound_technology.contact_us')
