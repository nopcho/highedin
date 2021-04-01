# -*- coding: utf-8 -*-
# Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.website.website_generator import WebsiteGenerator

class StudentGeneralRequest(WebsiteGenerator):
        def before_save(self):
                self.request_id = self.name
                self.status = "Edit"
        
        def before_submit(self):
                self.status = "Submit"

        def before_cancel(self):
                self.status = "Cancel"
