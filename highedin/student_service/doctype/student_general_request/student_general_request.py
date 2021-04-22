# -*- coding: utf-8 -*-
# Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class StudentGeneralRequest(WebsiteGenerator):
        def before_save(self):
                self.request_id = self.name
                self.route = "student-general-request/"+self.request_id
                self.date_submitted = frappe.utils.today()
        
        def before_submit(self):
                self.date_submitted = frappe.utils.today()

        def autoname(self):
                from frappe.model.naming import make_autoname
                self.name = make_autoname(self.naming_series)
