# -*- coding: utf-8 -*-
# Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.utils import getdate
from frappe.model.document import Document


class AcademicTerms(Document):
    def autoname(self):
        self.name = self.academic_term + "/{}".format(self.academic_year) if self.academic_term else ""

    def validate(self):
        #Check if entry with same academic_year and the term_name already exists
        validate_duplication(self)
        self.title = format(self.academic_term) + "/{}".format(self.academic_year) if self.academic_term else ""

        #Check that start of academic year is earlier than end of academic year
        if self.start_date and self.end_date \
                                and getdate(self.start_date) > getdate(self.end_date):
            frappe.throw(_("The Term End Date cannot be earlier than the Term Start Date. Please correct the dates and try again."))

        # Check that the start of the term is not before the start of the academic year 
                # and end of term is not after the end of the academic year"""
                        
        year = frappe.get_doc("Academic Years",self.academic_year)
        if self.start_date and getdate(year.start_date) and (getdate(self.start_date) < getdate(year.start_date)):
            frappe.throw(_("The Term Start Date cannot be earlier than the Year Start Date of the Academic Year to which the term is linked (Academic Year {}). Please correct the dates and try again.").format(self.academic_year))

        if self.end_date and getdate(year.end_date) and (getdate(self.end_date) > getdate(year.end_date)):
            frappe.throw(_("The Term End Date cannot be later than the Year End Date of the Academic Year to which the term is linked (Academic Year {}). Please correct the dates and try again.").format(self.academic_year))


def validate_duplication(self):
    term = frappe.db.sql("""select name from `tabAcademic Terms` where academic_year= %s and academic_term= %s
    and docstatus<2 and name != %s""", (self.academic_year, self.academic_term, self.name))
    if term:
        frappe.throw(_("An academic term with this 'Academic Year' {0} and 'Term Name' {1} already exists. Please modify these entries and try again.").format(self.academic_year,self.academic_term))
