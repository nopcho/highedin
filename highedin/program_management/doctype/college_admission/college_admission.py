# -*- coding: utf-8 -*-
# Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class CollegeAdmission(Document):
	def autoname(self):
		from frappe.model.naming import make_autoname
		self.name = make_autoname(self.naming_series)
		self.admission_code = self.name