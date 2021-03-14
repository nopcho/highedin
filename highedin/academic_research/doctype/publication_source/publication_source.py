# -*- coding: utf-8 -*-
# Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.website.website_generator import WebsiteGenerator
from frappe.utils import cstr, nowdate, cint


class PublicationSource(WebsiteGenerator):
    website = frappe._dict(
        template = "templates/generators/publication_source.html",
#        condition_field = "publish",
        page_title_field = "title"
    )

    def autoname(self):
       from frappe.model.naming import make_autoname
       self.name = make_autoname(self.naming_series)

    def get_context(self, context):
        if frappe.session.user == 'Guest':
          frappe.throw("You need to login to access this page", frappe.PermissionError);
#        show breadcrumbs
        context.parents = [{'route': 'publication_source', 'title': 'Publication Source' }]
        context.no_cache = 1
#        context.show_sidebar = True
        context.show_search = True
#        context.doc = frappe.get_doc('Publication Source', self.name)
#        frappe.throw(context.doc, frappe.PermissionError)
#        if not frappe.has_website_permission(context.doc):
#           frappe.throw("Not Permitted", frappe.PermissionError)

def get_list_context(context):
#       from erpnext.controllers.website_list_for_contact import get_list_context
#       list_context = get_list_context(context)
#       context.title = 'title'
        if frappe.session.user == 'Guest':
          frappe.throw("Login required", frappe.PermissionError);
        context.show_search = True
#        context.get_list = get_journal_list
#        return context
        context.update({
                "show_sidebar": False,
                "show_search": True,
                "title": _("Publication Source List"),
                "get_list": get_journal_list,
                "row_template": "academic_research/doctype/publication_source/templates/publication_source_row.html",
        })
        return context

def get_journal_list(doctype, txt, filters, limit_start, limit_page_length=1000, order_by=None):
        from frappe.www.list import get_list
        #user = frappe.session.user
        #ignore_permissions = False
        #if is_website_user():
        #       if not filters: filters = []
        #       filters.append(("Issue", "raised_by", "=", user))
        ignore_permissions = True
        fields = None
        order_by = 'title'
        filters= []
        filters.append(("Publication Source","status", "=", "Active"))
        return get_list(doctype, txt, filters, limit_start, limit_page_length, ignore_permissions, fields, order_by)
