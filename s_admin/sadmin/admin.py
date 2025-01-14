from django.contrib import admin
from django.db import models
# Register your models here.

from .models import Level,Subject,SchoolClass,LevelClass,ClassMember,LevelClassInstance,Dept,StaffMember,\
    StaffSubject,Facility,FacilitySpace,SpaceSlot,ClassAssessment,LearnerAssessment,DailyPlan,\
    Schemes,Syllabus,Currency,MemberRegister,TermParameter,ClassBilling,SubjectBilling,MemberRecord, Receipt,\
   BlogPost ,PostContribution,PostCategory,PostOrigin,PostContribution

# Register your models here.

# Define the Currency admin class
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ('cu_num','cu_code','cu_name','cu_base','cu_rate','cu_valid_from','cu_status')

# Register the Currency admin class with the associated model
admin.site.register(Currency, CurrencyAdmin)

# Define the TermParameter admin class
class TermParameterAdmin(admin.ModelAdmin):
    list_display = ('tp_num','tp_year','tp_term','tp_weeks','tp_period_len','tp_cycledays','tp_days',
                    'tp_start_date','tp_seats','tp_end_date','tp_status','tp_schemed','tp_billed')

# Register the TermParameter admin class with the associated model
admin.site.register(TermParameter, TermParameterAdmin)

# Define the Level admin class
class LevelAdmin(admin.ModelAdmin):
    list_display = ('lv_code','lv_sb_code','lv_name','lv_status')

# Register the Level admin class with the associated model
admin.site.register(Level, LevelAdmin)

# Define the Subject admin class
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('sb_code','sb_type','sb_desc','sb_hrs','sb_status')

# Register the Subject admin class with the associated model
admin.site.register(Subject, SubjectAdmin)

# Define the SchoolClass admin class
class SchoolClassAdmin(admin.ModelAdmin):
    list_display = ('sc_code','sc_seats','sc_sf_num','sc_lv_code','sc_type','sc_desc','sc_status')

# Register the SchoolClass admin class with the associated model
admin.site.register(SchoolClass, SchoolClassAdmin)

# Define the LevelClass admin class
class LevelClassAdmin(admin.ModelAdmin):
    list_display = ('lc_num','lc_sc_code','lc_lv_code','lc_sb_code','lc_sf_num','lc_type','lc_desc','lc_hrs',
                    'lc_status','lc_scheme_status')

# Register the LevelClass admin class with the associated model
admin.site.register(LevelClass, LevelClassAdmin)

# Define the ClassMember admin class
class ClassMemberAdmin(admin.ModelAdmin):
    list_display = ('cm_num','cm_sc_code','cm_year','cm_lv_code','cm_surname','cm_fname','cm_othername','cm_gender',
                    'cm_guardian','cm_phone','cm_email','cm_dob','cm_doj','cm_dol','cm_status','cm_app_status')

# Register the ClassMember admin class with the associated model
admin.site.register(ClassMember, ClassMemberAdmin)

# Define the MemberRegister admin class
class MemberRegisterAdmin(admin.ModelAdmin):
    list_display = ('mr_num','mr_year','mr_term','mr_cm_num','mr_sc_code','mr_comment','mr_date','mr_day','mr_mark','mr_status')

# Register the MemberRegister admin class with the associated model
admin.site.register(MemberRegister, MemberRegisterAdmin)

# Define the LevelClassInstance admin class
class LevelClassInstanceAdmin(admin.ModelAdmin):
    list_display = ('ci_num','ci_lc_num','ci_sc_code','ci_lv_code','ci_sb_code','ci_type','ci_desc','ci_hrs',
                    'ci_status')

# Register the LevelClassInstance admin class with the associated model
admin.site.register(LevelClassInstance, LevelClassInstanceAdmin)

# Define the Syllabus admin class
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('sy_code','sb_ex_board','sy_lv_code','sy_sb_code','sy_type',
                   'sy_desc','sy_eff_date','sb_status')

# Register the Syllabus admin class with the associated model
admin.site.register(Syllabus, SyllabusAdmin)

# Define the Schemes admin class
class SchemesAdmin(admin.ModelAdmin):
    list_display = ('ch_num','ch_lc_num','ch_sc_code','ch_sf_num','ch_lv_code','ch_sb_code','ch_sy_code',
                  'ch_ex_board','ch_year','ch_term','ch_week','ch_type','ch_topic','ch_objectives','ch_competencies',
                 'ch_methods','ch_evaluation','ch_review1','ch_review2','ch_eff_date','ch_status'
                )

# Register the Schemes admin class with the associated model
admin.site.register(Schemes, SchemesAdmin)

# Define the DailyPlan admin class
class DailyPlanAdmin(admin.ModelAdmin):
    list_display = ('sp_num','sp_ch_num','sp_year','sp_term','sp_cycle','sp_lc_num','sp_sc_code','sp_sb_code','sp_day','sp_hrs',
                  'sp_area','sp_topic','sp_objective','sp_absorption','sp_paction','sp_top',
                  'sp_middle','sp_lower','sp_del_date','sp_plan_date','sp_start_time','sp_finish_time','sp_status')

# Register the DailyPlan admin class with the associated model
admin.site.register(DailyPlan, DailyPlanAdmin)

# Define the ClassAssessment admin class
class ClassAssessmentAdmin(admin.ModelAdmin):
    list_display = ('as_num','as_lc_num','as_sc_code','as_ch_num','as_sb_code','as_type',
            'as_name','as_remark','as_exception','as_comment','as_review','as_resources',
            'as_trans_date','as_status')

# Register the ClassAssessment admin class with the associated model
admin.site.register(ClassAssessment, ClassAssessmentAdmin)

