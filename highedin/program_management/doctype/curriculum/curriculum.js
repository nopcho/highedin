// Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
// For license information, please see license.txt

frappe.ui.form.on('Curriculum', {
	// refresh: function(frm) {

	// }
});
frappe.ui.form.on('Curriculum Major', {
	major_name_abbr: function(frm, cdt, cdn) {
	var cur_rec = locals[cdt][cdn];
	cur_rec.major_code = frm.doc.program_code + '-' + cur_rec.major_name_abbr;
	frm.refresh_field('major');
	}
});
