
from .models import Level,Subject,SchoolClass,LevelClass,ClassMember,LevelClassInstance,Dept,StaffMember,\
    StaffSubject,Facility,FacilitySpace,SpaceSlot,ClassAssessment,LearnerAssessment,DailyPlan,Schemes,\
    Syllabus, Currency,MemberRegister,TermParameter,ClassBilling,SubjectBilling,MemberRecord, Receipt,BlogPost\
    , PostContribution,PostCategory,PostOrigin,PostContribution,ExcludedDay,SchoolLevel,ClassSubject,AuthRelation\
    , MemberMovement

from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput
from django import forms
from django.shortcuts import render
import json
from decimal import *
from django.db.models import Sum, F,Avg, Max, Min,Count,Q

# Create the Currency form class
class CurrencyForm(forms.ModelForm):
        # meta class
        class Meta:
            model = Currency
            # specify fields to be used
            fields = ['cu_num','cu_code','cu_name','cu_base','cu_rate','cu_valid_from','cu_status']
            widgets = {
                'cu_valid_from': widgets.DateInput(attrs={'type': 'date'}),
                #'od_status_date': widgets.DateInput(attrs={'type': 'date'}),
             }

# Create the ExcludedDay form class
class ExcludedDayForm(forms.ModelForm):
        # meta class
        class Meta:
            model = ExcludedDay
            # specify fields to be used
            fields = ['ex_code','ex_name','ex_date','ex_status']
            widgets = {
                'ex_date': widgets.DateInput(attrs={'type': 'date'}),
                #'od_status_date': widgets.DateInput(attrs={'type': 'date'}),
             }

# Create the Year Terms Parameters form class
class TermParameterForm(forms.ModelForm):
        # meta class
        class Meta:
            model = TermParameter
            # specify fields to be used
            fields = ['tp_num','tp_year','tp_term','tp_weeks','tp_period_len','tp_cycledays','tp_days','tp_seats',
                      'tp_start_date','tp_end_date','tp_start_time','tp_end_time','tp_status','tp_schemed','tp_billed']
            widgets = {
                'tp_start_date': widgets.DateInput(attrs={'type': 'date'}),
                'tp_end_date': widgets.DateInput(attrs={'type': 'date'}),
                'tp_start_time': widgets.TimeInput(attrs={'type': 'time'}),
                'tp_end_time': widgets.TimeInput(attrs={'type': 'time'}),
             }

#Form for running the orders graphs

class OrdRunForm(forms.Form):
    ord_choices = (("S","Sales Orders"),("P","Purchase Orders"))
    go = forms.ChoiceField(choices=ord_choices)

#Form for running the orders graphs

class GenSchemeForm(forms.Form):
        comm_choices = (("Y", "Proceed"), ("N", "Stop"))
        f_year = forms.IntegerField()
        f_term = forms.IntegerField()
        Gen_ok = forms.ChoiceField(choices=comm_choices)

#Form for running the orders graphs

class GenRegiserForm(forms.Form):
        comm_choices = (("Y", "Proceed"), ("N", "Stop"))
        f_year = forms.IntegerField()
        f_term = forms.IntegerField()
        Gen_ok = forms.ChoiceField(choices=comm_choices)
class GenSpaceLotForm(forms.Form):
    comm_choices = (("Y", "Proceed"), ("N", "Stop"))
    f_year = forms.IntegerField()
    f_term = forms.IntegerField()
    Gen_ok = forms.ChoiceField(choices=comm_choices)

class GenBillForm(forms.Form):
        comm_choices = (("Y", "Proceed"), ("N", "Stop"))
        f_year = forms.IntegerField()
        f_term = forms.IntegerField()
        Gen_ok = forms.ChoiceField(choices=comm_choices)
class GenClassForm(forms.Form):
        comm_choices = (("Y", "Proceed"), ("N", "Stop"))
        f_year = forms.IntegerField()
        f_term = forms.IntegerField()
        Gen_ok = forms.ChoiceField(choices=comm_choices)
class GenLevelForm(forms.Form):
    comm_choices = (("Y", "Proceed"), ("N", "Stop"))
    l_code = forms.IntegerField()
    Gen_ok = forms.ChoiceField(choices=comm_choices)

