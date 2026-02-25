<odoo>
<!--  Inline form view for creating/editing contact persons  -->
<record id="view_res_partner_contact_inline_form" model="ir.ui.view">
<field name="name">res.partner.contact.inline.form</field>
<field name="model">res.partner</field>
<field name="priority">999</field>
<field name="arch" type="xml">
<form string="Contact Person">
<sheet>
<group>
<group>
<field name="name" string="Full Name"/>
<field name="job_position" string="Job Position"/>
<field name="phone"/>
<field name="mobile"/>
<field name="email"/>
</group>
<group>
<field name="parent_id" string="Company" readonly="1"/>
<field name="type" invisible="1"/>
<field name="company_type" invisible="1"/>
</group>
</group>
</sheet>
</form>
</field>
</record>
<!--  Kanban view for contact persons embedded in the lead  -->
<record id="view_res_partner_contact_kanban" model="ir.ui.view">
<field name="name">res.partner.contact.kanban</field>
<field name="model">res.partner</field>
<field name="priority">999</field>
<field name="arch" type="xml">
<kanban quick_create="false">
<field name="name"/>
<field name="job_position"/>
<field name="phone"/>
<field name="mobile"/>
<field name="email"/>
<field name="image_128"/>
<templates>
<t t-name="kanban-box">
<div class="oe_kanban_global_click o_kanban_record d-flex flex-column align-items-center p-3">
<img t-att-src="kanban_image('res.partner', 'image_128', record.id.raw_value)" class="o_kanban_image rounded-circle mb-2" style="width:64px; height:64px; object-fit:cover;" alt="Contact"/>
<strong class="o_kanban_record_title text-center">
<field name="name"/>
</strong>
<span t-if="record.job_position.value" class="text-muted small text-center">
<field name="job_position"/>
</span>
<div class="mt-1 text-center">
<t t-if="record.phone.value">
<div>
<i class="fa fa-phone me-1"/>
<field name="phone"/>
</div>
</t>
<t t-if="record.mobile.value">
<div>
<i class="fa fa-mobile me-1"/>
<field name="mobile"/>
</div>
</t>
<t t-if="record.email.value">
<div>
<i class="fa fa-envelope me-1"/>
<field name="email"/>
</div>
</t>
</div>
</div>
</t>
</templates>
</kanban>
</field>
</record>
<!--  Inject Contacts tab into the CRM lead form  -->
<record id="crm_lead_contacts_form_view" model="ir.ui.view">
<field name="name">crm.lead.contacts.form</field>
<field name="model">crm.lead</field>
<field name="inherit_id" ref="crm.crm_lead_all_leads"/>
<field name="arch" type="xml">
<xpath expr="//notebook" position="inside">
<page string="Contacts" name="contacts_tab">
<field name="contact_ids" mode="kanban" widget="many2many" domain="[('company_type', '=', 'person'), ('type', '=', 'contact')]" context="{ 'default_parent_id': partner_id, 'default_type': 'contact', 'default_company_type': 'person', 'form_view_ref': 'crm_lead_contacts.view_res_partner_contact_inline_form', 'kanban_view_ref': 'crm_lead_contacts.view_res_partner_contact_kanban' }" options="{'no_create_edit': False, 'create': True}">
<kanban quick_create="false">
<field name="name"/>
<field name="job_position"/>
<field name="phone"/>
<field name="mobile"/>
<field name="email"/>
<field name="image_128"/>
<templates>
<t t-name="kanban-box">
<div class="oe_kanban_global_click o_kanban_record d-flex flex-column align-items-center p-3">
<img t-att-src="kanban_image('res.partner', 'image_128', record.id.raw_value)" class="o_kanban_image rounded-circle mb-2" style="width:64px; height:64px; object-fit:cover;" alt="Contact"/>
<strong class="o_kanban_record_title text-center">
<field name="name"/>
</strong>
<span t-if="record.job_position.value" class="text-muted small text-center">
<field name="job_position"/>
</span>
<div class="mt-1 text-center">
<t t-if="record.phone.value">
<div>
<i class="fa fa-phone me-1"/>
<field name="phone"/>
</div>
</t>
<t t-if="record.mobile.value">
<div>
<i class="fa fa-mobile me-1"/>
<field name="mobile"/>
</div>
</t>
<t t-if="record.email.value">
<div>
<i class="fa fa-envelope me-1"/>
<field name="email"/>
</div>
</t>
</div>
</div>
</t>
</templates>
</kanban>
</field>
</page>
</xpath>
</field>
</record>
</odoo>
