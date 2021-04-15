# -*- coding: utf-8 -*-
# Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class StudentLeaveRequest(Document):
	def before_save(self):
		self.leave_request_id = self.name