class GenMovementForm(forms.Form):
    comm_choices = (("Y", "Proceed"), ("N", "Stop"))
    class_code = forms.CharField()
    Gen_ok = forms.ChoiceField(choices=comm_choices)

# Create the Level form class
class LevelForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Level
        # specify fields to be used
        fields = ['lv_code','lv_sl_code','lv_name','lv_status'] #'lv_sb_code',
        #widgets = {
         #   'ee_date_joined': widgets.DateInput(attrs={'type': 'date'}),
          #  'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         #}

# Create the Subject form class
class SubjectForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Subject
        # specify fields to be used
        fields = ['sb_code','sb_type','sb_desc', 'sb_hrs','sb_status']
        #widgets = {
         #   'ee_date_joined': widgets.DateInput(attrs={'type': 'date'}),
          #  'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         #}

# Create the ClassSubject form class
class ClassSubjectForm(forms.ModelForm):
    # meta class
    class Meta:
        model = ClassSubject
        # specify fields to be used
        fields = ['cs_code','cs_sb_code','cs_name','cs_sl_code','cs_sc_code','cs_status']
        #widgets = {
         #   'ee_date_joined': widgets.DateInput(attrs={'type': 'date'}),
          #  'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         #}

# Create the SchoolLevel form class
class SchoolLevelForm(forms.ModelForm):
    # meta class
    class Meta:
        model = SchoolLevel
        # specify fields to be used
        fields = ['sl_code','sl_name','sl_status']
        #widgets = {
         #   'ee_date_joined': widgets.DateInput(attrs={'type': 'date'}),
          #  'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         #}

# Create the SchoolClass form class
class SchoolClassForm(forms.ModelForm):
    # meta class
    class Meta:
        model = SchoolClass
        # specify fields to be used
        fields = ['sc_code','sc_seats','sc_sf_num','sc_type','sc_desc','sc_status']
        #widgets = {
         #   'ee_date_joined': widgets.DateInput(attrs={'type': 'date'}),
          #  'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         #}

# Create the LevelClass form class
class LevelClassForm(forms.ModelForm):
    # meta class
    class Meta:
        model = LevelClass
        # specify fields to be used
        fields = ['lc_num','lc_sb_code','lc_type','lc_desc','lc_hrs','lc_status']
        #widgets = {
         #   'ee_date_joined': widgets.DateInput(attrs={'type': 'date'}),
          #  'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         #}

# Create the ClassMember form class
class ClassMemberForm(forms.ModelForm):
    # meta class
    class Meta:
        model = ClassMember
        # specify fields to be used
        fields = ['cm_num','cm_year','cm_surname','cm_fname','cm_othername','cm_gender','cm_guardian',
                    'cm_phone','cm_email','cm_dob','cm_doj','cm_dol','cm_status','cm_app_status']
        widgets = {
            'cm_dob': widgets.DateInput(attrs={'type': 'date'}),
            'cm_doj': widgets.DateInput(attrs={'type': 'date'}),
            'cm_dol': widgets.DateInput(attrs={'type': 'date'}),
            'cm_year': forms.HiddenInput(),
         }

# Create the MemberRegister forms classes
class MemberRegisterForm(forms.ModelForm):
    # meta class
    class Meta:
        model = MemberRegister
        # specify fields to be used
        fields = ['mr_num','mr_year','mr_term','mr_mark','mr_cm_num','mr_comment','mr_date','mr_day','mr_status'] #'mr_sc_code',
        widgets = {
            'mr_date': widgets.DateInput(attrs={'type': 'date'}),
            #'cm_doj': widgets.DateInput(attrs={'type': 'date'}),
            #'cm_dol': widgets.DateInput(attrs={'type': 'date'}),
         }
class MemberRegister1Form(forms.ModelForm):
    # meta class
    class Meta:
        model = MemberRegister
        # specify fields to be used
        fields = ['mr_num','mr_sc_code','mr_year','mr_term','mr_mark_1','mr_cm_num','mr_comment','mr_date','mr_day','mr_status']
        widgets = {
            'mr_date': widgets.DateInput(attrs={'type': 'date'}),
            #'cm_doj': widgets.DateInput(attrs={'type': 'date'}),
            #'cm_dol': widgets.DateInput(attrs={'type': 'date'}),
            'mr_sc_code': forms.HiddenInput(),
            'mr_year': forms.HiddenInput(),
            'mr_term': forms.HiddenInput(),
            'mr_status': forms.HiddenInput(),
         }
