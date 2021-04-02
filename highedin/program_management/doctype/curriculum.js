
frappe.ui.form.on('Curriculum Major', {
	major_name_abbr: function(frm, cdt, cdn) {
		console.log(5)
		var cur_rec = locals[cdt][cdn];
		console.log(cur_rec)
		cur_rec.major_code = frm.doc.program_code + '-' + cur_rec.major_name_abbr;
		frm.refresh_field('major');
		}
});
