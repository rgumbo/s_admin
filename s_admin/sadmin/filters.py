from django import forms
from .models import Level,Subject,SchoolClass,LevelClass,ClassMember,LevelClassInstance,Dept,StaffMember,\
    StaffSubject,Facility,FacilitySpace,SpaceSlot,Schemes,DailyPlan,ClassAssessment,LearnerAssessment,\
     MemberRegister,MemberRecord,AuthRelation,MemberMovement

import django_filters
#from decimal import Decimal
from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput

class SchoolClassFilter(django_filters.FilterSet):

    class Meta:
        model = SchoolClass
        fields = ['sc_code', 'sc_sl_code', 'sc_sf_num', 'sc_type', 'sc_desc', 'sc_status']

    def search_filter(self, queryset):
        return queryset.all() #filter(mr_gr_num=l_gr_num)

class SchemesFilter(django_filters.FilterSet):

    class Meta:
        model = Schemes
        fields = ['ch_sl_code','ch_status','ch_sf_num','ch_week','ch_sc_code','ch_sb_code']

    def search_filter(self, queryset):
        return queryset.all() #filter(mr_gr_num=l_gr_num)

class DailyPlanFilter(django_filters.FilterSet):

    class Meta:
        model = DailyPlan
        fields = ['sp_sl_code','sp_year','sp_term','sp_sc_code','sp_sb_code','sp_day','sp_cycle']

    def search_filter(self, queryset):
        return queryset.all() #filter(mr_gr_num=l_gr_num)

class ClassAssessmentFilter(django_filters.FilterSet):

    class Meta:
        model = ClassAssessment
        fields = ['as_trans_date','as_sb_code','as_ch_num','as_type']

    def search_filter(self, queryset):
        return queryset.all() #filter(mr_gr_num=l_gr_num)

class LearnerAssessmentFilter(django_filters.FilterSet):

    class Meta:
        model = LearnerAssessment
        fields = ['la_cm_num__cm_surname']

    def search_filter(self, queryset):
        return queryset.all() #filter(mr_gr_num=l_gr_num)

class MemberRegisterFilter(django_filters.FilterSet):

    class Meta:
        model = MemberRegister
        fields = ['mr_mark','mr_date','mr_sc_code', 'mr_year', 'mr_term','mr_cm_num__cm_surname']
        widgets = {
            'mr_date': widgets.DateInput(attrs={'type': 'date'}),
            #'cm_doj': widgets.DateInput(attrs={'type': 'date'}),
            #'cm_dol': widgets.DateInput(attrs={'type': 'date'}),
         }

    def search_filter(self, queryset):
        return queryset.all() #filter(mr_gr_num=l_gr_num)

class SubjectFilter(django_filters.FilterSet):

    class Meta:
        model = Subject
        fields = ['sb_code','sb_type','sb_desc']

    def search_filter(self, queryset):
        return queryset.all() #filter(mr_gr_num=l_gr_num)

class SchoolClassFilter(django_filters.FilterSet):

    class Meta:
        model = SchoolClass
        fields = ['sc_code','sc_lv_code','sc_sf_num','sc_type']

class LevelClassFilter(django_filters.FilterSet):
        class Meta:
            model = LevelClass
            fields = ['lc_sc_code', 'lc_lv_code', 'lc_sf_num', 'lc_type']

class ClassMemberFilter(django_filters.FilterSet):
    class Meta:
        model = ClassMember
        fields = ['cm_sc_code', 'cm_lv_code', 'cm_surname']

class MemberMvtFilter(django_filters.FilterSet):
    class Meta:
        model = MemberMovement
        fields = ['mm_cm_num', 'mm_date', 'mm_dr_status', 'mm_pk_status']
class LevelClassInstanceFilter(django_filters.FilterSet):
    class Meta:
        model = LevelClassInstance
        fields = ['ci_lc_num', 'ci_sc_code', 'ci_lv_code', 'ci_sb_code', 'ci_type']

class DeptFilter(django_filters.FilterSet):
    class Meta:
        model = Dept
        fields = ['dp_code', 'dp_name']

class StaffMemberFilter(django_filters.FilterSet):
    class Meta:
        model = StaffMember
        fields = ['sf_num','sf_dp_code', 'sf_surname','sf_gender','sf_app_status']

class StaffSubjectFilter(django_filters.FilterSet):
    class Meta:
        model = StaffSubject
        fields = ['ss_sf_num','ss_sb_code', 'ss_lv_code']

class FacilityFilter(django_filters.FilterSet):
    class Meta:
        model = Facility
        fields = ['fc_code','fc_name']

class FacilitySpaceFilter(django_filters.FilterSet):
    class Meta:
        model = FacilitySpace
        fields = ['fs_fc_num','fs_desc']

class SpaceSlotFilter(django_filters.FilterSet):
    class Meta:
        model = SpaceSlot
        fields = ['sp_fc_num','sp_fs_num','sp_sc_code','sp_sf_num',
                   'sp_date','sp_day','sp_start_time','sp_finish_time','sp_status']
class MembContFilter(django_filters.FilterSet):

    class Meta:
        model = MemberRecord
        fields = ['mr_year','mr_term','mr_sc_code__sc_desc','mr_cm_num__cm_fname','mr_cm_num__cm_guardian']

    def search_filter(self, queryset):
        return queryset.filter(mr_gr_num=1) #l_gr_num)