class MemberRegister2Form(forms.ModelForm):
    # meta class
    class Meta:
        model = MemberRegister
        # specify fields to be used
        fields = ['mr_num','mr_sc_code','mr_year','mr_term','mr_mark_2','mr_cm_num','mr_comment','mr_date','mr_day','mr_status']
        widgets = {
            'mr_date': widgets.DateInput(attrs={'type': 'date'}),
            'mr_sc_code': forms.HiddenInput(),
            'mr_year': forms.HiddenInput(),
            'mr_term': forms.HiddenInput(),
            'mr_status': forms.HiddenInput(),
         }

class MemberRegister3Form(forms.ModelForm):
    # meta class
    class Meta:
        model = MemberRegister
        # specify fields to be used
        fields = ['mr_num','mr_sc_code','mr_year','mr_term','mr_mark_3','mr_cm_num','mr_comment','mr_date','mr_day','mr_status']
        widgets = {
            'mr_date': widgets.DateInput(attrs={'type': 'date'}),
            'mr_sc_code': forms.HiddenInput(),
            'mr_year': forms.HiddenInput(),
            'mr_term': forms.HiddenInput(),
            'mr_status': forms.HiddenInput(),
         }

class MemberRegister4Form(forms.ModelForm):
    # meta class
    class Meta:
        model = MemberRegister
        # specify fields to be used
        fields = ['mr_num','mr_sc_code','mr_year','mr_term','mr_mark_4','mr_cm_num','mr_comment','mr_date','mr_day','mr_status']
        widgets = {
            'mr_date': widgets.DateInput(attrs={'type': 'date'}),
            'mr_sc_code': forms.HiddenInput(),
            'mr_year': forms.HiddenInput(),
            'mr_term': forms.HiddenInput(),
            'mr_status': forms.HiddenInput(),
         }

class MemberRegister5Form(forms.ModelForm):
    # meta class
    class Meta:
        model = MemberRegister
        # specify fields to be used
        fields = ['mr_num','mr_sc_code','mr_year','mr_term','mr_mark_5','mr_cm_num','mr_comment','mr_date','mr_day','mr_status']
        widgets = {
            'mr_date': widgets.DateInput(attrs={'type': 'date'}),
            'mr_sc_code': forms.HiddenInput(),
            'mr_year': forms.HiddenInput(),
            'mr_term': forms.HiddenInput(),
            'mr_status': forms.HiddenInput(),
         }

class MemberRegister6Form(forms.ModelForm):
    # meta class
    class Meta:
        model = MemberRegister
        # specify fields to be used
        fields = ['mr_num','mr_sc_code','mr_year','mr_term','mr_mark_6','mr_cm_num','mr_comment','mr_date','mr_day','mr_status']
        widgets = {
            'mr_date': widgets.DateInput(attrs={'type': 'date'}),
            'mr_sc_code': forms.HiddenInput(),
            'mr_year': forms.HiddenInput(),
            'mr_term': forms.HiddenInput(),
            'mr_status': forms.HiddenInput(),
         }

class MemberRegister7Form(forms.ModelForm):
    # meta class
    class Meta:
        model = MemberRegister
        # specify fields to be used
        fields = ['mr_num','mr_sc_code','mr_year','mr_term','mr_mark_7','mr_cm_num','mr_comment','mr_date','mr_day','mr_status']
        widgets = {
            'mr_date': widgets.DateInput(attrs={'type': 'date'}),
            'mr_sc_code': forms.HiddenInput(),
            'mr_year': forms.HiddenInput(),
            'mr_term': forms.HiddenInput(),
            'mr_status': forms.HiddenInput(),
         }