# Define the LearnerAssessment admin class
class LearnerAssessmentAdmin(admin.ModelAdmin):
    list_display = ('la_num','la_sc_code','la_lc_num','la_cm_num','la_as_num','la_type',
                  'la_remark','la_comment','la_mark_f','la_grade_f','la_mark_a','la_grade_a','la_status')

# Register the LearnerAssessment admin class with the associated model
admin.site.register(LearnerAssessment, LearnerAssessmentAdmin)

# Define the Dept admin class
class DeptAdmin(admin.ModelAdmin):
    list_display = ('dp_code','dp_name','dp_status')

# Register the Dept admin class with the associated model
admin.site.register(Dept, DeptAdmin)

# Define the StaffMember admin class
class StaffMemberAdmin(admin.ModelAdmin):
    list_display = ('sf_num','sf_dp_code','sf_surname','sf_fname','sf_othername','sf_nok','sf_phone',
                    'sf_email','sf_dob','sf_doj','sf_dol','sf_status','sf_gender','sf_app_status')

# Register the StaffMember admin class with the associated model
admin.site.register(StaffMember, StaffMemberAdmin)

# Define the StaffSubject admin class
class StaffSubjectAdmin(admin.ModelAdmin):
    list_display = ('ss_num','ss_sf_num','ss_sb_code','ss_lv_code','ss_status')

# Register the StaffSubject admin class with the associated model
admin.site.register(StaffSubject, StaffSubjectAdmin)

# Define the Facility admin class
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('fc_num','fc_code','fc_name','fc_desc','fc_status','fc_type')

# Register the Facility admin class with the associated model
admin.site.register(Facility, FacilityAdmin)

# Define the FacilitySpace admin class
class FacilitySpaceAdmin(admin.ModelAdmin):
    list_display = ('fs_num','fs_fc_num','fs_desc','fs_status')

# Register the FacilitySpace admin class with the associated model
admin.site.register(FacilitySpace, FacilitySpaceAdmin)

# Define the SpaceSlot admin class
class SpaceSlotAdmin(admin.ModelAdmin):
    list_display = ('sp_num','sp_fs_num','sp_desc','sp_hrs','sp_fromtime','sp_totime','sp_status')

# Register the SpaceSlot admin class with the associated model
admin.site.register(SpaceSlot, SpaceSlotAdmin)

# Define the ClassBilling admin class
class ClassBillingAdmin(admin.ModelAdmin):
    list_display = ('cb_num','cb_sc_code','cb_lv_code','cb_type','cb_desc','cb_rate','cb_year','cb_term','cb_status')

# Register the SpaceSlot admin class with the associated model
admin.site.register(ClassBilling, ClassBillingAdmin)

# Define the SubjectBilling admin class
class SubjectBillingAdmin(admin.ModelAdmin):
    list_display = ('jb_num','jb_lc_num','jb_sc_code','jb_lv_code','jb_sb_code','jb_type','jb_desc',
                    'jb_rate','jb_status','jb_year','jb_term')

# Register the SubjectBilling admin class with the associated model
admin.site.register(SubjectBilling, SubjectBillingAdmin)

# Define the MemberRecord admin class
class MemberRecordAdmin(admin.ModelAdmin):
    list_display = ('mr_num','mr_cm_num','mr_sc_code','mr_lv_code','mr_cb_num','mr_jb_num','mr_year','mr_term',
                    'mr_trans_date','mr_due_date','mr_pamount','mr_aamount','mr_pay_ref',
                     'mr_category','mr_dr_cr','mr_paid','mr_status','mr_processed','mr_pay_type')

# Register the MemberRecord admin class with the associated model
admin.site.register(MemberRecord, MemberRecordAdmin)

# Define the Receipt admin class
class ReceiptAdmin(admin.ModelAdmin):
    list_display = ('rc_num','rc_cm_num','rc_sc_code','rc_lv_code','rc_mr_num','rc_period','rc_trans_date',
                    'rc_value_date','rc_due_date','rc_pamount','rc_aamount','rc_balance','rc_pay_ref',
                     'rc_dr_cr','rc_paid','rc_status','rc_processed','rc_pay_type'
                    )

# Register the Receipt admin class with the associated model
admin.site.register(Receipt, ReceiptAdmin)

# Blog Models admin registration Start here
# Define the PostCategory admin class
class PostCategoryAdmin(admin.ModelAdmin):
    list_display = ('ct_code','ct_desc','ct_seo_title','ct_seo_desc','slug')

# Register the admin class with the PostCategory model
admin.site.register(PostCategory, PostCategoryAdmin )

# Define the PostOrigin admin class
class PostOriginAdmin(admin.ModelAdmin):
    list_display = ('po_num','po_name','po_position')

# Register the admin class with the PostOrigin model
admin.site.register(PostOrigin, PostOriginAdmin)

# Define the BlogPost admin class
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('bp_heading', 'slug', 'bp_status','bp_date')
    list_filter = ("bp_status",)
    search_fields = ['bp_heading', 'bp_body']
    prepopulated_fields = {'slug': ('bp_heading',)}

# Register the admin class with the BlogPost model
admin.site.register(BlogPost, BlogPostAdmin)

# Define the PostContribution admin class
class PostContributionAdmin(admin.ModelAdmin):
    list_display = ('pc_contributor', 'pc_contribution', 'pc_bp_num', 'ad_date_c', 'pc_active')
    list_filter = ('pc_active', 'ad_date_c')
    search_fields = ('pc_contributor', 'pc_email', 'pc_contribution')
    actions = ['approve_contributions']

    def approve_contributions(self, request, queryset):
        queryset.update(pc_active=True)

# Register the admin class with the PostContribution model
admin.site.register(PostContribution, PostContributionAdmin)
