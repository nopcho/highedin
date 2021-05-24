// Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
// For license information, please see license.txt

frappe.ui.form.on('AUN Program Level Evaluation', "template", (frm) => {
	frm.doc.criterion = []
	frm.doc.criterion_checklist = []
	frappe.model.with_doc("AUNQA Program Level Template", frm.doc.template, function() {																									
	var tabletransfer= frappe.model.get_doc("AUNQA Program Level Template", frm.doc.template);
		$.each(tabletransfer.criterion, function(index, row){
			let d = frm.add_child('criterion');
			d.criterion_no = row.criterion_no;																										
			d.description = row.description;																										
			frm.refresh_field('criterion');																									
		});
		$.each(tabletransfer.criterion_checklist, function(index, row){
			let d = frm.add_child('criterion_checklist');
			d.checklist_no = row.checklist_no;																										
			d.description = row.description;
			d.ref_criterion = row.ref_criterion;																										
			frm.refresh_field('criterion_checklist');																							
		});
	});																									
})