class MemberRegister8Form(forms.ModelForm):
    # meta class
    class Meta:
        model = MemberRegister
        # specify fields to be used
        fields = ['mr_num','mr_sc_code','mr_year','mr_term','mr_mark_8','mr_cm_num','mr_comment','mr_date','mr_day','mr_status']
        widgets = {
            'mr_date': widgets.DateInput(attrs={'type': 'date'}),
            'mr_sc_code': forms.HiddenInput(),
            'mr_year': forms.HiddenInput(),
            'mr_term': forms.HiddenInput(),
            'mr_status': forms.HiddenInput(),
         }

class MemberRegister9Form(forms.ModelForm):
    # meta class
    class Meta:
        model = MemberRegister
        # specify fields to be used
        fields = ['mr_num','mr_sc_code','mr_year','mr_term','mr_mark_9','mr_cm_num','mr_comment','mr_date','mr_day','mr_status']
        widgets = {
            'mr_date': widgets.DateInput(attrs={'type': 'date'}),
            'mr_sc_code': forms.HiddenInput(),
            'mr_year': forms.HiddenInput(),
            'mr_term': forms.HiddenInput(),
            'mr_status': forms.HiddenInput(),
         }

class MemberRegister10Form(forms.ModelForm):
    # meta class
    class Meta:
        model = MemberRegister
        # specify fields to be used
        fields = ['mr_num','mr_sc_code','mr_year','mr_term','mr_mark_10','mr_cm_num','mr_comment','mr_date','mr_day','mr_status']
        widgets = {
            'mr_date': widgets.DateInput(attrs={'type': 'date'}),
            'mr_sc_code': forms.HiddenInput(),
            'mr_year': forms.HiddenInput(),
            'mr_term': forms.HiddenInput(),
            'mr_status': forms.HiddenInput(),
         }

# Create the LevelClassInstance form class
class LevelClassInstanceForm(forms.ModelForm):
    # meta class
    class Meta:
        model = LevelClassInstance
        # specify fields to be used
        fields = ['ci_num','ci_lc_num','ci_sc_code','ci_lv_code','ci_sb_code','ci_type','ci_desc','ci_hrs',
                    'ci_status']
        #widgets = {
         #   'ee_date_joined': widgets.DateInput(attrs={'type': 'date'}),
          #  'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         #}

