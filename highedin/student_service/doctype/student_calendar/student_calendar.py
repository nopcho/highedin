# -*- coding: utf-8 -*-
# Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class StudentCalendar(Document):
	def before_save(self):
		self.project_id = self.name
		self.date_submitted = frappe.utils.today()
		
