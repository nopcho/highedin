// Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
// For license information, please see license.txt

frappe.ui.form.on('AUN Program Level Evaluation', "template", (frm) => {

	frappe.model.with_doc("AUNQA Program Level Template", frm.doc.template, function() {																									
	var tabletransfer= frappe.model.get_doc("AUNQA Program Level Template", frm.doc.template);
	// console.info('test')																								
	$.each(tabletransfer.criterion, function(index, row){
			// console.info('testloop');																						
			let d = frm.add_child('criterion');
			console.info(row.criterion_no, row.description);																							
			d.criterion_no = row.criterion_no;																										
			d.description = row.description;																										
			frm.refresh_field('criterion');																									
	});																									

	});																									
})