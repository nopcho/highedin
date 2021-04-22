# -*- coding: utf-8 -*-
# Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.website.website_generator import WebsiteGenerator

class AUNQAProgramLevelTemplate(WebsiteGenerator):
	def validate(self):
		self.aunqa_code = self.name
		self.route = 'aunqa-program-level-template/'+self.aunqa_code
		# self.criterion[0].criterion_no = self.criterion[0].name
