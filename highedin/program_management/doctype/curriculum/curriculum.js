

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

frappe.ui.form.on('Curriculum Plan Type', {
	plan_type_abbr: function(frm, cdt, cdn) {
        var cur_rec = locals[cdt][cdn];
        cur_rec.plan_type_code = frm.doc.program_code + '-' + cur_rec.plan_type_abbr;
        frm.refresh_field('plan_type');
        }
});


frappe.ui.form.on('Curriculum Plan Option', {
        plan_option_code: function(frm, cdt, cdn) {
        var cur_rec = locals[cdt][cdn];
        cur_rec.plan_option_code = frm.doc.program_code + '-'+ cur_rec.major_abbr + '-' + cur_rec.plan_type_abbr;
        frm.refresh_field('plan_name');
        }
});