# Create the Syllabus form class
class SyllabusForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Syllabus
        # specify fields to be used
        fields = ['sy_code','sb_ex_board','sy_lv_code','sy_sb_code','sy_type',
                   'sy_desc','sy_eff_date','sb_status']
        widgets = {
            'sy_eff_date': widgets.DateInput(attrs={'type': 'date'}),
          #  'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         }

# Create the Schemes form class
class SchemesForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Schemes
        # specify fields to be used
        fields = ['ch_num','ch_sy_code','ch_ex_board','ch_year','ch_term','ch_week','ch_type','ch_topic','ch_objectives',
                  'ch_competencies','ch_methods','ch_evaluation','ch_review1','ch_review2',
                  'ch_eff_date','ch_status'] #'ch_lc_num','ch_sc_code','ch_sf_num','ch_lv_code','ch_sb_code',
        widgets = {
            'ch_eff_date': widgets.DateInput(attrs={'type': 'date'}),
            #'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
            #'ch_year': forms.HiddenInput(),
            #'ch_term': forms.HiddenInput(),
         }

# Create the DailyPlan form class
class DailyPlanForm(forms.ModelForm):
    # meta class
    class Meta:
        model = DailyPlan
        # specify fields to be used
        fields = ['sp_num','sp_ch_num','sp_lc_num','sp_sc_code','sp_sb_code','sp_year','sp_term','sp_cycle','sp_day',
                  'sp_hrs','sp_area','sp_topic','sp_objective','sp_absorption','sp_paction','sp_top','sp_middle',
                  'sp_lower','sp_hnotes','sp_del_date','sp_plan_date','sp_start_time','sp_finish_time','sp_status']
        widgets = {
            'sp_del_date': widgets.DateInput(attrs={'type': 'date'}),
            'sp_plan_date': widgets.DateInput(attrs={'type': 'date'}),
            'sp_start_time': widgets.TimeInput(attrs={'type': 'time'}),
            'sp_finish_time': widgets.TimeInput(attrs={'type': 'time'}),
            'sp_ch_num': forms.HiddenInput(),
            'sp_lc_num': forms.HiddenInput(),
            'sp_sc_code': forms.HiddenInput(),
            'sp_sb_code': forms.HiddenInput(),
         }

# Create the ClassAssessment form class
class ClassAssessmentForm(forms.ModelForm):
    # meta class
    class Meta:
        model = ClassAssessment
        # specify fields to be used
        fields = ['as_num','as_type','as_name','as_remark','as_exception','as_comment',
                  'as_review','as_resources','as_trans_date','as_status'] #'as_lc_num','as_sc_code','as_ch_num',
                  # 'as_sb_code'
        widgets = {
            'as_trans_date': widgets.DateInput(attrs={'type': 'date'}),
          #  'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         }

# Create the LearnerAssessment form class
class LearnerAssessmentForm(forms.ModelForm):
    # meta class
    class Meta:
        model = LearnerAssessment
        # specify fields to be used
        fields = ['la_num','la_type','la_cm_num','la_remark','la_comment','la_mark_f','la_grade_f',
                  'la_mark_a','la_grade_a','la_status'] #la_sc_code','la_lc_num','la_as_num','la_sb_code'
        #widgets = {
         #   'ee_date_joined': widgets.DateInput(attrs={'type': 'date'}),
          #  'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         #}

# Create the Dept form class
class DeptForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Dept
        # specify fields to be used
        fields = ['dp_code','dp_name','dp_status']
        #widgets = {
         #   'ee_date_joined': widgets.DateInput(attrs={'type': 'date'}),
          #  'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         #}

# Create the StaffMember form class
class StaffMemberForm(forms.ModelForm):
    # meta class
    class Meta:
        model = StaffMember
        # specify fields to be used
        fields = ['sf_num','sf_dp_code','sf_surname','sf_fname','sf_othername','sf_ll_code','sf_nok','sf_phone',
                    'sf_email','sf_dob','sf_doj','sf_dol','sf_status','sf_gender','sf_app_status']
        widgets = {
            'sf_dob': widgets.DateInput(attrs={'type': 'date'}),
            'sf_doj': widgets.DateInput(attrs={'type': 'date'}),
            'sf_dol': widgets.DateInput(attrs={'type': 'date'}),
            'sf_dp_code': forms.HiddenInput(),
         }

# Create the StaffSubject form class
class StaffSubjectForm(forms.ModelForm):
    # meta class
    class Meta:
        model = StaffSubject
        # specify fields to be used
        fields = ['ss_num','ss_sb_code','ss_lv_code','ss_status'] #'ss_sf_num',
        #widgets = {
         #   'ee_date_joined': widgets.DateInput(attrs={'type': 'date'}),
          #  'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         #}

# Create the Facility form class
class FacilityForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Facility
        # specify fields to be used
        fields = ['fc_num','fc_code','fc_name','fc_desc','fc_status','fc_type']
        #widgets = {
         #   'ee_date_joined': widgets.DateInput(attrs={'type': 'date'}),
          #  'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         #}

# Create the FacilitySpace form class
class FacilitySpaceForm(forms.ModelForm):
    # meta class
    class Meta:
        model = FacilitySpace
        # specify fields to be used
        fields = ['fs_num','fs_desc','fs_status'] #'fs_fc_num',
        #widgets = {
         #   'ee_date_joined': widgets.DateInput(attrs={'type': 'date'}),
          #  'ee_dob': widgets.DateInput(attrs={'type': 'date'}),
         #}

# Create the SpaceSlot form class
class SpaceSlotForm(forms.ModelForm):
    # meta class
    class Meta:
        model = SpaceSlot
        # specify fields to be used
        fields = ['sp_num','sp_fs_num','sp_date','sp_day','sp_start_time','sp_finish_time','sp_sc_code',
                  'sp_sf_num','sp_type','sp_desc','sp_hrs','sp_status']
        widgets = {
            'sp_fs_num': forms.HiddenInput(),
            'sp_date': widgets.DateInput(attrs={'type': 'date'}),
            'sp_start_time': widgets.TimeInput(attrs={'type': 'time'}),
            'sp_finish_time': widgets.TimeInput(attrs={'type': 'time'}),
         }

# Create the ClassBilling form class
class ClassBillingForm(forms.ModelForm):
    # meta class
    class Meta:
        model = ClassBilling
        # specify fields to be used
        fields = ['cb_num','cb_sc_code','cb_lv_code','cb_type','cb_desc','cb_rate','cb_year','cb_term','cb_status']
        widgets = {
            'cb_sc_code': forms.HiddenInput(),
            'cb_lv_code': forms.HiddenInput(),
            'cb_year': forms.HiddenInput(),
            'cb_term': forms.HiddenInput(),
         }

# Create the SubjectBilling form class
class SubjectBillingForm(forms.ModelForm):
    # meta class
    class Meta:
        model = SubjectBilling
        # specify fields to be used
        fields = ['jb_num','jb_lc_num','jb_sc_code','jb_lv_code','jb_sb_code','jb_type',
                  'jb_desc','jb_rate','jb_year','jb_term','jb_status']
        widgets = {
            'jb_lc_num': forms.HiddenInput(),
            'jb_sc_code': forms.HiddenInput(),
            'jb_lv_code': forms.HiddenInput(),
            'jb_sb_code': forms.HiddenInput(),
            'jb_year': forms.HiddenInput(),
            'jb_term': forms.HiddenInput(),
        }

# Create the MemberRecord form class
class MemberRecordForm(forms.ModelForm):
    # meta class
    class Meta:
        model = MemberRecord
        # specify fields to be used
        fields = ['mr_num','mr_cm_num','mr_sc_code','mr_lv_code','mr_cb_num','mr_year','mr_term',
                  'mr_trans_date','mr_due_date','mr_pamount','mr_aamount','mr_pay_ref',
                  'mr_category','mr_dr_cr','mr_paid','mr_status','mr_processed','mr_pay_type'
                 ]
        widgets = {
            'mr_cm_num': forms.HiddenInput(),
            'mr_sc_code': forms.HiddenInput(),
            'mr_lv_code': forms.HiddenInput(),
            'mr_category': forms.HiddenInput(),
            'mr_year': forms.HiddenInput(),
            'mr_term': forms.HiddenInput(),
            'mr_trans_date': widgets.DateInput(attrs={'type': 'date'}),
            'mr_due_date': widgets.DateInput(attrs={'type': 'date'}),
        }

# Create the Receipt form class
class ReceiptForm(forms.ModelForm):
    # meta class
    class Meta:
        model = Receipt
        # specify fields to be used
        fields = ['rc_num','rc_cm_num','rc_sc_code','rc_lv_code','rc_mr_num','rc_period','rc_trans_date',
                  'rc_value_date','rc_due_date','rc_pamount','rc_aamount','rc_balance','rc_pay_ref',
                  'rc_dr_cr','rc_paid','rc_status','rc_processed','rc_pay_type']
        widgets = {
            'rc_cm_num': forms.HiddenInput(),
            'rc_sc_code': forms.HiddenInput(),
            'rc_lv_code': forms.HiddenInput(),
            'rc_mr_num': forms.HiddenInput(),
            'rc_year': forms.HiddenInput(),
            'rc_term': forms.HiddenInput(),

            'rc_period': forms.HiddenInput(),
            'rc_value_date': forms.HiddenInput(),
            'rc_due_date': forms.HiddenInput(),
            'rc_pamount': forms.HiddenInput(),
            'rc_balance': forms.HiddenInput(),

            'rc_dr_cr': forms.HiddenInput(),
            'rc_paid': forms.HiddenInput(),
            'rc_status': forms.HiddenInput(),
            'rc_processed': forms.HiddenInput(),

            'rc_trans_date': widgets.DateInput(attrs={'type': 'date'}),
          }

class MemberTransForm(forms.ModelForm):
    class Meta:
        model = MemberRecord
        fields = ['mr_num','mr_cm_num','mr_year','mr_term','mr_trans_date','mr_due_date',
            'mr_aamount','mr_category']
        widgets = {
            'mr_trans_date': widgets.DateTimeInput(attrs={'type': 'date'}),
            'mr_value_date': widgets.DateTimeInput(attrs={'type': 'date'}),
            'mr_due_date'  : widgets.DateTimeInput(attrs={'type': 'date'}),
            }

# Create the authrelation form class
class AuthRelationForm(forms.ModelForm):
    # meta class
    class Meta:
        model = AuthRelation
        # specify fields to be used
        fields = ['ar_num', 'ar_cm_num', 'ar_sc_code', 'ar_sname', 'ar_fname', 'ar_nid', 'ar_phone', 'ar_email',
                  'ar_status']
        widgets = {
                    'ar_cm_num': forms.HiddenInput(),
                    'ar_sc_code': forms.HiddenInput(),
                  }

# Create the membermovement form class
class MemberMovementForm(forms.ModelForm):
    # meta class
    class Meta:
        model = MemberMovement
        # specify fields to be used
        fields = ['mm_num', 'mm_cm_num', 'mm_sc_code', 'mm_fs_num', 'mm_date', 'mm_day', 'mm_dr_ar_num', 'mm_date_dr',
                  'mm_dr_status',
                  'mm_dr_notes', 'mm_pk_ar_num', 'mm_date_pk', 'mm_pk_status', 'mm_pk_notes', 'mm_status']
        widgets = {
                    'mm_date': widgets.DateInput(attrs={'type': 'date'}),
                    'mm_date_dr': widgets.TimeInput(attrs={'type': 'time'}),
                    'mm_date_pk': widgets.TimeInput(attrs={'type': 'time'}),
                    'mm_sc_code': forms.HiddenInput(),
                    'mm_fs_num': forms.HiddenInput(),
                  }

 # Start Blog forms

 # Start Interactions Form

from django.db import models
from .models import PostCategory, PostOrigin, BlogPost, PostContribution
from django import forms

class PostCategoryForm(forms.Form):
        ct_code = models.CharField(verbose_name='Code', max_length=10,
                                   help_text='Enter code uniquely identifying post category')
        ct_desc = models.CharField(max_length=50, blank=True, null=True, help_text='The description of the category')

class PostOriginForm(forms.Form):
        po_num = models.CharField(verbose_name='Code', max_length=10,
                                  help_text='Enter code uniquely identifying originator of the post')
        po_name = models.CharField(max_length=100, blank=True, null=True, help_text='The name of the originator')
        po_position = models.CharField(max_length=50, blank=True, null=True,
                                       help_text='The position/title of the originator')

class BlogPostForm(forms.Form):
        bp_choices = (('D', 'Draft'), ('R', 'Peered'), ('P', 'Publish'))
        bp_num = models.AutoField(verbose_name='Post Number', help_text='Number uniquely identifying the post')
        bp_ct_code = models.ForeignKey(PostCategory, on_delete=models.CASCADE, verbose_name='Category',
                                       help_text='Category into which this post falls')
        bp_po_num = models.ForeignKey(PostOrigin, on_delete=models.CASCADE, verbose_name='Originator',
                                      help_text='The originator of the post')
        bp_heading = models.CharField(verbose_name='Heading', max_length=100, help_text='The heading of the post')
        bp_date = models.DateTimeField(auto_now_add=True, help_text='Date on which this post was created')
        bp_body = models.TextField(verbose_name='Message', max_length=200, help_text='The post s message')
        bp_status = models.CharField(verbose_name='Status', max_length=1, choices=bp_choices,
                                     help_text='Enter the status of the post')
        bp_file = models.FileField(upload_to='media/', verbose_name='Choose File to upload', blank=True, null=True)
        bp_image = models.ImageField(upload_to='media/', verbose_name='Choose image to upload', blank=True, null=True)

class PostContributionForm(forms.Form):
        pc_num = models.AutoField(verbose_name='Contribution Number', primary_key=True,
                                  help_text='Number uniquely identifying the contribution')
        pc_bp_num = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name='BlogPost',
                                      help_text='The of the post')
        pc_contribution = models.TextField(verbose_name='Contribution', max_length=350,
                                           help_text='The contribution to a post')

class BlogForm(forms.ModelForm):
        class Meta:
            model = BlogPost
            fields = ('bp_ct_code', 'bp_po_num', 'bp_heading', 'bp_body', 'bp_status', 'bp_file', 'bp_image')

class ContributionForm(forms.ModelForm):
        class Meta:
            model = PostContribution
            fields = ('pc_contributor', 'pc_email', 'pc_contribution')
            # 'pc_bp_num',
