// Copyright (c) 2021, Nopporn Chotikakamthorn and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student General Request', {
	 refresh: function(frm) {
	 	console.log(frappe.user)
	 }
});

//frappe.listview_settings('Student Genral Request', {
//	filters: [
//		['status', '=', frappe.user_roles]
//	]
//});
