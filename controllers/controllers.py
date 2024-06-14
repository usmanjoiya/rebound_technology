# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

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
        news_data = []
        recs = request.env['rebound_technology.news'].sudo().search([])
        for rec in recs:
            news_data.append({
                'id': rec.id,
                'title': rec.name,
                'link': rec.link or False,
                'description': rec.description or False
            })
        data = {
            'all_news': news_data
        }
        return http.request.render('rebound_technology.news', data)

    @http.route('/news/<string:news_post_title>', auth='none', website=True)
    def sub_news_func(self, news_post_title, **kw):
        news = request.env['rebound_technology.news'].sudo().search([("name", '=', news_post_title), ('news_type', '=', 'content')])
        data = {
            'news_content': news.description,
            'title': news.name
        }
        return http.request.render('rebound_technology.sub_news', data)

    @http.route('/contact_us', auth='public', website=True)
    def contact_us_func(self, **kw):
        return http.request.render('rebound_technology.contact_us')

    @http.route('/contact/form', auth='public', type='http', website=True, csrf=False)
    def email_contact_form(self, **kw):
        form_data = kw
        print('abc')
        crm_rec = request.env['crm.lead'].sudo().create({
            'name': form_data['name'],
            'email_from': form_data['email'],
            'phone': form_data['phone'],
            'description': form_data['massage'],
            'type': 'opportunity'
        })
