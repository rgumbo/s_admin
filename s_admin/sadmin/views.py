from django.shortcuts import render

from .filters import SchoolClassFilter,SchemesFilter,DailyPlanFilter,ClassAssessmentFilter,\
        LearnerAssessmentFilter,MemberRegisterFilter ,MembContFilter,SubjectFilter,SchoolClassFilter,\
        StaffMemberFilter, FacilitySpaceFilter,ClassMemberFilter,SpaceSlotFilter,MemberMvtFilter

import json
from decimal import *
import datetime
from django.contrib import messages

from django.views import View, generic
from django.db.models import Sum, F,Avg, Max, Min,Count,Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.db.models.functions import Round

from django.shortcuts import render, redirect, get_object_or_404

from django.shortcuts import render, get_object_or_404

from django.views.generic import ListView, DetailView

from .models import Level,Subject,SchoolClass,LevelClass,ClassMember,LevelClassInstance,Dept,StaffMember,\
    StaffSubject,Facility,FacilitySpace,SpaceSlot,ClassAssessment,LearnerAssessment,DailyPlan,Schemes,\
    Syllabus,Currency,MemberRegister,TermParameter,ClassBilling,SubjectBilling,MemberRecord, Receipt,BlogPost\
    , PostContribution,PostCategory,PostOrigin,PostContribution,ExcludedDay,SchoolLevel,ClassSubject,\
    AuthRelation , MemberMovement

from .forms import LevelForm,SubjectForm,SchoolClassForm,LevelClassForm,ClassMemberForm,LevelClassInstanceForm\
     ,DeptForm,StaffMemberForm,StaffSubjectForm,FacilityForm,FacilitySpaceForm,SpaceSlotForm,\
     ClassAssessmentForm,LearnerAssessmentForm,DailyPlanForm,SchemesForm,SyllabusForm,CurrencyForm,\
     TermParameterForm,MemberRegisterForm,GenSchemeForm,GenRegiserForm,GenClassForm,ClassBillingForm,SubjectBillingForm,\
     MemberRecordForm, ReceiptForm,GenBillForm,ContributionForm, BlogForm,ExcludedDayForm,SchoolLevelForm,\
     GenLevelForm,GenSpaceLotForm,MemberRegister1Form,MemberRegister2Form,MemberRegister3Form,MemberRegister4Form,\
     MemberRegister5Form,MemberRegister6Form,MemberRegister7Form,MemberRegister8Form,\
     MemberRegister9Form,MemberRegister10Form,ClassSubjectForm,AuthRelationForm , MemberMovementForm,\
     GenMovementForm

# Create your views here.

global g_sb_num
g_sb_num = 0

#Index Templates

def HomePageView(Request):
    template = 'sadmin/homeindex.html'
    context = {}

    return render (Request, template, context)

def ClassHomeView(Request):
    template = 'sadmin/class_home.html'
    context = {}

    return render (Request, template, context)

def GeoHomeView(Request):
    template = 'sadmin/geo_home.html'
    context = {}

    return render (Request, template, context)

def ParaHomeView(Request):
    template = 'sadmin/para_home.html'
    context = {}

    return render (Request, template, context)

def TransHomeView(Request):
    template = 'sadmin/trans_home.html'
    context = {}

    return render (Request, template, context)

def SchoolOpsView(Request):
    template = 'sadmin/schoolops.html'
    context = {}

    return render (Request, template, context)

def TheSchoolView(Request):
    template = 'sadmin/theschool.html'
    context = {}

    return render (Request, template, context)
def InfoCentreView(Request):
    template = 'sadmin/infocentre.html'
    context = {}

    return render (Request, template, context)

def StoreReportsView(Request):
    template = 'sadmin/storereports.html'
    context = {}

    return render (Request, template, context)

def StoreParamView(Request):
    template = 'sadmin/storeparams.html'
    context = {}

    return render (Request, template, context)

def StoreTransView(Request):
    template = 'sadmin/storestrans.html'
    context = {}

    return render (Request, template, context)

# Create your views here.
def SnapShotView(request):

    # Number of subjects - Hours
    num_subject = Subject.objects.aggregate(tot_num=Count('sb_code'),tot_hrs=Sum('sb_hrs'))

    # Number of classes
    tot_class   = SchoolClass.objects.aggregate(tot_num=Count('sc_code'))

    #Number of Staff - Teaching, Non-Teaching
    tot_teach   = StaffMember.objects.filter(sf_status='1',sf_app_status='1').aggregate(tot_tch=Count('sf_num'))
    tot_wteach  = StaffMember.objects.filter(sf_status='1',sf_app_status='1',sf_gender='F').aggregate(tot_wtch=Count('sf_num'))

    tot_nteach  = StaffMember.objects.filter(sf_status='1').exclude(sf_app_status='1').aggregate(tot_ntch=Count('sf_num'))
    tot_wnteach = StaffMember.objects.filter(sf_status='1',sf_gender='F').exclude(sf_app_status='1').aggregate(tot_wntch=Count('sf_num'))

    # Number of Students
    tot_stu     = ClassMember.objects.filter(cm_status='1').aggregate(num_stu=Count('cm_num'))
    tot_fstu    = ClassMember.objects.filter(cm_status='1',cm_gender='F').aggregate(num_fstu=Count('cm_num'))

    # Number of weeks - Schemes (Done - Pending) -  Daily Plans (Done - Pending)
    tot_wks     = Schemes.objects.aggregate(num_weeks=Count('ch_num'))
    tot_pwks    = Schemes.objects.filter(ch_status='2').aggregate(num_pweeks=Count('ch_num'))

    tot_hrs     = DailyPlan.objects.filter(sp_status='0').aggregate(num_hrs=Sum('sp_hrs'))
    tot_phrs    = DailyPlan.objects.filter(sp_status='1').aggregate(num_phrs=Sum('sp_hrs'))

    tot_days     = DailyPlan.objects.filter(sp_status='0').aggregate(num_days=Count('sp_num'))
    tot_pdays    = DailyPlan.objects.filter(sp_status='1').aggregate(num_pdays=Count('sp_num'))

    # Total Days   Total Absentees
    tot_present = MemberRegister.objects.filter(mr_mark='P').aggregate(num_p=Count('mr_num'))
    tot_absent  = MemberRegister.objects.filter(mr_mark='A').aggregate(num_a=Count('mr_num'))
    tot_sick    = MemberRegister.objects.filter(mr_mark='S').aggregate(num_s=Count('mr_num'))

    # Number of Spaces (Rooms)
    tot_fac     = FacilitySpace.objects.filter(fs_status='1').aggregate(num_abs=Count('fs_num'))

    context = {
        'num_subject' : num_subject,
        'tot_class'  : tot_class,
        'tot_teach'   : tot_teach,
        'tot_wteach'  : tot_wteach,
        'tot_nteach'  : tot_nteach,
        'tot_wnteach' : tot_wnteach,
        'tot_stu'     : tot_stu,
        'tot_fstu'    : tot_fstu,
        'tot_wks'     : tot_wks,
        'tot_pwks'    : tot_pwks,
        'tot_hrs'     : tot_hrs,
        'tot_phrs'    : tot_phrs,
        'tot_days'    : tot_days,
        'tot_pdays'   : tot_pdays,
        'tot_present' : tot_present,
        'tot_absent'  : tot_absent,
        'tot_sick'    : tot_sick,
        'tot_fac'     : tot_fac,
    }
    return render(request, 'sadmin/index.html', context=context)

# home view for TermParameter. TermParameter are displayed in a list
class TermParameterIndexView(ListView):
    template_name = 'sadmin/termparameter/index.html'
    context_object_name = 'TermParameter_list'

    def get_queryset(self):
        return TermParameter.objects.all()

# Detail view (view TermParameter detail)
class TermParameterDetailView(DetailView):
    model = TermParameter
    template_name = 'sadmin/termparameter/termparameter-detail.html'

# New TermParameter view (Create new TermParameter)
def TermParameterView(request):
    if request.method == 'POST':
        form = TermParameterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('termparameter')
    form = TermParameterForm()
    return render(request, 'sadmin/termparameter/termparameter.html', {'form': form})

# Edit a TermParameter
def EditTermParameter(request, pk, template_name='sadmin/termparameter/edit.html'):
    termparameter = get_object_or_404(TermParameter, pk=pk)
    form = TermParameterForm(request.POST or None, instance=termparameter)
    if form.is_valid():
        form.save()
        return redirect('termparameter')
    return render(request, template_name, {'form': form})

# Delete TermParameter
def DeleteTermParameter(request, pk, template_name='sadmin/termparameter/confirm_delete.html'):
    termparameter = get_object_or_404(TermParameter, pk=pk)
    if request.method == 'POST':
        termparameter.delete()
        return redirect('termparameter')
    return render(request, template_name, {'object': termparameter})

# home view for ExcludedDay. ExcludedDay are displayed in a list
class ExcludedDayIndexView(ListView):
    template_name = 'sadmin/excludedday/index.html'
    context_object_name = 'ExcludedDay_list'

    def get_queryset(self):
        return ExcludedDay.objects.all()

# Detail view (view ExcludedDay detail)
class ExcludedDayDetailView(DetailView):
    model = ExcludedDay
    template_name = 'sadmin/excludedday/excludedday-detail.html'

# New ExcludedDay view (Create new ExcludedDay)
def ExcludedDayView(request):
    if request.method == 'POST':
        form = ExcludedDayForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('excludedday')
    form = ExcludedDayForm()
    return render(request, 'sadmin/excludedday/excludedday.html', {'form': form})

# Edit a ExcludedDay
def EditExcludedDay(request, pk, template_name='sadmin/excludedday/edit.html'):
    excludedday = get_object_or_404(ExcludedDay, pk=pk)
    form = ExcludedDayForm(request.POST or None, instance=excludedday)
    if form.is_valid():
        form.save()
        return redirect('excludedday')
    return render(request, template_name, {'form': form})

# Delete ExcludedDay
def DeleteExcludedDay(request, pk, template_name='sadmin/excludedday/confirm_delete.html'):
    excludedday = get_object_or_404(ExcludedDay, pk=pk)
    if request.method == 'POST':
        excludedday.delete()
        return redirect('excludedday')
    return render(request, template_name, {'object': excludedday})

#Editing Member record - Special function
def EditMemberRecordView(request,mr_num , template_name='sadmin/mrecord/edit.html'):
    memberrecord = get_object_or_404(MemberRecord, pk=mr_num)
    form = MemberRecordForm(request.POST or None, instance=memberrecord)
    if form.is_valid():
        form.save()
        return redirect('paylist')
    return render(request, template_name, {'form': form})

# home view for Currency. Currency are displayed in a list
class CurrencyIndexView(ListView):
    template_name = 'sadmin/currency/index.html'
    context_object_name = 'Currency_list'

    def get_queryset(self):
        return Currency.objects.all()

# Detail view (view Currency detail)
class CurrencyDetailView(DetailView):
    model = Currency
    template_name = 'sadmin/currency/currency-detail.html'

# New Currency view (Create new Currency)
def CurrencyView(request):
    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('currency')
    form = CurrencyForm()
    return render(request, 'sadmin/currency/currency.html', {'form': form})

# Edit a Currency
def EditCurrency(request, pk, template_name='sadmin/currency/edit.html'):
    currency = get_object_or_404(Currency, pk=pk)
    form = CurrencyForm(request.POST or None, instance=currency)
    if form.is_valid():
        form.save()
        return redirect('currency')
    return render(request, template_name, {'form': form})

# Delete Currency
def DeleteCurrency(request, pk, template_name='sadmin/currency/confirm_delete.html'):
    currency = get_object_or_404(Currency, pk=pk)
    if request.method == 'POST':
        currency.delete()
        return redirect('currency')
    return render(request, template_name, {'object': currency})

# home view for Level. Level are displayed in a list
class LevelIndexView(ListView):
    template_name = 'sadmin/level/index.html'
    context_object_name = 'Level_list'

    def get_queryset(self):
        return Level.objects.filter(lv_sl_code=self.kwargs['pk'])

class LevelListView(ListView):
    template_name = 'sadmin/level/index1.html'
    context_object_name = 'Level_list'

    def get_queryset(self):
        return Level.objects.all()

 # Detail view (view Level detail)
class LevelDetailView(DetailView):
    model = Level
    template_name = 'sadmin/level/level.detail.html'

# New Level view (Create new Level)
def LevelView1(request):
    if request.method == 'POST':
        form = LevelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('level')
    form = LevelForm()
    return render(request, 'sadmin/level/level.html', {'form': form})

def LevelView(request, pk):
    subject = Subject.objects.get(pk=pk)

    new_level = None
    if request.method == 'POST':

        form = LevelForm(data=request.POST or None)

        if form.is_valid():
            # Create a Level object but don't save to database yet
            new_level = form.save(commit=False)
            new_level.lv_sb_code = subject

            new_level.save()
            messages.success(request, "Level created successfully")
        return redirect('subject')
    else:
        form = LevelForm()
    return render(request, 'sadmin/level/level.html', {'form': form})

# Edit a Level
def EditLevel(request, pk, template_name='sadmin/level/edit.html'):
    level = get_object_or_404(Level, pk=pk)
    form = LevelForm(request.POST or None, instance=level)
    if form.is_valid():
        form.save()
        return redirect('level',pk)
    return render(request, template_name, {'form': form})

# Delete Level
def DeleteLevel(request, pk, template_name='sadmin/level/confirm_delete.html'):
    level = get_object_or_404(Level, pk=pk)
    if request.method == 'POST':
        level.delete()
        return redirect('level')
    return render(request, template_name, {'object': level})

# home view for Subject. Subject are displayed in a list
class SubjectIndexView(ListView):
    template_name = 'sadmin/Subject/index.html'
    context_object_name = 'Subject_list'

    def get_queryset(self):
        return Subject.objects.all()

# Detail view (view Subject detail)
class SubjectDetailView(DetailView):
    model = Subject
    template_name = 'sadmin/Subject/Subject-detail.html'

# New Subject view (Create new Subject)
def SubjectView(request):
    if request.method == 'POST':
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('subject')
    form = SubjectForm()
    return render(request, 'sadmin/Subject/Subject.html', {'form': form})

# Edit a Subject
def EditSubject(request, pk, template_name='sadmin/Subject/edit.html'):
    subject = get_object_or_404(Subject, pk=pk)
    form = SubjectForm(request.POST or None, instance=subject)
    if form.is_valid():
        form.save()
        return redirect('subject')
    return render(request, template_name, {'form': form})

# Delete Subject
def DeleteSubject(request, pk, template_name='sadmin/Subject/confirm_delete.html'):
    subject = get_object_or_404(Subject, pk=pk)
    if request.method == 'POST':
        Subject.delete()
        return redirect('subject')
    return render(request, template_name, {'object': subject})

# home view for Facility. Facility are displayed in a list
class FacilityIndexView(ListView):
    template_name = 'sadmin/facility/index.html'
    context_object_name = 'Facility_list'

    def get_queryset(self):
        return Facility.objects.all()

# Detail view (view Facility detail)
class FacilityDetailView(DetailView):
    model = Facility
    template_name = 'sadmin/facility/facility-detail.html'

# New Facility view (Create new Facility)
def FacilityView(request):
    if request.method == 'POST':
        form = FacilityForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('facility')
    form = FacilityForm()
    return render(request, 'sadmin/facility/facility.html', {'form': form})

# Edit a Facility
def EditFacility(request, pk, template_name='sadmin/facility/edit.html'):
    facility = get_object_or_404(Facility, pk=pk)
    form = FacilityForm(request.POST or None, instance=facility)
    if form.is_valid():
        form.save()
        return redirect('facility')
    return render(request, template_name, {'form': form})

# Delete Facility
def DeleteFacility(request, pk, template_name='sadmin/facility/confirm_delete.html'):
    facility = get_object_or_404(Facility, pk=pk)
    if request.method == 'POST':
        facility.delete()
        return redirect('facility')
    return render(request, template_name, {'object': facility})

# home view for SchoolLevel. SchoolLevel are displayed in a list
class SchoolLevelIndexView(ListView):
    template_name = 'sadmin/schoolLevel/index.html'
    context_object_name = 'SchoolLevel_list'

    def get_queryset(self):
        return SchoolLevel.objects.all()

class SchoolLevelIndexBillView(ListView):
    template_name = 'sadmin/schoollevel/index_bill.html'
    context_object_name = 'SchoolLevel_list'

    def get_queryset(self):
        return SchoolLevel.objects.all()
class SchoolLevelIndex_rView(ListView):
    template_name = 'sadmin/schoolLevel/index_r.html'
    context_object_name = 'SchoolLevel_list'

    def get_queryset(self):
        return SchoolLevel.objects.all()
# Detail view (view SchoolLevel detail)
class SchoolLevelDetailView(DetailView):
    model = SchoolLevel
    template_name = 'sadmin/schoolLevel/schoolLevel-detail.html'

# New SchoolLevel view (Create new SchoolLevel)
def SchoolLevelView(request):
    if request.method == 'POST':
        form = SchoolLevelForm(request.POST)
        if form.is_valid():
            l_sl_code = form.cleaned_data['sl_code']
            l_sl_name = form.cleaned_data['sl_name']
            form.save()
            subject = Subject.objects.all()

            for sub in subject:
                c_level = Level()

                c_level.lv_sb_code_id = sub.sb_code
                c_level.lv_name       = l_sl_name
                c_level.lv_sl_code_id = l_sl_code

                c_level.save()

        return redirect('slevel')
    form = SchoolLevelForm()
    return render(request, 'sadmin/schoollevel/SchoolLevel.html', {'form': form})

# Edit a SchoolLevel
def EditSchoolLevel(request, pk, template_name='sadmin/schoollevel/edit.html'):
    schoollevel = get_object_or_404(SchoolLevel, pk=pk)
    form = SchoolLevelForm(request.POST or None, instance=schoollevel)
    if form.is_valid():
        form.save()
        return redirect('slevel')
    return render(request, template_name, {'form': form})

# Delete SchoolLevel
def DeleteSchoolLevel(request, pk, template_name='sadmin/schoollevel/confirm_delete.html'):
    schoollevel = get_object_or_404(SchoolLevel, pk=pk)
    if request.method == 'POST':
        schoollevel.delete()
        return redirect('sLevel')
    return render(request, template_name, {'object': schoollevel})

# home view for Dept. Dept are displayed in a list
class DeptIndexView(ListView):
    template_name = 'sadmin/dept/index.html'
    context_object_name = 'Dept_list'

    def get_queryset(self):
        return Dept.objects.all()

# Detail view (view Dept detail)
class DeptDetailView(DetailView):
    model = Dept
    template_name = 'sadmin/dept/dept-detail.html'

# New Dept view (Create new Dept)
def DeptView(request):
    if request.method == 'POST':
        form = DeptForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dept')
    form = DeptForm()
    return render(request, 'sadmin/dept/dept.html', {'form': form})

# Edit a Dept
def EditDept(request, pk, template_name='sadmin/dept/edit.html'):
    dept = get_object_or_404(Dept, pk=pk)
    form = DeptForm(request.POST or None, instance=dept)
    if form.is_valid():
        form.save()
        return redirect('dept')
    return render(request, template_name, {'form': form})

# Delete Dept
def DeleteDept(request, pk, template_name='sadmin/dept/confirm_delete.html'):
    dept = get_object_or_404(Dept, pk=pk)
    if request.method == 'POST':
        dept.delete()
        return redirect('dept')
    return render(request, template_name, {'object': dept})

# home view for SchoolClass. SchoolClass are displayed in a list
class SchoolClassIndexView(ListView):
    template_name = 'sadmin/schoolclass/index.html'
    context_object_name = 'SchoolClass_list'

    def get_queryset(self):
        return SchoolClass.objects.filter(sc_sl_code=self.kwargs['pk'])

class SchoolClassRegIndexView(ListView):
    template_name = 'sadmin/schoolclass/indexreg.html'
    context_object_name = 'SchoolClass_list'

    def get_queryset(self):
        return SchoolClass.objects.all()

class SchoolClassRatesIndexView(ListView):
    template_name = 'sadmin/schoolclass/indexrates.html'
    context_object_name = 'SchoolClass_list'

    def get_queryset(self):
        return SchoolClass.objects.all()

 # Detail view (view SchoolClass detail)
class SchoolClassDetailView(DetailView):
    model = SchoolClass
    template_name = 'sadmin/schoolclass/schoolclass-detail.html'

# New SchoolClass view (Create new SchoolClass)
def SchoolClassView1(request):
    if request.method == 'POST':
        form = SchoolClassForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('schoolclass')
    form = SchoolClassForm()
    return render(request, 'sadmin/schoolclass/schoolclass.html', {'form': form})


def SchoolClassView(request, pk):
    # level = Level.objects.get(pk=pk)
    schoollevel = SchoolLevel.objects.get(pk=pk)

    new_schoolclass = None
    if request.method == 'POST':

        form = SchoolClassForm(data=request.POST or None)

        if form.is_valid():
            # Create a SchoolClass object but don't save to database yet
            new_schoolclass = form.save(commit=False)
            new_schoolclass.sc_sl_code = schoollevel

            new_schoolclass.save()

            new_sclass = SchoolClass.objects.get(pk=new_schoolclass.pk)

            subject = Subject.objects.all()

            for sub in subject:
                c_subject = ClassSubject()

                c_subject.cs_sb_code_id = sub.sb_code
                c_subject.cs_name = sub.sb_desc
                c_subject.cs_sl_code_id = schoollevel.sl_code

                c_subject.cs_lv_code_id = new_sclass.sc_lv_code
                c_subject.cs_sf_num_id = new_sclass.sc_sf_num_id
                c_subject.cs_sc_code_id = new_sclass.sc_code

                c_subject.save()

                #print(sub.sb_code, sub.sb_desc ,schoollevel.sl_code ,new_sclass.sc_code)

            messages.success(request, "SchoolClass created successfully")
        return redirect('schoolclass', pk)
    else:
        form = SchoolClassForm()
    return render(request, 'sadmin/schoolclass/schoolclass.html', {'form': form})

# Edit a SchoolClass
def EditSchoolClass(request, pk, template_name='sadmin/schoolclass/edit.html'):
    schoolclass = get_object_or_404(SchoolClass, pk=pk)
    form = SchoolClassForm(request.POST or None, instance=schoolclass)
    if form.is_valid():
        form.save()
        return redirect('schoolclass',pk)
    return render(request, template_name, {'form': form})

# Delete SchoolClass
def DeleteSchoolClass(request, pk, template_name='sadmin/schoolclass/confirm_delete.html'):
    schoolclass = get_object_or_404(SchoolClass, pk=pk)
    if request.method == 'POST':
        schoolclass.delete()
        return redirect('schoolclass')
    return render(request, template_name, {'object': schoolclass})

# home view for Class Staff Member. Staff Member  are displayed in a list
class ClassSubjectIndexView(ListView):
    template_name = 'sadmin/classsubject/index.html'
    context_object_name = 'ClassSubject_list'

    def get_queryset(self):
        return ClassSubject.objects.filter(cs_sc_code=self.kwargs['sc_code'])

# Detail view (view ClassSubject detail)
class ClassSubjectDetailView(DetailView):
    model = ClassSubject
    template_name = 'sadmin/classsubject/classsubject-detail.html'

# New ClassSubject view (Create new ClassSubject)
def ClassSubjectView(request, pk):
    schoolclass = SchoolClass.objects.get(pk=pk)

    new_classsubject = None
    if request.method == 'POST':

        form = ClassSubjectForm(data=request.POST or None)

        if form.is_valid():
            # Create a ClassSubject object but don't save to database yet
            new_classsubject = form.save(commit=False)
            new_classsubject.cs_sc_code = schoolclass

            new_classsubject.save()
            messages.success(request, "Class Subject created successfully")
        return redirect('dept')
    else:
        form = ClassSubjectForm()
    return render(request, 'sadmin/classsubject/classsubject.html', {'form': form})

# Edit a Staff Member
def EditClassSubject(request, pk, template_name='sadmin/classsubject/edit.html'):
    classsubject = get_object_or_404(ClassSubject, pk=pk)
    form = ClassSubjectForm(request.POST or None, instance=classsubject)
    if form.is_valid():
        form.save()
        return redirect('classsubject',pk)
    return render(request, template_name, {'form': form})

# Delete Staff Member
def DeleteClassSubject(request, pk, template_name='sadmin/classsubject/confirm_delete.html'):
    classsubject = get_object_or_404(ClassSubject, pk=pk)
    if request.method == 'POST':
        classsubject.delete()
        return redirect('classsubject',pk)
    return render(request, template_name, {'object': classsubject})

# home view for LevelClass. LevelClass are displayed in a list
class LevelClassIndexView(ListView):
    template_name = 'sadmin/levelclass/index.html'
    context_object_name = 'LevelClass_list'

    def get_queryset(self):
        return LevelClass.objects.filter(lc_sc_code=self.kwargs['pk'])

class LevelClassAllIndexView(ListView):
    template_name = 'sadmin/levelclass/indexall.html'
    context_object_name = 'LevelClass_list'

    def get_queryset(self):
        return LevelClass.objects.all()

class LevelClassRatesIndexView(ListView):
    template_name = 'sadmin/levelclass/indexrates.html'
    context_object_name = 'LevelClass_list'

    def get_queryset(self):
        return LevelClass.objects.all()

 # Detail view (view LevelClass detail)
class LevelClassDetailView(DetailView):
    model = LevelClass
    template_name = 'sadmin/levelclass/levelclass.detail.html'

# New LevelClass view (Create new LevelClass)
def LevelClassView1(request):
    if request.method == 'POST':
        form = LevelClassForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('levelclass')
    form = LevelClassForm()
    return render(request, 'sadmin/levelclass/levelclass.html', {'form': form})

def LevelClassView(request, pk):
    schoolclass = SchoolClass.objects.get(pk=pk)

    new_levelclass = None
    if request.method == 'POST':

        form = LevelClassForm(data=request.POST or None)

        if form.is_valid():
            # Create a LevelClass object but don't save to database yet
            new_levelclass = form.save(commit=False)
            new_levelclass.lc_sc_code = schoolclass
            new_levelclass.lc_lv_code = schoolclass.sc_lv_code
            new_levelclass.lc_sf_num = schoolclass.sc_sf_num

            new_levelclass.save()
            messages.success(request, "LevelClass created successfully")
        return redirect('schoolclass',pk)
    else:
        form = LevelClassForm()
    return render(request, 'sadmin/levelclass/levelclass.html', {'form': form})

# Edit a LevelClass
def EditLevelClass(request, pk, template_name='sadmin/levelclass/edit.html'):
    levelclass = get_object_or_404(LevelClass, pk=pk)
    form = LevelClassForm(request.POST or None, instance=levelclass)
    if form.is_valid():
        form.save()
        return redirect('levelclass',pk)
    return render(request, template_name, {'form': form})

# Delete LevelClass
def DeleteLevelClass(request, pk, template_name='sadmin/levelclass/confirm_delete.html'):
    levelclass = get_object_or_404(LevelClass, pk=pk)
    if request.method == 'POST':
        levelclass.delete()
        return redirect('levelclass')
    return render(request, template_name, {'object': levelclass})

# home view for MemberRegister. MemberRegister are displayed in a list
class MemberRegisterIndexView(ListView):
    template_name = 'sadmin/memberregister/index.html'
    context_object_name = 'MemberRegister_list'

    def get_queryset(self):
        return MemberRegister.objects.filter(mr_sc_code=self.kwargs['pk'])

 # Detail view (view MemberRegister detail)
class MemberRegisterDetailView(DetailView):
    model = MemberRegister
    template_name = 'sadmin/memberregister/memberregister.detail.html'

# New MemberRegister view (Create new MemberRegister)
def MemberRegisterView1(request):
    if request.method == 'POST':
        form = MemberRegisterForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('MemberRegister')
    form = MemberRegisterForm()
    return render(request, 'sadmin/memberregister/memberregister.html', {'form': form})

def MemberRegisterView(request, pk):
    schoolclass = SchoolClass.objects.get(pk=pk)

    new_memberregister = None
    if request.method == 'POST':

        form = MemberRegisterForm(data=request.POST or None)

        if form.is_valid():
            # Create a MemberRegister object but don't save to database yet
            new_memberregister = form.save(commit=False)
            new_memberregister.mr_sc_code = schoolclass

            new_memberregister.save()
            messages.success(request, "MemberRegister created successfully")
        return redirect('regschoolclass')
    else:
        form = MemberRegisterForm()
    return render(request, 'sadmin/memberregister/memberregister.html', {'form': form})

# Edit a MemberRegister
def EditMemberRegister(request, pk, template_name='sadmin/memberregister/edit.html'):
    memberregister = get_object_or_404(MemberRegister, pk=pk)
    form = MemberRegisterForm(request.POST or None, instance=memberregister)
    if form.is_valid():
        form.save()
        return redirect('memberregister',pk)
    return render(request, template_name, {'form': form})

# Edit a MemberRegister
def EditMemberRegister1(request, mr_num , template_name='sadmin/memberregister/edit1.html'):
    memberregister = get_object_or_404(MemberRegister, pk=mr_num)
    if g_sb_num == 1:
       form = MemberRegister1Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 2:
       form = MemberRegister2Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 3:
       form = MemberRegister3Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 4:
       form = MemberRegister4Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 5:
       form = MemberRegister5Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 6:
       form = MemberRegister6Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 7:
       form = MemberRegister7Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 8:
       form = MemberRegister8Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 9:
       form = MemberRegister9Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 10:
       form = MemberRegister10Form(request.POST or None, instance=memberregister)
    else:
       form = MemberRegisterForm(request.POST or None, instance=memberregister)

    if form.is_valid():
        form.save()
        return redirect('attendsched')
    return render(request, template_name, {'form': form})
def EditMemberRegister1(request, mr_num , template_name='sadmin/memberregister/edit1.html'):
    memberregister = get_object_or_404(MemberRegister, pk=mr_num)
    if g_sb_num == 1:
       form = MemberRegister1Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 2:
       form = MemberRegister2Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 3:
       form = MemberRegister3Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 4:
       form = MemberRegister4Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 5:
       form = MemberRegister5Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 6:
       form = MemberRegister6Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 7:
       form = MemberRegister7Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 8:
       form = MemberRegister8Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 9:
       form = MemberRegister9Form(request.POST or None, instance=memberregister)
    elif g_sb_num == 10:
       form = MemberRegister10Form(request.POST or None, instance=memberregister)
    else:
       form = MemberRegisterForm(request.POST or None, instance=memberregister)

    if form.is_valid():
        form.save()
        return redirect('attendsched')
    return render(request, template_name, {'form': form})

# Delete MemberRegister
def DeleteMemberRegister(request, pk, template_name='sadmin/memberregister/confirm_delete.html'):
    memberregister = get_object_or_404(MemberRegister, pk=pk)
    if request.method == 'POST':
        memberregister.delete()
        return redirect('memberregister')
    return render(request, template_name, {'object': memberregister})

# home view for Class Member. ClassMember  are displayed in a list
class ClassMemberIndexView(ListView):
    template_name = 'sadmin/classmember/index.html'
    context_object_name = 'ClassMember_list'

    def get_queryset(self):
        return ClassMember.objects.filter(cm_sc_code=self.kwargs['pk'])

# Detail view (view ClassMember detail)
class ClassMemberDetailView(DetailView):
    model = ClassMember
    template_name = 'sadmin/classmember/classmember-detail.html'

# New ClassMember view (Create new ClassMember)
def ClassMemberView1(request):
    if request.method == 'POST':
        form = ClassMemberForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('classmember')
    form = ClassMemberForm()
    return render(request, 'sadmin/classmember/authrelation.html', {'form': form})

def ClassMemberView(request, pk):
    schoolclass = SchoolClass.objects.get(pk=pk)

    new_classmember = None
    if request.method == 'POST':

        form = ClassMemberForm(data=request.POST or None)

        if form.is_valid():
            # Create a ClassMember object but don't save to database yet
            new_classmember = form.save(commit=False)
            new_classmember.cm_sc_code = schoolclass
            new_classmember.cm_lv_code = schoolclass.sc_lv_code

            new_classmember.save()
            messages.success(request, "ClassMember created successfully")
        return redirect('schoolclass',pk)
    else:
        form = ClassMemberForm()
    return render(request, 'sadmin/classmember/authrelation.html', {'form': form})
def CreateStudentView(request, pk):
    schoolclass = SchoolClass.objects.get(pk=pk)

    new_classmember = None
    if request.method == 'POST':

        form = ClassMemberForm(data=request.POST or None)

        if form.is_valid():
            # Create a ClassMember object but don't save to database yet
            new_classmember = form.save(commit=False)
            new_classmember.cm_sc_code = schoolclass
            new_classmember.cm_lv_code = schoolclass.sc_lv_code

            new_classmember.save()
            messages.success(request, "ClassMember created successfully")
        return redirect('classlist')
    else:
        form = ClassMemberForm()
    return render(request, 'sadmin/classmember/authrelation.html', {'form': form})

# Edit a ClassMember
def EditClassMember(request, pk, template_name='sadmin/classmember/edit.html'):
    classmember = get_object_or_404(ClassMember, pk=pk)
    form = ClassMemberForm(request.POST or None, instance=classmember)
    if form.is_valid():
        form.save()
        return redirect('classmember',pk)
    return render(request, template_name, {'form': form})

def EditStudent(request, cm_num, template_name='sadmin/classmember/edit.html'):
    classmember = get_object_or_404(ClassMember, cm_num=cm_num)
    form = ClassMemberForm(request.POST or None, instance=classmember)
    sc_code = classmember.cm_sc_code

    if form.is_valid():
        form.save()
        return redirect('students',sc_code)
    return render(request, template_name, {'form': form})

def EditClassMember1(request, mr_cm_num, template_name='sadmin/classmember/edit.html'):
    classmember = get_object_or_404(ClassMember, pk=mr_cm_num)
    form = ClassMemberForm(request.POST or None, instance=classmember)
    if form.is_valid():
        form.save()
        return redirect('classmember',mr_cm_num)
    return render(request, template_name, {'form': form})

# Delete ClassMember
def DeleteClassMember(request, pk, template_name='sadmin/ClassMember/confirm_delete.html'):
    classmember = get_object_or_404(ClassMember, pk=pk)
    if request.method == 'POST':
        classmember.delete()
        return redirect('classmember')
    return render(request, template_name, {'object': classmember})

# home view for LevelClassInstance. LevelClassInstance  are displayed in a list
class LevelClassInstanceIndexView(ListView):
    template_name = 'sadmin/LevelClassInstance/index.html'
    context_object_name = 'LevelClassInstance_list'

    def get_queryset(self):
        return LevelClassInstance.objects.filter(dt_to_code=self.kwargs['pk'])

# Detail view (view LevelClassInstance detail)
class LevelClassInstanceDetailView(DetailView):
    model = LevelClassInstance
    template_name = 'sadmin/LevelClassInstance/LevelClassInstance-detail.html'

# New LevelClassInstance view (Create new LevelClassInstance)
def LevelClassInstanceView1(request):
    if request.method == 'POST':
        form = LevelClassInstanceForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('levelclassinstance')
    form = LevelClassInstanceForm()
    return render(request, 'sadmin/LevelClassInstance/LevelClassInstance.html', {'form': form})

def LevelClassInstanceView(request, pk):
    #town = Town.objects.get(pk=pk)
    #staffmember = Region.objects.get(pk=town.to_rg_code_id)
    #dept = Country.objects.get(pk=staffmember.rg_co_code_id)

    new_LevelClassInstance = None
    if request.method == 'POST':

        form = LevelClassInstanceForm(data=request.POST or None)

        if form.is_valid():
            # Create a LevelClassInstance object but don't save to database yet
            new_levelclassinstance = form.save(commit=False)
            #new_LevelClassInstance.dt_to_code = town
            #new_LevelClassInstance.dt_rg_code = town.to_rg_code
            #new_LevelClassInstance.dt_co_code = dept

            new_levelclassinstance.save()
            messages.success(request, "LevelClassInstance created successfully")
        return redirect('town',pk)
    else:
        form = LevelClassInstanceForm()
    return render(request, 'sadmin/LevelClassInstance/LevelClassInstance.html', {'form': form})

# Edit a LevelClassInstance
def EditLevelClassInstance(request, pk, template_name='sadmin/LevelClassInstance/edit.html'):
    levelclassinstance = get_object_or_404(LevelClassInstance, pk=pk)
    form = LevelClassInstanceForm(request.POST or None, instance=levelclassinstance)
    if form.is_valid():
        form.save()
        return redirect('levelclassinstance',pk)
    return render(request, template_name, {'form': form})

# Delete LevelClassInstance
def DeleteLevelClassInstance(request, pk, template_name='sadmin/LevelClassInstance/confirm_delete.html'):
    levelclassinstance = get_object_or_404(LevelClassInstance, pk=pk)
    if request.method == 'POST':
        levelclassinstance.delete()
        return redirect('levelclassinstance')
    return render(request, template_name, {'object': levelclassinstance})

# home view for Syllabus. Syllabus are displayed in a list
class SyllabusIndexView(ListView):
    template_name = 'sadmin/syllabus/index.html'
    context_object_name = 'Syllabus_list'

    def get_queryset(self):
        return Syllabus.objects.all()

# Detail view (view Syllabus detail)
class SyllabusDetailView(DetailView):
    model = Syllabus
    template_name = 'sadmin/syllabus/syllabus-detail.html'

# New Syllabus view (Create new Syllabus)
def SyllabusView(request):
    if request.method == 'POST':
        form = SyllabusForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('syllabus')
    form = SyllabusForm()
    return render(request, 'sadmin/syllabus/syllabus.html', {'form': form})

# Edit a Syllabus
def EditSyllabus(request, pk, template_name='sadmin/syllabus/edit.html'):
    syllabus = get_object_or_404(Syllabus, pk=pk)
    form = SyllabusForm(request.POST or None, instance=syllabus)
    if form.is_valid():
        form.save()
        return redirect('syllabus')
    return render(request, template_name, {'form': form})

# Delete Syllabus
def DeleteSyllabus(request, pk, template_name='sadmin/syllabus/confirm_delete.html'):
    syllabus = get_object_or_404(Syllabus, pk=pk)
    if request.method == 'POST':
        syllabus.delete()
        return redirect('syllabus')
    return render(request, template_name, {'object': syllabus})

# home view for Schemes. Schemes are displayed in a list
class SchemesIndexView(ListView):
    template_name = 'sadmin/schemes/index.html'
    context_object_name = 'Schemes_list'

    def get_queryset(self):
        return Schemes.objects.filter(ch_sy_code=self.kwargs['pk'])

class SchemesIndexView1(ListView):
    template_name = 'sadmin/schemes/index.html'
    context_object_name = 'Schemes_list'

    def get_queryset(self):
        return Schemes.objects.filter(ch_num=self.kwargs['pk'])

# Detail view (view Schemes detail)
class SchemesDetailView(DetailView):
    model = Schemes
    template_name = 'sadmin/schemes/schemes-detail.html'

# New Schemes view (Create new Schemes)
def SchemesView1(request):
    if request.method == 'POST':
        form = SchemesForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('schemes')
    form = SchemesForm()
    return render(request, 'sadmin/schemes/schemes.html', {'form': form})

def SchemesView(request, pk):
    syllabus = Syllabus.objects.get(pk=pk)
    #staffmember = Region.objects.get(pk=town.to_rg_code_id)
    #dept = Country.objects.get(pk=staffmember.rg_co_code_id)

    new_schemes = None
    if request.method == 'POST':

        form = SchemesForm(data=request.POST or None)

        if form.is_valid():
            # Create a Schemes object but don't save to database yet
            new_schemes = form.save(commit=False)
            new_schemes.ch_lc_num = syllabus
            #new_Schemes.dt_rg_code = town.to_rg_code
            #new_Schemes.dt_co_code = country

            new_schemes.save()
            messages.success(request, "Schemes created successfully")
        return redirect('classlevel',pk)
    else:
        form = SchemesForm()
    return render(request, 'sadmin/schemes/schemes.html', {'form': form})

def ChSchemesView(request, pk):
    levelclass = LevelClass.objects.get(pk=pk)

    new_schemes = None
    if request.method == 'POST':

        form = SchemesForm(data=request.POST or None)

        if form.is_valid():
            # Create a Schemes object but don't save to database yet
            new_schemes = form.save(commit=False)
            new_schemes.ch_lc_num = levelclass
            new_schemes.ch_sc_code = levelclass.lc_sc_code
            new_schemes.ch_lv_code = levelclass.lc_lv_code
            new_schemes.ch_sb_code = levelclass.lc_sb_code
            new_schemes.ch_sf_num = levelclass.lc_sf_num

            new_schemes.save()
            messages.success(request, "Schemes created successfully")
        return redirect('classlevel',pk)
    else:
        form = SchemesForm()
    return render(request, 'sadmin/schemes/schemes.html', {'form': form})

def SubSchemesView(request, lc_sb_code):
    subject = Subject.objects.get(sb_code=lc_sb_code)
    #staffmember = Region.objects.get(pk=town.to_rg_code_id)
    #dept = Country.objects.get(pk=staffmember.rg_co_code_id)

    new_schemes = None
    if request.method == 'POST':

        form = SchemesForm(data=request.POST or None)

        if form.is_valid():
            # Create a Schemes object but don't save to database yet
            new_schemes = form.save(commit=False)
            new_schemes.ch_sb_code = subject
            #new_Schemes.dt_rg_code = town.to_rg_code
            #new_Schemes.dt_co_code = country

            new_schemes.save()
            messages.success(request, "Schemes created successfully")
        return redirect('subject',lc_sb_code)
    else:
        form = SchemesForm()
    return render(request, 'sadmin/schemes/schemes.html', {'form': form})

# Edit a Schemes
def EditSchemes(request, pk, template_name='sadmin/schemes/edit.html'):
    schemes = get_object_or_404(Schemes, pk=pk)
    form = SchemesForm(request.POST or None, instance=schemes)
    if form.is_valid():
        form.save()
        return redirect('schemes',pk)
    return render(request, template_name, {'form': form})

# Delete Schemes
def DeleteSchemes(request, pk, template_name='sadmin/schemes/confirm_delete.html'):
    schemes = get_object_or_404(Schemes, pk=pk)
    if request.method == 'POST':
        schemes.delete()
        return redirect('schemes')
    return render(request, template_name, {'object': schemes})

# home view for DailyPlan. DailyPlan are displayed in a list
class DailyPlanIndexView(ListView):
    template_name = 'sadmin/dailyplan/index.html'
    context_object_name = 'DailyPlan_list'

    def get_queryset(self):
        return DailyPlan.objects.filter(sp_ch_num=self.kwargs['pk'])

 # Detail view (view DailyPlan detail)
class DailyPlanDetailView(DetailView):
    model = DailyPlan
    template_name = 'sadmin/dailyplan/dailyplan-detail.html'

# New DailyPlan view (Create new DailyPlan)
def DailyPlanView1(request):
    if request.method == 'POST':
        form = DailyPlanForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('dailyplan')
    form = DailyPlanForm()
    return render(request, 'sadmin/dailyplan/dailyplan.html', {'form': form})

def DailyPlanView(request, pk):
    schemes = Schemes.objects.get(pk=pk)

    new_dailyplan = None
    if request.method == 'POST':

        form = DailyPlanForm(data=request.POST or None)

        if form.is_valid():
            # Create a DailyPlan object but don't save to database yet
            new_dailyplan = form.save(commit=False)
            new_dailyplan.sp_ch_num = schemes
            new_dailyplan.sp_sc_code = schemes.sp_ch_num
            new_dailyplan.sp_lv_code = schemes.sp_lc_num
            new_dailyplan.sp_sb_code = schemes.sp_sc_code
            new_dailyplan.sp_sf_num = schemes.sp_sb_code

            new_dailyplan.save()
            messages.success(request, "DailyPlan created successfully")
        return redirect('schemes',pk)
    else:
        form = DailyPlanForm()
    return render(request, 'sadmin/dailyplan/dailyplan.html', {'form': form})

# Edit a DailyPlan
def EditDailyPlan(request, pk, template_name='sadmin/dailyplan/edit.html'):
    dailyplan = get_object_or_404(DailyPlan, pk=pk)
    form = DailyPlanForm(request.POST or None, instance=dailyplan)
    if form.is_valid():
        form.save()
        return redirect('dailyplan',pk)
    return render(request, template_name, {'form': form})

# Delete DailyPlan
def DeleteDailyPlan(request, pk, template_name='sadmin/dailyplan/confirm_delete.html'):
    dailyplan = get_object_or_404(DailyPlan, pk=pk)
    if request.method == 'POST':
        dailyplan.delete()
        return redirect('dailyplan')
    return render(request, template_name, {'object': dailyplan})

# home view for ClassAssessment. ClassAssessment  are displayed in a list
class ClassAssessmentIndexView(ListView):
    template_name = 'sadmin/classassessment/index.html'
    context_object_name = 'ClassAssessment_list'

    def get_queryset(self):
        return ClassAssessment.objects.filter(as_ch_num=self.kwargs['pk'])

# Detail view (view ClassAssessment detail)
class ClassAssessmentDetailView(DetailView):
    model = ClassAssessment
    template_name = 'sadmin/classassessment/classassessment-detail.html'

# New ClassAssessment view (Create new ClassAssessment)
def ClassAssessmentView1(request):
    if request.method == 'POST':
        form = ClassAssessmentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('classassessment')
    form = ClassAssessmentForm()
    return render(request, 'sadmin/classassessment/subjectbilling.html', {'form': form})

def ClassAssessmentView(request, pk):
    scheme = Schemes.objects.get(pk=pk)
    #staffmember = Region.objects.get(pk=town.to_rg_code_id)
    #dept = Country.objects.get(pk=staffmember.rg_co_code_id)

    new_classassessment = None
    if request.method == 'POST':

        form = ClassAssessmentForm(data=request.POST or None)

        if form.is_valid():
            # Create a ClassAssessment object but don't save to database yet
            new_classassessment = form.save(commit=False)
            new_classassessment.as_ch_num = scheme
            #new_classassessment.as_lc_num = scheme.ch_lc_num
            new_classassessment.as_sc_code = scheme.ch_sc_code
            new_classassessment.as_sb_code = scheme.ch_sb_code

            new_classassessment.save()
            messages.success(request, "ClassAssessment created successfully")
        return redirect('chscheme',pk)
    else:
        form = ClassAssessmentForm()
    return render(request, 'sadmin/classassessment/classassessment.html', {'form': form})

# Edit a ClassAssessment
def EditClassAssessment(request, pk, template_name='sadmin/classassessment/edit.html'):
    classassessment = get_object_or_404(ClassAssessment, pk=pk)
    form = ClassAssessmentForm(request.POST or None, instance=classassessment)
    if form.is_valid():
        form.save()
        return redirect('classassessment',pk)
    return render(request, template_name, {'form': form})

# Delete ClassAssessment
def DeleteClassAssessment(request, pk, template_name='sadmin/classassessment/confirm_delete.html'):
    classassessment = get_object_or_404(ClassAssessment, pk=pk)
    if request.method == 'POST':
        classassessment.delete()
        return redirect('classassessment')
    return render(request, template_name, {'object': classassessment})

# home view for LearnerAssessment. LearnerAssessment  are displayed in a list
class LearnerAssessmentIndexView(ListView):
    template_name = 'sadmin/learnerassessment/index.html'
    context_object_name = 'LearnerAssessment_list'

    def get_queryset(self):
        return LearnerAssessment.objects.filter(la_as_num=self.kwargs['pk'])

# Detail view (view LearnerAssessment detail)
class LearnerAssessmentDetailView(DetailView):
    model = LearnerAssessment
    template_name = 'sadmin/learnerassessment/learnerassessment-detail.html'

# New LearnerAssessment view (Create new LearnerAssessment)
def LearnerAssessmentView1(request):
    if request.method == 'POST':
        form = LearnerAssessmentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('learnerassessment')
    form = LearnerAssessmentForm()
    return render(request, 'sadmin/learnerassessment/learnerassessment.html', {'form': form})

def LearnerAssessmentView(request, pk):
    classassessment = ClassAssessment.objects.get(pk=pk)
    #staffmember = Region.objects.get(pk=town.to_rg_code_id)
    #dept = Country.objects.get(pk=staffmember.rg_co_code_id)

    new_learnerassessment = None
    if request.method == 'POST':

        form = LearnerAssessmentForm(data=request.POST or None)

        if form.is_valid():
            # Create a LearnerAssessment object but don't save to database yet -
            new_learnerassessment = form.save(commit=False)
            new_learnerassessment.la_as_num = classassessment
            new_learnerassessment.la_sc_code = classassessment.as_sc_code
            #new_learnerassessment.la_lc_num = classassessment.as_lc_num
            #new_learnerassessment.la_cm_num = classassessment.as_cm_num
            new_learnerassessment.la_sb_code = classassessment.as_sb_code

            new_learnerassessment.save()
            messages.success(request, "LearnerAssessment created successfully")
        return redirect('classassessment',pk)
    else:
        form = LearnerAssessmentForm()
    return render(request, 'sadmin/learnerassessment/learnerassessment.html', {'form': form})

# Edit a LearnerAssessment
def EditLearnerAssessment(request, pk, template_name='sadmin/learnerassessment/edit.html'):
    learnerassessment = get_object_or_404(LearnerAssessment, pk=pk)
    form = LearnerAssessmentForm(request.POST or None, instance=learnerassessment)
    if form.is_valid():
        form.save()
        return redirect('learnerassessment',pk)
    return render(request, template_name, {'form': form})

# Delete LearnerAssessment
def DeleteLearnerAssessment(request, pk, template_name='sadmin/learnerassessment/confirm_delete.html'):
    learnerassessment = get_object_or_404(LearnerAssessment, pk=pk)
    if request.method == 'POST':
        learnerassessment.delete()
        return redirect('learnerassessment')
    return render(request, template_name, {'object': learnerassessment})

# home view for Class Staff Member. Staff Member  are displayed in a list
class StaffMemberIndexView(ListView):
    template_name = 'sadmin/StaffMember/index.html'
    context_object_name = 'StaffMember_list'

    def get_queryset(self):
        return StaffMember.objects.filter(sf_dp_code=self.kwargs['pk'])

# Detail view (view StaffMember detail)
class StaffMemberDetailView(DetailView):
    model = StaffMember
    template_name = 'sadmin/StaffMember/StaffMember-detail.html'

# New StaffMember view (Create new StaffMember)
def StaffMemberView1(request):
    if request.method == 'POST':
        form = StaffMemberForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('staffmember')
    form = StaffMemberForm()
    return render(request, 'sadmin/StaffMember/StaffMember.html', {'form': form})

def StaffMemberView(request, pk):
    dept = Dept.objects.get(pk=pk)

    new_staffmember = None
    if request.method == 'POST':

        form = StaffMemberForm(data=request.POST or None)

        if form.is_valid():
            # Create a StaffMember object but don't save to database yet
            new_staffmember = form.save(commit=False)
            new_staffmember.sf_dp_code = dept

            new_staffmember.save()
            messages.success(request, "Staff Member created successfully")
        return redirect('dept')
    else:
        form = StaffMemberForm()
    return render(request, 'sadmin/StaffMember/StaffMember.html', {'form': form})

# Edit a Staff Member
def EditStaffMember(request, pk, template_name='sadmin/StaffMember/edit.html'):
    staffmember = get_object_or_404(StaffMember, pk=pk)
    form = StaffMemberForm(request.POST or None, instance=staffmember)
    if form.is_valid():
        form.save()
        return redirect('staffmember',pk)
    return render(request, template_name, {'form': form})

# Delete Staff Member
def DeleteStaffMember(request, pk, template_name='sadmin/StaffMember/confirm_delete.html'):
    staffmember = get_object_or_404(StaffMember, pk=pk)
    if request.method == 'POST':
        staffmember.delete()
        return redirect('staffmember')
    return render(request, template_name, {'object': staffmember})

# home view for Facility Space. Facility Space  are displayed in a list
class FacilitySpaceIndexView(ListView):
    template_name = 'sadmin/facilityspace/index.html'
    context_object_name = 'FacilitySpace_list'

    def get_queryset(self):
        return FacilitySpace.objects.filter(fs_fc_num=self.kwargs['pk'])

# Detail view (view Facility Space detail)
class FacilitySpaceDetailView(DetailView):
    model = FacilitySpace
    template_name = 'sadmin/facilityspace/facilityspace-detail.html'

# New Facility Space view (Create new FacilitySpace)
def FacilitySpaceView1(request):
    if request.method == 'POST':
        form = FacilitySpaceForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('facilityspace')
    form = FacilitySpaceForm()
    return render(request, 'sadmin/facilityspace/facilityspace.html', {'form': form})

def FacilitySpaceView(request, pk):
    facility = Facility.objects.get(pk=pk)
    new_facilityspace = None
    if request.method == 'POST':

        form = FacilitySpaceForm(data=request.POST or None)

        if form.is_valid():
            # Create a FacilitySpace object but don't save to database yet
            new_facilityspace = form.save(commit=False)
            new_facilityspace.fs_fc_num = facility

            new_facilityspace.save()
            messages.success(request, "Facility Space created successfully")
        return redirect('facility')
    else:
        form = FacilitySpaceForm()
    return render(request, 'sadmin/facilityspace/facilityspace.html', {'form': form})

# Edit a Facility Space
def EditFacilitySpace(request, pk, template_name='sadmin/facilityspace/edit.html'):
    facilityspace = get_object_or_404(FacilitySpace, pk=pk)
    form = FacilitySpaceForm(request.POST or None, instance=facilityspace)
    if form.is_valid():
        form.save()
        return redirect('facilityspace',pk)
    return render(request, template_name, {'form': form})

# Delete Facility Space
def DeleteFacilitySpace(request, pk, template_name='sadmin/facilityspace/confirm_delete.html'):
    facilityspace = get_object_or_404(FacilitySpace, pk=pk)
    if request.method == 'POST':
        facilityspace.delete()
        return redirect('facilityspace')
    return render(request, template_name, {'object': facilityspace})

# home view for Class Member. Staff Subject  are displayed in a list
class StaffSubjectIndexView(ListView):
    template_name = 'sadmin/StaffSubject/index.html'
    context_object_name = 'StaffSubject_list'

    def get_queryset(self):
        return StaffSubject.objects.filter(ss_sf_num=self.kwargs['pk'])

# Detail view (view Staff Subject detail)
class StaffSubjectDetailView(DetailView):
    model = StaffSubject
    template_name = 'sadmin/StaffSubject/StaffSubject-detail.html'

# New Staff Subject view (Create new Staff Subject)
def StaffSubjectView1(request):
    if request.method == 'POST':
        form = StaffSubjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('staffsubject')
    form = StaffSubjectForm()
    return render(request, 'sadmin/StaffSubject/StaffSubject.html', {'form': form})

def StaffSubjectView(request, pk):
    staffmember = StaffMember.objects.get(pk=pk)

    new_staffsubject = None
    if request.method == 'POST':

        form = StaffSubjectForm(data=request.POST or None)

        if form.is_valid():
            # Create a Staff Subject object but don't save to database yet
            new_staffsubject = form.save(commit=False)
            new_staffsubject.ss_sf_num = staffmember

            new_staffsubject.save()
            messages.success(request, "Staff Subject created successfully")
        return redirect('staffmember',pk)
    else:
        form = StaffSubjectForm()
    return render(request, 'sadmin/StaffSubject/StaffSubject.html', {'form': form})

# Edit a Staff Subject
def EditStaffSubject(request, pk, template_name='sadmin/StaffSubject/edit.html'):
    staffsubject = get_object_or_404(StaffSubject, pk=pk)
    form = StaffSubjectForm(request.POST or None, instance=staffsubject)
    if form.is_valid():
        form.save()
        return redirect('staffsubject',pk)
    return render(request, template_name, {'form': form})

# Delete Staff Subject
def DeleteStaffSubject(request, pk, template_name='sadmin/StaffSubject/confirm_delete.html'):
    staffsubject = get_object_or_404(StaffSubject, pk=pk)
    if request.method == 'POST':
        staffsubject.delete()
        return redirect('staffsubject')
    return render(request, template_name, {'object': staffsubject})

# home view for Space Slot. Space Slot are displayed in a list
class SpaceSlotIndexView(ListView):
    template_name = 'sadmin/spaceslot/index.html'
    context_object_name = 'SpaceSlot_list'

    def get_queryset(self):
        return SpaceSlot.objects.filter(sp_fs_num=self.kwargs['pk'])

# Detail view (view Staff Subject detail)
class SpaceSlotDetailView(DetailView):
    model = SpaceSlot
    template_name = 'sadmin/spaceslot/spaceslot-detail.html'

# New Staff Subject view (Create new Staff Subject)
def SpaceSlotView1(request):
    if request.method == 'POST':
        form = SpaceSlotForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('spaceslot')
    form = SpaceSlotForm()
    return render(request, 'sadmin/spaceslot/slotlist.html', {'form': form})

def SpaceSlotView(request, pk):
    facilityspace = FacilitySpace.objects.get(pk=pk)

    new_spaceslot = None
    if request.method == 'POST':

        form = SpaceSlotForm(data=request.POST or None)

        if form.is_valid():
            # Create a Staff Subject object but don't save to database yet
            new_spaceslot = form.save(commit=False)
            new_spaceslot.sp_fs_num = facilityspace

            new_spaceslot.save()
            messages.success(request, "Space Slot created successfully")
        return redirect('facilityspace',pk)
    else:
        form = SpaceSlotForm()
    return render(request, 'sadmin/spaceslot/slotlist.html', {'form': form})

# Edit a Space Slot
def EditSpaceSlot(request, pk, template_name='sadmin/spaceslot/edit.html'):
    spaceslot = get_object_or_404(SpaceSlot, pk=pk)
    form = SpaceSlotForm(request.POST or None, instance=spaceslot)
    if form.is_valid():
        form.save()
        return redirect('spaceslot',pk)
    return render(request, template_name, {'form': form})

# Delete Space Slot
def DeleteSpaceSlot(request, pk, template_name='sadmin/spaceslot/confirm_delete.html'):
    spaceslot = get_object_or_404(SpaceSlot, pk=pk)
    if request.method == 'POST':
        spaceslot.delete()
        return redirect('spaceslot')
    return render(request, template_name, {'object': spaceslot})

# Billing Views

class ClassBillingIndexView(ListView):
    template_name = 'sadmin/billing/cbindex.html'
    context_object_name = 'ClassBilling_list'

    def get_queryset(self):
        return ClassBilling.objects.filter(cb_sl_code =self.kwargs['pk'])

def ClassBillingView(request, pk):
        schoollevel = SchoolLevel.objects.get(pk=pk)
        schoolclass = SchoolClass.objects.get(sc_sl_code=pk)
        termparams = TermParameter.objects.get(tp_billed='N')

        new_classbilling = None
        if request.method == 'POST':

            form = ClassBillingForm(data=request.POST or None)

            if form.is_valid():
                # Create a Class Billing Instance object but don't save to database yet
                new_classbilling = form.save(commit=False)

                new_classbilling.cb_sl_code = schoollevel
                new_classbilling.cb_sc_code = schoolclass
                new_classbilling.cb_year = termparams.tp_year
                new_classbilling.cb_term = termparams.tp_term

                new_classbilling.save()
                messages.success(request, "Billing head object created successfully")
            return redirect('schlevelrates')
        else:
            form = ClassBillingForm()
        return render(request, 'sadmin/billing/classbilling.html', {'form': form})

class SubjectBillingIndexView(ListView):
    template_name = 'sadmin/billing/sbindex.html'
    context_object_name = 'SubjectBilling_list'

    def get_queryset(self):
        return SubjectBilling.objects.filter(jb_sc_code=self.kwargs['pk'])

def SubjectBillingView(request, pk):
    schoolclass = SchoolClass.objects.get(pk=pk)
    termparams = TermParameter.objects.get(tp_billed='N')

    new_subjectbilling = None
    if request.method == 'POST':

        form = SubjectBillingForm(data=request.POST or None)

        if form.is_valid():
            # Create a Subject Billing Instance object but don't save to database yet
            new_subjectbilling = form.save(commit=False)

            new_subjectbilling.jb_sc_code = schoolclass
            new_subjectbilling.jb_sl_code = schoolclass.sc_sl_code
            new_subjectbilling.jb_lv_code = schoolclass.sc_lv_code
            new_subjectbilling.jb_year = termparams.tp_year
            new_subjectbilling.jb_term = termparams.tp_term

            new_subjectbilling.save()
            messages.success(request, "Subject Billing head object created successfully")
        return redirect('rateslevelclass')
    else:
        form = SubjectBillingForm()
    return render(request, 'sadmin/billing/subjectbilling.html', {'form': form})

# home view for MemberMovement. MemberMovement are displayed in a list
class MemberMovementIndexView(ListView):
    template_name = 'sadmin/membermovement/index.html'
    context_object_name = 'MemberMovement_list'

    def get_queryset(self):
        return MemberMovement.objects.filter(mm_cm_num=self.kwargs['pk'])

 # Detail view (view MemberMovement detail)
class MemberMovementDetailView(DetailView):
    model = MemberMovement
    template_name = 'sadmin/membermovement/membermovement.detail.html'

def MemberMovementView(request, pk):
    classmember = ClassMember.objects.get(pk=pk)

    new_membermovement = None
    if request.method == 'POST':

        form = MemberMovementForm(data=request.POST or None)

        if form.is_valid():
            # Create a MemberMovement object but don't save to database yet
            new_membermovement = form.save(commit=False)
            new_membermovement.mm_cm_num  = classmember
            new_membermovement.mm_sc_code = classmember.cm_sc_code

            new_membermovement.save()

            messages.success(request, "Member Movement created successfully")
        return redirect('classmember',pk)
    else:
        form = MemberMovementForm()
    return render(request, 'sadmin/membermovement/membermovement.html', {'form': form})

# Edit a MemberMovement
def EditMemberMovement(request, pk, template_name='sadmin/membermovement/edit.html'):
    membermovement = get_object_or_404(MemberMovement, pk=pk)
    form = MemberMovementForm(request.POST or None, instance=membermovement)
    if form.is_valid():
        form.save()
        return redirect('membermovement',pk)
    return render(request, template_name, {'form': form})

# Delete MemberMovement
def DeleteMemberMovement(request, pk, template_name='sadmin/membermovement/confirm_delete.html'):
    membermovement = get_object_or_404(MemberMovement, pk=pk)
    if request.method == 'POST':
        membermovement.delete()
        return redirect('membermovement')
    return render(request, template_name, {'object': membermovement})

# home view for AuthRelation. AuthRelation are displayed in a list
class AuthRelationIndexView(ListView):
    template_name = 'sadmin/authrelation/index.html'
    context_object_name = 'AuthRelation_list'

    def get_queryset(self):
        return AuthRelation.objects.filter(ar_cm_num=self.kwargs['pk'])

 # Detail view (view AuthRelation detail)
class AuthRelationDetailView(DetailView):
    model = AuthRelation
    template_name = 'sadmin/authrelation/authrelation.detail.html'

 # New Authorized relation object

def AuthRelationView(request, cm_num):
    classmember = ClassMember.objects.get(cm_num=cm_num)
    #l_sc_code = 0

    new_authrelation = None
    if request.method == 'POST':

        form = AuthRelationForm(data=request.POST or None)

        if form.is_valid():
            # Create a AuthRelation object but don't save to database yet
            new_authrelation = form.save(commit=False)
            new_authrelation.ar_cm_num  = classmember
            new_authrelation.ar_sc_code = classmember.cm_sc_code
            l_cm_num = classmember.cm_num
            l_sc_code = classmember.cm_sc_code
            print(l_cm_num,l_sc_code)

            new_authrelation.save()

            messages.success(request, "Authorized relation created successfully")
        return redirect('students',cm_num)
    else:
        form = AuthRelationForm()
    return render(request, 'sadmin/authrelation/authrelation.html', {'form': form})

# Edit a AuthRelation
def EditAuthRelation(request, pk, template_name='sadmin/authrelation/edit.html'):
    authrelation = get_object_or_404(AuthRelation, pk=pk)
    form = AuthRelationForm(request.POST or None, instance=authrelation)
    if form.is_valid():
        form.save()
        return redirect('authrelation',pk)
    return render(request, template_name, {'form': form})

# Delete AuthRelation
def DeleteAuthRelation(request, pk, template_name='sadmin/authrelation/confirm_delete.html'):
    authrelation = get_object_or_404(AuthRelation, pk=pk)
    if request.method == 'POST':
        authrelation.delete()
        return redirect('authrelation')
    return render(request, template_name, {'object': authrelation})

def ClassListView(request):

    dataset = SchoolClass.objects.values('sc_code','sc_lv_code__lv_name','sc_sf_num__sf_surname','sc_type','sc_desc','sc_status').\
        annotate(num_of=Sum('sc_code')).order_by('sc_code')

    sc_class = SchoolClassFilter(request.GET, queryset=dataset)
    total_num = sc_class.qs.aggregate(TotNum=Sum('num_of'))

    context = {'filter': sc_class,'total_num': total_num}

    return render(request, 'sadmin/reports/class_list.html', context)

def SchemesListView(request):

    dataset = Schemes.objects.values('ch_num','ch_sc_code','ch_lc_num__lc_desc','ch_sc_code__sc_desc','ch_sf_num__sf_surname',
              'ch_sb_code__sb_desc','ch_eff_date','ch_week','ch_topic',
              'ch_objectives','ch_methods','ch_evaluation','ch_status').annotate(num_of=Count('ch_num')).order_by('ch_sc_code__sc_desc','ch_week')

    sc_schemes = SchemesFilter(request.GET, queryset=dataset)
    total_num  = sc_schemes.qs.aggregate(TotNum=Sum('num_of'))

    context = {'filter': sc_schemes, 'total_num': total_num}

    return render(request, 'sadmin/reports/schemes_list.html', context)

def DailyPlanListView(request,ch_num):

    dataset = DailyPlan.objects.filter(sp_ch_num=ch_num).values('sp_num','sp_plan_date','sp_del_date','sp_day',\
		'sp_start_time','sp_finish_time','sp_cycle','sp_sc_code__sc_desc','sp_sb_code__sb_desc','sp_hrs','sp_area',\
        'sp_absorption').order_by('sp_del_date')

    dailyplan = DailyPlanFilter(request.GET, queryset=dataset)
    #total_num = sc_class.qs.aggregate(TotNum=Sum('num_of'))

    context = {'filter': dailyplan}

    return render(request, 'sadmin/reports/dailyplan_list.html', context)

def ClassDailyPlanListView(request,sc_code):

    dataset = DailyPlan.objects.filter(sp_sc_code=sc_code).values('sp_num','sp_plan_date','sp_del_date','sp_day',\
		'sp_start_time','sp_finish_time','sp_cycle','sp_sc_code__sc_desc','sp_sb_code__sb_desc','sp_hrs','sp_area',\
        'sp_absorption','sp_sc_code').order_by('sp_del_date')

    dailyplan = DailyPlanFilter(request.GET, queryset=dataset)
    #total_num = sc_class.qs.aggregate(TotNum=Sum('num_of'))

    context = {'filter': dailyplan}

    return render(request, 'sadmin/reports/dailyplan_list.html', context)
def ClassAssessmentListView(request,sc_code):

    dataset = ClassAssessment.objects.filter(as_sc_code=sc_code).values('as_num','as_lc_num__lc_desc',\
              'as_sc_code__sc_desc','as_ch_num','as_sb_code__sb_desc','as_type','as_name',\
              'as_remark','as_exception','as_comment','as_review','as_resources',\
              'as_trans_date','as_status').order_by('as_trans_date')

    classassessment = ClassAssessmentFilter(request.GET, queryset=dataset)
    #total_num = sc_class.qs.aggregate(TotNum=Sum('num_of'))

    context = {'filter': classassessment}

    return render(request, 'sadmin/reports/classassessment_list.html', context)

def LearnerAssessmentListView(request,as_num):

    dataset = LearnerAssessment.objects.filter(la_as_num=as_num).values('la_num','la_as_num__as_name','la_cm_num__cm_surname',
              'la_cm_num__cm_fname','la_lc_num','la_sc_code__sc_desc','la_type','la_remark','la_comment','la_mark_f',\
              'la_grade_f','la_mark_a','la_grade_a','la_status')\
              .annotate(num_of=Sum('la_num'),max_m=Max('la_mark_a'),min_m=Min('la_mark_a'),avg_m=Avg('la_mark_a'))\
              .order_by('la_as_num','la_num')

    learnerassessment = LearnerAssessmentFilter(request.GET, queryset=dataset)
    total_num = learnerassessment.qs.aggregate(TotNum=Sum('num_of'))
    max_mark = learnerassessment.qs.aggregate(MaxMark=Sum('max_m'))
    min_mark = learnerassessment.qs.aggregate(MinMark=Sum('min_m'))
    avg_mark = learnerassessment.qs.aggregate(AvgMark=Sum('avg_m'))

    context = {'filter': learnerassessment,'total_num' : total_num,'max_mark':max_mark,'min_mark':min_mark,
               'avg_mark':avg_mark}

    return render(request, 'sadmin/reports/learnerassessment_list.html', context)

def MemberRegisterListView(request,sc_code,sp_del_date):

    dataset = MemberRegister.objects.filter(mr_sc_code=sc_code,mr_date=sp_del_date).values('mr_cm_num','mr_num','mr_year','mr_term','mr_cm_num__cm_surname',\
            'mr_cm_num__cm_fname','mr_sc_code__sc_desc','mr_comment','mr_date','mr_day','mr_mark',
            'mr_status').annotate(present=Count('mr_num',filter=Q(mr_mark='P')),sick=Count('mr_num',filter=Q(mr_mark='S')),\
            absent=Count('mr_num',filter=Q(mr_mark='A')),total_num=Count('mr_num')).order_by('mr_date','mr_cm_num')

    memberregister = MemberRegisterFilter(request.GET, queryset=dataset)
    total_num      = memberregister.qs.aggregate(TotNum=Sum('total_num'))
    tot_present    = memberregister.qs.aggregate(TotPresent=Sum('present'))
    tot_sick    = memberregister.qs.aggregate(TotSick=Sum('sick'))
    tot_absent     = memberregister.qs.aggregate(TotAbsent=Sum('absent'))

    context = {'filter': memberregister,'total_num': total_num,'tot_present': tot_present,
               'tot_excused': tot_sick,'tot_absent': tot_absent}
    return render(request, 'sadmin/reports/memberregister_list.html', context)


class GenSchemeView(View):
    form_class = GenSchemeForm
    template_name = 'sadmin/reports/genscheme.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'GenSchemeForm': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        context = {'form': form}
        if form.is_valid():
            l_year = form.cleaned_data['f_year']
            l_term = form.cleaned_data['f_term']
            l_gen = form.cleaned_data['Gen_ok']

            termparams = TermParameter.objects.get(tp_year=l_year, tp_term=l_term)

            l_tp_year = termparams.tp_year
            l_tp_term = termparams.tp_term
            l_tp_weeks = termparams.tp_weeks
            l_tp_period_len = termparams.tp_period_len
            l_cycle_days = termparams.tp_cycledays
            l_tp_days = termparams.tp_days
            l_tp_start_date = termparams.tp_start_date
            l_tp_end_date = termparams.tp_end_date
            l_tp_status = termparams.tp_status
            l_tp_schemed = termparams.tp_schemed
            l_tp_period_len = termparams.tp_period_len

            l_sp_start_date = l_tp_start_date
            l_eff_date = l_tp_start_date

            # Loop through Level Class Subject (For each study level, class and subject )
            if l_gen == 'Y' and l_tp_schemed == '1':

                classsubject = ClassSubject.objects.filter(cs_status='1')  # all()

                for subject in classsubject:
                    classsubject1 = ClassSubject.objects.get(pk=subject.cs_code)

                    # syllabus   = Syllabus.objects.get(sy_sb_code=levelclass1.lc_sb_code)

                    # l_sy_code  = syllabus
                    # l_ex_board = syllabus.sb_ex_board

                    l_week = 1
                    no_of_weeks = 1
                    l_status = 0

                    while l_week <= l_tp_weeks:
                        c_scheme = Schemes()
                        # print(l_week)
                        c_scheme.ch_cs_code  = classsubject1
                        c_scheme.ch_sc_code  = classsubject1.cs_sc_code
                        c_scheme.ch_sf_num   = classsubject1.cs_sf_num
                        c_scheme.ch_sl_code  = classsubject1.cs_sl_code
                        c_scheme.ch_sb_code  = classsubject1.cs_sb_code
                        c_scheme.ch_eff_date = l_eff_date
                        c_scheme.ch_year     = l_tp_year
                        c_scheme.ch_term     = l_tp_term
                        # c_scheme.ch_sy_code  = l_sy_code
                        # c_scheme.ch_ex_board = l_ex_board
                        c_scheme.ch_week = l_week
                        c_scheme.ch_status = l_status

                        c_scheme.save()
                        l_day        = 0
                        l_day_num    = 0
                        l_weekendday = 'N'
                        l_hrs        = l_tp_period_len
                        l_eff_date   = l_eff_date + datetime.timedelta(days=l_cycle_days)

                        # print(l_cycle_days)
                        while l_day    <= l_cycle_days:  # l_cycle_days : l_tp_days:
                            new_scheme = Schemes.objects.get(pk=c_scheme.pk)

                            c_dalypan  = DailyPlan()

                            l_d_status = '0'
                            week_end   = [5, 6]

                            if l_sp_start_date.weekday() in week_end:
                                l_d_status = 'W'
                                l_day_num  = 0
                            else:
                                l_day      = (l_day + 1)
                                l_day_num  = l_day

                            if ExcludedDay.objects.filter(ex_date=l_sp_start_date,ex_status='1').exists():
                                l_d_status = 'H'
                                l_day_num  = 0

                            c_dalypan.sp_ch_num_id = new_scheme.ch_num
                            c_dalypan.sp_cs_code   = new_scheme.ch_cs_code
                            c_dalypan.sp_sl_code   = new_scheme.ch_sl_code
                            c_dalypan.sp_sc_code   = new_scheme.ch_sc_code
                            c_dalypan.sp_sf_num    = new_scheme.ch_sf_num
                            c_dalypan.sp_sb_code   = new_scheme.ch_sb_code
                            c_dalypan.sp_year      = new_scheme.ch_year
                            c_dalypan.sp_term      = new_scheme.ch_term
                            c_dalypan.sp_cycle     = new_scheme.ch_week
                            c_dalypan.sp_day       = l_day_num
                            c_dalypan.sp_hrs       = l_hrs
                            c_dalypan.sp_del_date  = l_sp_start_date
                            c_dalypan.sp_plan_date = l_sp_start_date
                            c_dalypan.sp_type      = '1'  # new_scheme.ch_type
                            c_dalypan.sp_status    = l_d_status

                            c_dalypan.save()
                            l_d_status      = '0'
                            l_sp_start_date = l_sp_start_date + datetime.timedelta(days=1)

                        l_week = l_week + 1
                        l_tp_start_date = l_tp_start_date + datetime.timedelta(days=1)

            return redirect('genscheme')

        return render(request, self.template_name, {'GenSchemeForm': form})
class GenRegisterView(View):
    form_class = GenRegiserForm
    template_name = 'sadmin/reports/genregister.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'GenRegiserForm': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        context = {'form': form}
        if form.is_valid():
            l_year =  form.cleaned_data['f_year']
            l_term = form.cleaned_data['f_term']
            l_gen  = form.cleaned_data['Gen_ok']

            termparams = TermParameter.objects.get(tp_year=l_year,tp_term=l_term)

            l_tp_year       = termparams.tp_year
            l_tp_term       = termparams.tp_term
            l_tp_weeks      = termparams.tp_weeks
            l_tp_period_len = termparams.tp_period_len
            l_tp_days       = termparams.tp_days
            l_tp_start_date = termparams.tp_start_date
            l_tp_end_date   = termparams.tp_end_date
            l_tp_status     = termparams.tp_status
            l_tp_schemed    = termparams.tp_schemed

    #Loop through Level Class Subject (For each study level, class and subject )
            if l_gen == 'Y':
              classmember = ClassMember.objects.all()

              for member in classmember :
                 l_cm_num     = member.cm_num
                 l_cm_sc_code = member.cm_sc_code
                 l_mr_date    = l_tp_start_date
                 l_days       = 1

                 while l_days <= l_tp_days :
                    m_register = MemberRegister()
                    l_d_status = 'N'
                    week_end = [5, 6]

                    if l_mr_date.weekday() in week_end:
                        l_d_status = 'W'
                        l_mr_mark = 'W'
                    else:
                        l_d_status = 'N'
                        l_mr_mark = 'P'

                    if ExcludedDay.objects.filter(ex_date=l_mr_date).exists():
                        l_d_status = 'H'
                        l_mr_mark = 'H'

                    m_register.mr_cm_num_id  = l_cm_num #levelclass1.cm_num
                    m_register.mr_sc_code = l_cm_sc_code #levelclass1.cm_sc_code
                    m_register.mr_date    = l_mr_date
                    m_register.mr_year    = l_tp_year
                    m_register.mr_term    = l_tp_term
                    m_register.mr_day     = l_days
                    m_register.mr_status  = l_d_status
                    m_register.mr_mark    = l_mr_mark

                    m_register.save()
                    l_days     = l_days + 1
                    l_mr_date  = l_mr_date + datetime.timedelta(days=1)
                    l_d_status = 'N'
                    l_mr_mark  = 'P'

            return redirect('genregister')

        return render(request, self.template_name, {'GenRegiserForm': form})

class GenSpaceLotView(View):
    form_class = GenSpaceLotForm
    template_name = 'sadmin/reports/genspacelot.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'GenSpaceLotForm': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        context = {'form': form}
        if form.is_valid():
            l_year = form.cleaned_data['f_year']
            l_term = form.cleaned_data['f_term']
            l_gen = form.cleaned_data['Gen_ok']

            termparams = TermParameter.objects.get(tp_year=l_year, tp_term=l_term)

            l_tp_year = termparams.tp_year
            l_tp_term = termparams.tp_term
            l_tp_weeks = termparams.tp_weeks
            l_tp_period_len = termparams.tp_period_len
            l_tp_days = termparams.tp_days
            l_tp_start_date = termparams.tp_start_date
            l_tp_end_date = termparams.tp_end_date
            l_start_time = termparams.tp_start_time
            l_finish_time = termparams.tp_end_time
            l_tp_status = termparams.tp_status
            l_tp_schemed = termparams.tp_schemed

            # Loop through Level Class Subject (For each study level, class and subject )
            if l_gen == 'Y':
                facilityspace = FacilitySpace.objects.all()

                for space in facilityspace:
                    l_fs_num = space.fs_num
                    l_fc_num = space.fs_fc_num_id

                    l_mr_date = l_tp_start_date
                    l_days = 1

                    print(space.fs_num, space.fs_fc_num)
                    while l_days <= l_tp_days:
                        num_slots = 0
                        max_slots = 28

                        slot_start_time = l_start_time
                        slot_finish_time = l_finish_time

                        #spaceslot = SpaceSlot()
                        l_d_status = 'N'
                        week_end = [5, 6]

                        if l_mr_date.weekday() in week_end:
                            l_d_status = 'W'
                            l_mr_mark = 'W'
                        else:
                            l_d_status = 'N'
                            l_mr_mark = 'P'

                        if ExcludedDay.objects.filter(ex_date=l_mr_date).exists():
                            l_d_status = 'H'
                            l_mr_mark = 'H'

                        #num_slots = 0
                        #max_slots = 28

                        #slot_start_time = l_start_time
                        #slot_finish_time = l_finish_time

                        print(slot_start_time, l_finish_time)

                        #while slot_start_time <= l_finish_time:
                        while num_slots <= max_slots:
                            spaceslot = SpaceSlot()
                            slot_finish_time = (slot_start_time + datetime.timedelta(minutes=30))

                            print(l_days, '****',slot_start_time,slot_finish_time)
                            spaceslot.sp_fs_num_id = l_fs_num
                            spaceslot.sp_fc_num_id = l_fc_num
                            # spaceslot.sp_sc_code_id = l_fs_num

                            spaceslot.sp_date = l_mr_date
                            spaceslot.sp_day = l_days
                            spaceslot.sp_start_time = slot_start_time
                            spaceslot.sp_finish_time = slot_finish_time

                            spaceslot.save()

                            num_slots = (num_slots + 1)

                            slot_start_time = slot_finish_time

                        l_days = l_days + 1
                        l_mr_date = l_mr_date + datetime.timedelta(days=1)
                        l_d_status = 'N'
                        l_mr_mark = 'P'

            return redirect('genspacelot')

        return render(request, self.template_name, {'GenSpaceLotForm': form})
class GenBillView(View):
    form_class = GenBillForm
    template_name = 'sadmin/reports/genbill.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'GenBillForm': form})
    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        context = {'form': form}
        if form.is_valid():
            l_year = form.cleaned_data['f_year']
            l_term = form.cleaned_data['f_term']
            l_gen = form.cleaned_data['Gen_ok']

            termparams = TermParameter.objects.get(tp_year=l_year, tp_term=l_term)

            l_tp_year = termparams.tp_year
            l_tp_term = termparams.tp_term
            l_tp_weeks = termparams.tp_weeks
            l_tp_period_len = termparams.tp_period_len
            l_tp_days = termparams.tp_days
            l_tp_start_date = termparams.tp_start_date
            l_tp_end_date = termparams.tp_end_date
            l_tp_status = termparams.tp_status
            l_tp_schemed = termparams.tp_schemed

            # Loop through Level Class Subject (For each study level, class and subject )
            if l_gen == 'Y':

                classmember = ClassMember.objects.all().order_by('cm_sc_code')

                for member in classmember:
                    l_cm_num = member.cm_num
                    l_sc_code = member.cm_sc_code
                    l_lv_code = member.cm_lv_code

                    classbilling = ClassBilling.objects.filter(cb_sc_code=l_sc_code)

                    for billing in classbilling:

                        #print(billing.cb_num,billing.cb_rate,billing.cb_year)
                        l_cb_num = billing.cb_num
                        l_cb_sc_code = billing.cb_sc_code
                        l_cb_lv_code = billing.cb_lv_code
                        l_cb_type = billing.cb_type
                        l_cb_desc = billing.cb_desc
                        l_cb_rate = billing.cb_rate
                        l_cb_year = billing.cb_year
                        l_cb_term = billing.cb_term

                        membrec_c = MemberRecord()

                        membrec_c.mr_cm_num_id = l_cm_num
                        membrec_c.mr_sc_code = l_sc_code
                        membrec_c.mr_lv_code = l_lv_code
                        membrec_c.mr_cb_num_id = l_cb_num
                        membrec_c.mr_year = l_cb_year
                        membrec_c.mr_term = l_cb_term
                        membrec_c.mr_trans_date = l_tp_start_date
                        membrec_c.mr_due_date = l_tp_start_date
                        membrec_c.mr_pamount = l_cb_rate
                        membrec_c.mr_aamount = l_cb_rate
                        membrec_c.mr_pay_ref = 'None'
                        membrec_c.mr_category = '1'
                        membrec_c.mr_dr_cr = 'D'
                        membrec_c.mr_paid = 'N'
                        membrec_c.mr_status = '1'
                        membrec_c.mr_processed = 'N'
                        membrec_c.mr_pay_type = '1'

                        membrec_c.save()

                        subjectbilling = SubjectBilling.objects.filter(jb_sc_code=l_sc_code)

                        for subject in subjectbilling:

                            l_jb_num = subject.jb_num
                            l_jb_sl_code = subject.jb_sl_code
                            l_jb_sc_code = subject.jb_sc_code
                            l_jb_lv_code = subject.jb_lv_code
                            #l_jb_sb_code = subject.jb_sb_code
                            l_jb_type = subject.jb_type
                            l_jb_desc = subject.jb_desc
                            l_jb_rate = subject.jb_rate
                            l_jb_status = subject.jb_status
                            l_jb_year = subject.jb_year
                            l_jb_term = subject.jb_term

                            membrec_sb = MemberRecord()

                            membrec_sb.mr_cm_num_id = l_cm_num
                            membrec_sb.mr_sc_code = l_jb_sc_code
                            membrec_sb.mr_lv_code = l_lv_code
                            membrec_sb.mr_jb_num_id = l_jb_num
                            membrec_sb.mr_year = l_jb_year
                            membrec_sb.mr_term = l_jb_term
                            membrec_sb.mr_trans_date = l_tp_start_date
                            membrec_sb.mr_due_date = l_tp_start_date
                            membrec_sb.mr_pamount = l_jb_rate
                            membrec_sb.mr_aamount = l_cb_rate
                            membrec_sb.mr_pay_ref = 'None'
                            membrec_sb.mr_category = '1'
                            membrec_sb.mr_dr_cr = 'D'
                            membrec_sb.mr_paid = 'N'
                            membrec_sb.mr_status = '1'
                            membrec_sb.mr_processed = 'N'
                            membrec_sb.mr_pay_type = '1'

                            membrec_sb.save()

            return redirect('billgen')

        return render(request, self.template_name, {'GenBillForm': form})

class GenSeatsView(View):
    form_class = GenClassForm
    template_name = 'sadmin/reports/genclass.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'GenClassForm': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        context = {'form': form}
        if form.is_valid():
            l_year = form.cleaned_data['f_year']
            l_term = form.cleaned_data['f_term']
            l_gen = form.cleaned_data['Gen_ok']

            termparams = TermParameter.objects.get(tp_year=l_year, tp_term=l_term)

            l_tp_year = termparams.tp_year
            l_tp_term = termparams.tp_term
            l_tp_weeks = termparams.tp_weeks
            l_tp_seats = termparams.tp_seats
            l_tp_period_len = termparams.tp_period_len
            l_tp_days = termparams.tp_days
            l_tp_start_date = termparams.tp_start_date
            l_tp_end_date = termparams.tp_end_date
            l_tp_status = termparams.tp_status
            l_tp_schemed = termparams.tp_schemed

            classquery = SchoolClass.objects.all().order_by('sc_code')

            for c_query in classquery:

                n_of_seats = 1

                while n_of_seats <= l_tp_seats:
                    c_memb = ClassMember()

                    c_memb.cm_sc_code_id = c_query.sc_code
                    c_memb.cm_lv_code = c_query.sc_lv_code
                    c_memb.cm_year = l_year
                    c_memb.cm_surname = 'X'
                    c_memb.cm_fname = 'X'
                    c_memb.cm_othername = 'X'
                    c_memb.cm_guardian = 'X'
                    c_memb.cm_phone = 'X'
                    c_memb.cm_email = 'X'
                    c_memb.cm_gender = 'F'

                    c_memb.save()

                    n_of_seats = (n_of_seats + 1)

            return redirect('genclasseats')
        return render(request, self.template_name, {'GenRegiserForm': form})
class GenLevelView(View):
    form_class = GenLevelForm
    template_name = 'sadmin/reports/genslevel.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'GenLevelForm': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        context = {'form': form}
        if form.is_valid():
            l_lv_code =  form.cleaned_data['l_code']
            l_gen     = form.cleaned_data['Gen_ok']

    #Loop through Subjects assigning ot to a school class
            if l_gen == 'Y':
              subject = Subject.objects.all()
              for sub in subject :

                 schoollevel = SchoolLevel.objects.all()

                 for school in schoollevel:
                    level = Level()

                    level.lv_code          = l_lv_code
                    level.lv_name          = school.sl_name
                    level.lv_sl_code_id    = school.sl_code
                    level.lv_sb_code_id    = sub.sb_code

                    level.save()
                    print(l_lv_code, school.sl_name ,school.sl_code ,sub.sb_code)
                    l_lv_code = (l_lv_code + 1)

            return redirect('genlevel')

        return render(request, self.template_name, {'GenLevelForm': form})

class GenMovementView(View):
    form_class = GenMovementForm
    template_name = 'sadmin/reports/genmovement.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'GenMovementForm': form})

    def post(self, request, *args, **kwargs):

        form = self.form_class(request.POST)
        context = {'form': form}
        if form.is_valid():
            l_class_code =  form.cleaned_data['class_code']
            #l_term = form.cleaned_data['f_term']
            l_gen  = form.cleaned_data['Gen_ok']

            termparams = TermParameter.objects.get(tp_status='1')

            l_tp_year       = termparams.tp_year
            l_tp_term       = termparams.tp_term
            l_tp_weeks      = termparams.tp_weeks
            l_tp_period_len = termparams.tp_period_len
            l_tp_days       = termparams.tp_days
            l_tp_start_date = termparams.tp_start_date
            l_tp_end_date   = termparams.tp_end_date
            l_tp_status     = termparams.tp_status
            l_tp_schemed    = termparams.tp_schemed

    #Loop through Level Class Subject (For each study level, class and subject )
            if l_gen == 'Y':
              classmember = ClassMember.objects.filter(cm_sc_code=l_class_code) #all()

              for member in classmember :
                 l_cm_num     = member.cm_num
                 l_cm_sc_code = member.cm_sc_code
                 l_mr_date    = l_tp_start_date
                 l_days       = 1

                 print('Class Found')

                 while l_days <= l_tp_days :
                    m_movement = MemberMovement()
                    l_d_status = 'N'
                    week_end = [5, 6]

                    if l_mr_date.weekday() in week_end:
                        l_d_status = 'W'
                        l_mr_mark = 'W'
                    else:
                        l_d_status = 'N'
                        l_mr_mark = 'P'

                    if ExcludedDay.objects.filter(ex_date=l_mr_date).exists():
                        l_d_status = 'H'
                        l_mr_mark = 'H'

                    if l_mr_mark == 'W' :

                        m_movement.mm_cm_num_id  = l_cm_num
                        m_movement.mm_sc_code    = l_cm_sc_code
                        m_movement.mm_date       = l_mr_date
                        m_movement.mm_dr_status  = '0'
                        m_movement.mm_pk_status  = '0'
                        m_movement.mm_day        = l_days
                        m_movement.mm_status     = '0'

                        m_movement.save()

                    l_days     = l_days + 1
                    l_mr_date  = l_mr_date + datetime.timedelta(days=1)
                    l_d_status = 'N'
                    l_mr_mark  = 'P'

            return redirect('genmovement')

        return render(request, self.template_name, {'GenMovementForm': form})

# Class member payment
def SubmitPayView(request, pk, mr_cm_num):

        classmember = ClassMember.objects.get(cm_num=mr_cm_num)
        memberdue = get_object_or_404(MemberRecord, pk=pk)

        new_payment = None
        if request.method == 'POST':

            form = ReceiptForm(data=request.POST or None)

            if form.is_valid():
                # Create Receipt object but don't save to database yet
                new_payment = form.save(commit=False)
                new_payment.rc_mr_num  = pk
                new_payment.rc_sc_code = memberdue.mr_sc_code
                new_payment.rc_lv_code = memberdue.mr_lv_code
                new_payment.rc_status  = 'O'

                new_payment.py_user = request.user

                new_payment.save()
                messages.success(request, "Payment submitted successfully")
            return redirect('payment')
        else:
            form = ReceiptForm()
        return render(request, 'sadmin/payments/submitpay.html', {'form': form, 'new_payment': new_payment})
def ReceiptView(request, mr_num):

    membrec = get_object_or_404(MemberRecord, mr_num=mr_num)

    new_receipt = None
    if request.method == 'POST':

        form = ReceiptForm(data=request.POST or None)

        if form.is_valid():
            # Create a Staff Subject object but don't save to database yet
            new_receipt = form.save(commit=False)

            new_receipt.rc_cm_num  = membrec.mr_cm_num
            new_receipt.rc_sc_code = membrec.mr_sc_code
            new_receipt.rc_lv_code = membrec.mr_lv_code

            new_receipt.rc_mr_num  = membrec.mr_num
            new_receipt.rc_year    = membrec.mr_year
            new_receipt.rc_term    = membrec.mr_term
            new_receipt.rc_dr_cr   = 'C'

            new_receipt.save()
            messages.success(request, "Receipted successfully")
        return redirect('paylist')
    else:
        form = ReceiptForm()
    return render(request, 'sadmin/receipt/receipt.html', {'form': form})

def MemberPayView(request,mr_num):
    memberdue = get_object_or_404(MemberRecord, mr_num=mr_num)
    #memberdue  = MemberRecord.objects.get(mr_num = mr_num)

    new_receipt = None
    if request.method == 'POST':

        form = ReceiptForm(data=request.POST or None)

        if form.is_valid():
            # Create a Level object but don't save to database yet

            f_pamount = form.cleaned_data['rc_pamount']
            f_aamount = form.cleaned_data['rc_aamount']
            f_mr_num = form.cleaned_data['rc_mr_num']

            new_receipt = form.save(commit=False)
            new_receipt.rc_mr_num     = memberdue.mr_num
            new_receipt.rc_cm_num     = memberdue.mr_cm_num
            new_receipt.rc_cm_num     = memberdue.mr_cm_num
            new_receipt.rc_sc_code    = memberdue.mr_sc_code
            new_receipt.rc_lv_code    = memberdue.mr_lv_code
            new_receipt.rc_year       = memberdue.mr_year
            new_receipt.rc_term       = memberdue.mr_term
            new_receipt.rc_pamount    = memberdue.mr_pamount
            new_receipt.rc_mr_num     = memberdue.mr_num

            f_pamount    = (f_pamount* -1)
            f_aamount    = (f_aamount* -1)

            new_receipt.save()

            membrec = MemberRecord()

            membrec.mr_cm_num  = memberdue.mr_cm_num
            membrec.mr_sc_code = memberdue.mr_sc_code
            membrec.mr_lv_code = memberdue.mr_lv_code

            membrec.mr_cb_num  = memberdue.mr_cb_num
            membrec.mr_jb_num  = memberdue.mr_jb_num

            membrec.mr_year    = memberdue.mr_year
            membrec.mr_term    = memberdue.mr_term

            #membrec.mr_period     = memberdue.mr_period
            membrec.mr_trans_date = memberdue.mr_trans_date
            #membrec.mr_value_date = memberdue.mr_value_date
            membrec.mr_due_date   = memberdue.mr_due_date
            membrec.mr_pamount    = f_pamount
            membrec.mr_aamount    = f_aamount
            membrec.mr_units      = 0
            membrec.mr_pay_ref    = f_mr_num
            membrec.mr_category   = 'G'
            membrec.mr_dr_cr      = 'C'
            membrec.mr_paid       = 'N'
            membrec.mr_status     = '1'
            membrec.mr_processed  = '1'
            membrec.mr_pay_type   = '3'

            membrec.save()

            messages.success(request, "Payment submitted successfully")
        return redirect('paylist')
    else:
        form = ReceiptForm()
    return render(request,  'sadmin/payments/submitpay.html', {'form': form})

def PayListView(request):
        global l_gr_num

        total = 0
        dataset = MemberRecord.objects.filter(mr_status='1').values('mr_num','mr_cm_num','mr_sc_code__sc_desc','mr_cm_num',
                  'mr_cm_num__cm_surname','mr_cm_num__cm_fname','mr_cm_num__cm_guardian','mr_cm_num__cm_phone',
                  'mr_trans_date','mr_year','mr_term','mr_aamount','mr_pay_ref','mr_dr_cr',
                  'mr_paid','mr_status','mr_processed','mr_pay_type','mr_category').\
                  annotate(sum_damnt=Sum('mr_aamount',filter=Q(mr_dr_cr='D')),
                  sum_camnt=Sum('mr_aamount',filter=Q(mr_dr_cr='C'))).order_by('mr_sc_code', 'mr_year')

        rec_list  = MembContFilter(request.GET, queryset=dataset)
        sum_damnt = rec_list.qs.aggregate(SumDamnt=Sum('sum_damnt'))
        sum_camnt = rec_list.qs.aggregate(SumCamnt=Sum('sum_camnt'))

        context = {'filter': rec_list, 'sum_damnt': sum_damnt, 'sum_camnt': sum_camnt }

        return render(request, 'sadmin/reports/paylist.html', context)


def StudentAccView(request, mr_cm_num):
    total = 0
    dataset = MemberRecord.objects.filter(mr_status='1', mr_cm_num=mr_cm_num).values('mr_num', 'mr_cm_num',
              'mr_sc_code__sc_desc', 'mr_cm_num','mr_cm_num__cm_surname','mr_cm_num__cm_fname',
              'mr_cm_num__cm_guardian','mr_cm_num__cm_phone','mr_trans_date', 'mr_year','mr_term', 'mr_aamount',
              'mr_pay_ref', 'mr_dr_cr','mr_paid', 'mr_status','mr_processed', 'mr_pay_type','mr_category'). \
              annotate(sum_damnt=Sum('mr_aamount', filter=Q(mr_dr_cr='D')),
                 sum_camnt=Sum('mr_aamount', filter=Q(mr_dr_cr='C'))).order_by('mr_sc_code', 'mr_year')

    rec_list = MembContFilter(request.GET, queryset=dataset)
    sum_damnt = rec_list.qs.aggregate(SumDamnt=Sum('sum_damnt'))
    sum_camnt = rec_list.qs.aggregate(SumCamnt=Sum('sum_camnt'))

    context = {'filter': rec_list, 'sum_damnt': sum_damnt, 'sum_camnt': sum_camnt}

    return render(request, 'sadmin/reports/paylist.html', context)

def g_position(request):
    dataset = MemberRecord.objects.values('mr_year').annotate(
        rec_sum=Sum('mr_aamount', filter=Q(mr_dr_cr='C')),
        inv_sum=Sum('mr_aamount', filter=Q(mr_dr_cr='D'))) \
        .order_by('mr_year')

    years = list()
    inv_series_data = list()
    rec_series_data = list()

    for entry in dataset:
        years.append('%s Year' % entry['mr_year'])

        inv = entry['inv_sum']
        if inv is None:
            inv = 0
        inv = abs(float(inv))

        rec = entry['rec_sum']
        if rec is None:
            rec = 0
        rec = abs(float(rec))

        inv_series_data.append(inv)
        rec_series_data.append(rec)

    inv_series = {
        'name': 'Invoiced',
        'data': inv_series_data,
        'color': 'purple'
    }

    rec_series = {
        'name': 'Receipts',
        'data': rec_series_data,
        'color': 'green'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Group Financial Dashboard'},
        'xAxis': {'years': years},
        'series': [inv_series, rec_series]
    }

    dump = json.dumps(chart, cls=DecimalEncoder)

    return render(request, 'sadmin/reports/charts/g_position.html', {'chart': dump})

def GenderAnl(request):
    dataset = ClassMember.objects.values('cm_sc_code').annotate(
        tot_m=Count('cm_num', filter=Q(cm_gender='M')),
        tot_f=Count('cm_num', filter=Q(cm_gender='F'))) \
        .order_by('cm_sc_code')

    s_class = list()
    male_series_data = list()
    female_series_data = list()

    for entry in dataset:
        s_class.append('%s s_class' % entry['cm_sc_code'])

        male = entry['tot_m']
        if male is None:
            male = 0
        male = abs(float(male))

        female = entry['tot_f']
        if female is None:
            female = 0
        female = abs(float(female))

        male_series_data.append(male)
        female_series_data.append(female)

    male_series = {
        'name': 'Males',
        'data': male_series_data,
        'color': 'purple'
    }

    female_series = {
        'name': 'Female',
        'data': female_series_data,
        'color': 'Yellow'
    }

    chart = {
        'chart': {'type': 'column'},
        'title': {'text': 'Class Gender Analysis'},
        'xAxis': {'s_class': s_class},
        'series': [male_series, female_series]
    }

    dump = json.dumps(chart, cls=DecimalEncoder)

    return render(request, 'sadmin/reports/charts/genderanl.html', {'chart': dump})

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        #  if passed in object is instance of Decimal
        # convert it to a string
        if isinstance(obj, Decimal):
            return str(obj)
        # otherwise use the default behavior
        return json.JSONEncoder.default(self, obj)

# Schedules
def SubjectSchedView(request):

        dataset   = Subject.objects.filter(sb_status='1').values('sb_desc', 'sb_code', 'sb_type','sb_hrs'). \
                    annotate(sum_hrs=Sum('sb_hrs'), cnt_sub=Count('sb_code')).order_by('sb_desc')

        sub_list = SubjectFilter(request.GET, queryset=dataset)
        tot_hrs  = sub_list.qs.aggregate(SumHrs=Sum('sum_hrs'))
        tot_subj = sub_list.qs.aggregate(CntSub=Sum('cnt_sub'))

        context  = {'filter': sub_list, 'tot_hrs': tot_hrs, 'tot_subj': tot_subj}

        return render(request, 'sadmin/reports/schedules/subjectlist.html', context)

def SchClassSchedView(request):
    dataset = SchoolClass.objects.filter(sc_status='1').values('sc_sl_code__sl_name', 'sc_desc', 'sc_code',\
              'sc_sf_num__sf_surname'). \
        annotate(cnt_class=Count('sc_code')).order_by('sc_lv_code', 'sc_desc')

    sch_list = SchoolClassFilter(request.GET, queryset=dataset)
    tot_classes = sch_list.qs.aggregate(CntClass=Sum('cnt_class'))

    context = {'filter': sch_list, 'tot_classes': tot_classes}

    return render(request, 'sadmin/reports/schedules/classlist.html', context)

def ClassMemberListView(request, sc_code):
        dataset = ClassMember.objects.filter(cm_sc_code=sc_code).values('cm_num', 'cm_sc_code', 'cm_sc_code__sc_desc',
                  'cm_lv_code', 'cm_year','cm_surname', 'cm_fname', 'cm_othername','cm_guardian', 'cm_phone',
                  'cm_email', 'cm_dob','cm_gender','cm_doj', 'cm_dol', 'cm_status').annotate(
                  cnt_membs=Count('cm_num'), cnt_membf=Count('cm_num', filter=Q(cm_gender='F'))).order_by('cm_surname')

        member_list = ClassMemberFilter(request.GET, queryset=dataset)
        tot_membs = member_list.qs.aggregate(CntMembs=Sum('cnt_membs'))
        tot_membf = member_list.qs.aggregate(CntMembf=Sum('cnt_membf'))
        #tot_membm = member_list.qs.aggregate(CntMembm=Sum('cnt_membm'))

        context = {'filter': member_list, 'tot_membs': tot_membs, 'tot_membf': tot_membf, }

        return render(request, 'sadmin/reports/schedules/classmemblist.html', context)

def MemberMvtListView(request, sc_code):
    dataset = MemberMovement.objects.filter(mm_sc_code=sc_code).values('mm_num', 'mm_cm_num', 'mm_cm_num__cm_surname',
              'mm_cm_num__cm_fname', 'mm_sc_code','mm_sc_code__sc_desc', 'mm_fs_num','mm_day', 'mm_date', 'mm_dr_ar_num','mm_dr_ar_num__ar_sname',
              'mm_date_dr', 'mm_dr_status', 'mm_dr_notes','mm_pk_ar_num', 'mm_pk_ar_num__ar_sname','mm_date_pk',
              'mm_pk_status', 'mm_pk_notes').annotate(cnt_membs=Count('mm_num'), cnt_dr=Count('mm_num', filter=Q(mm_dr_status='2')),
               cnt_pk=Count('mm_num', filter=Q(mm_pk_status='0'))).order_by('mm_sc_code')

    member_list = MemberMvtFilter(request.GET, queryset=dataset)
    tot_membs = member_list.qs.aggregate(CntMembs=Sum('cnt_membs'))
    tot_dr = member_list.qs.aggregate(CntDr=Sum('cnt_dr'))
    tot_pk = member_list.qs.aggregate(CntPk=Sum('cnt_pk'))

    context = {'filter': member_list, 'tot_membs': tot_membs, 'tot_dr': tot_dr, 'tot_pk': tot_pk}

    return render(request, 'sadmin/reports/schedules/membmvtlist.html', context)
def StaffSchedView(request):
        dataset = StaffMember.objects.filter(sf_status='1').values('sf_surname', 'sf_fname', 'sf_gender',
            'sf_dp_code__dp_name','sf_phone','sf_app_status').annotate(cnt_staff=Count('sf_num')).order_by('sf_surname')

        staff_list = StaffMemberFilter(request.GET, queryset=dataset)
        tot_staff  = staff_list.qs.aggregate(CntStaff=Sum('cnt_staff'))

        context = {'filter': staff_list, 'tot_staff': tot_staff}

        return render(request, 'sadmin/reports/schedules/stafflist.html', context)

def SchmeSchedView(request):

    dataset = Schemes.objects.values('ch_num','ch_lv_code__lv_name', 'ch_sc_code__sc_desc',
              'ch_sf_num__sf_surname', 'ch_sb_code__sb_desc', 'ch_year','ch_term','ch_week',
              'ch_objectives','ch_evaluation').\
        annotate(cnt_sch=Count('ch_week'),cnt_psch=Count('ch_week',filter=Q(ch_status='2'))).order_by('ch_lv_code')

    scheme_list = SchemesFilter(request.GET, queryset=dataset)
    sch_tot = scheme_list.qs.aggregate(CntSch=Sum('cnt_sch'))
    sch_ptot = scheme_list.qs.aggregate(CntPsch=Sum('cnt_psch'))

    context = {'filter': scheme_list, 'sch_tot': sch_tot, 'sch_ptot': sch_ptot}

    return render(request, 'sadmin/reports/schedules/schemeslist.html', context)

def MemberRegView(request):

    dataset = MemberRegister.objects.exclude(mr_mark='P').values('mr_num','mr_cm_num','mr_sc_code__sc_desc','mr_cm_num__cm_surname', 'mr_cm_num__cm_fname',
              'mr_date', 'mr_mark').\
              annotate(cnt_awol=Count('mr_num',filter=Q(mr_mark='A')),cnt_sick=Count('mr_num',filter=Q(mr_mark='S'))).order_by('mr_sc_code')

    attend_list = MemberRegisterFilter(request.GET, queryset=dataset)
    awol_tot = attend_list.qs.aggregate(CntAwol=Sum('cnt_awol'))
    sick_tot = attend_list.qs.aggregate(CntSick=Sum('cnt_sick'))


    context = {'filter': attend_list, 'awol_tot': awol_tot, 'sick_tot': sick_tot}

    return render(request, 'sadmin/reports/schedules/attendlist.html', context)

def SpacesView(request):

    dataset = FacilitySpace.objects.values('fs_num','fs_fc_num__fc_name','fs_desc','fs_status').\
              annotate(cnt_space=Count('fs_num')) #.order_by('mr_sc_code')

    spaces_list = FacilitySpaceFilter(request.GET, queryset=dataset)
    space_tot   = spaces_list.qs.aggregate(CntSpace=Sum('cnt_space'))

    context = {'filter': spaces_list, 'space_tot': space_tot }

    return render(request, 'sadmin/reports/schedules/spacelist.html', context)

def SlotsView(request):

    dataset = SpaceSlot.objects.values('sp_num','sp_fs_num','sp_fc_num','sp_sc_code','sp_sf_num','sp_type',
                                'sp_desc','sp_hrs','sp_date','sp_day','sp_start_time','sp_finish_time',
                                'sp_fc_num__fc_desc','sp_fs_num__fs_desc','sp_sc_code__sc_desc',
                                'sp_sf_num__sf_surname','sp_status').\
              annotate(cnt_space=Count('sp_num')).order_by('sp_fs_num','sp_num')

    slot_list = SpaceSlotFilter(request.GET, queryset=dataset)
    slot_tot  = slot_list.qs.aggregate(CntSpace=Sum('cnt_space'))

    context = {'filter': slot_list, 'slot_tot': slot_tot }

    return render(request, 'sadmin/reports/schedules/slotlist.html', context)

#Start Blog Views

#Start Commspace Views

class PostList(generic.ListView):

    queryset = BlogPost.objects.filter(bp_status='P').order_by('-ad_date_c')
    template_name = 'sadmin/commspace/index.html'

    context_object_name = 'post_list'
    paginate_by = 20

class PostListAdmin(generic.ListView):

    queryset = BlogPost.objects.exclude(bp_status='P').order_by('-ad_date_c')
    template_name = 'sadmin/commspace/index.html'

    context_object_name = 'post_list'
    paginate_by = 20

class PostDetail(generic.DetailView):
    model = BlogPost
    template_name = 'sadmin/commspace/post_detail.html'

@login_required
def Post_Detail(request, slug):

    c_user = request.user
    print(c_user)

    template_name = 'sadmin/commspace/post_detail.html'
    post = get_object_or_404(BlogPost, slug=slug)

    if request.user.username in ("reg","xx"):
        contributions = post.contributions.all()
        #print(c_user)
    else:
        contributions = post.contributions.filter(pc_active=True)
        print(request.user.username)

    new_contribution = None
    # Contribution posted
    if request.method == 'POST':
        contribution_form = ContributionForm(data=request.POST)

        if contribution_form.is_valid():

            # Create Contribution object but don't save to database yet
            new_contribution = contribution_form.save(commit=False)
            # Assign the current post to the Contribution
            new_contribution.pc_bp_num = post
            # Save the comment to the database
            new_contribution.save()
    else:
        contribution_form = ContributionForm()

    return render(request, template_name, {'post': post,
                                           'contributions': contributions,
                                           'new_contribution': new_contribution,
                                           'contribution_form': contribution_form})
@login_required
def post_new(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.ad_user_c = request.user
            post.save()

            return redirect('post_detail', slug=post.slug)
    else:
        form = BlogForm()
    return render(request, 'sadmin/commspace/post_edit.html', {'form': form})

@login_required
def post_edit(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.ad_user_a = request.user
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = BlogForm(instance=post)
    return render(request, 'sadmin/commspace/post_edit.html', {'form': form,'post': post})

@login_required
def post_remove(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    post.delete()
    return redirect('bloghome')

@login_required
def cont_approve(request, pk):
    contribution = get_object_or_404(PostContribution, pk=pk)
    contribution.approve_contributions()
    return redirect('bloghome')

@login_required
def cont_remove(request, pk):
    contribution = get_object_or_404(PostContribution, pk=pk)
    contribution.delete()
    return redirect('bloghome')

#Data Upload utilities
# Upload Utility Tools
import csv, tempfile, codecs
from django.core.files.storage import default_storage
def StaffUploadView(request):

   #  declaring template
    template = "sadmin/file_upload/member_upload1.html"

    from django.utils.dateparse import parse_datetime

    if request.method == "GET":
        return render(request, template)

# Allows to temporarily store files

# Input file: get the name of the file
    csv_file = request.FILES['file']
    if not csv_file:
            return "No File"

    memb_list = default_storage.save(csv_file.name, csv_file)

    csvfile = default_storage.open(memb_list, 'r')
    reader = csv.reader(csvfile)

    #reader = csv.reader(tempfile_path)

    lines = list(reader)

#import csv
    from django.utils.dateparse import parse_datetime

# Open the csv file and reads it into a two dimensional List
    #f = request.FILES['file']
    #with open("c:/nec/members2024v1.csv", 'rt') as f:
    #with open('c:/starnec/testcase.csv', 'rt') as f:
    #reader = csv.reader(r_file)
    #lines = list(reader)

# Create an empty list of objects of your model
    objects = []

# Iterate each record of the csv file
    for line in lines:
        obj = StaffMember()
    # obj.mm_num=line[0],
        obj.sf_dp_code_id = line[0]
        obj.sf_surname = line[1]
        obj.sf_fname = line[2]
        obj.sf_othername = line[3]

# Add the model to the list of objects
    #objects.append(obj)
        obj.save()

        print(line[2])

# Save all objects simultaniously, instead of saving for each line
    #Member.objects.bulk_create(objects)
    context = {}
    return render(request, template, context)

def DeptUploadView(request):

   #  declaring template
    template = "sadmin/file_upload/member_upload1.html"

    if request.method == "GET":
        return render(request, template)

# Allows to temporarily store files

# Input file: get the name of the file
    csv_file = request.FILES['file']
    if not csv_file:
            return "No File"

    dept_list = default_storage.save(csv_file.name, csv_file)

    csvfile = default_storage.open(dept_list, 'r')
    reader = csv.reader(csvfile)

    lines = list(reader)


# Iterate each record of the csv file
    for line in lines:
        obj = Dept()

        obj.dp_code = line[0]
        obj.dp_name = line[1]

        obj.save()

        #print(line[2])

# Save all objects simultaniously, instead of saving for each line
    context = {}
    return render(request, template, context)


def StaffUpdateView(request):
    #  declaring template
    template = "sadmin/file_upload/member_upload1.html"

    from django.utils.dateparse import parse_datetime

    if request.method == "GET":
        return render(request, template)

    # Allows to temporarily store files

    # Input file: get the name of the file
    csv_file = request.FILES['file']
    if not csv_file:
        return "No File"

    memb_list = default_storage.save(csv_file.name, csv_file)

    csvfile = default_storage.open(memb_list, 'r')
    reader = csv.reader(csvfile)

    # reader = csv.reader(tempfile_path)

    lines = list(reader)

    # import csv
    from django.utils.dateparse import parse_datetime

    # Open the csv file and reads it into a two dimensional List
    # f = request.FILES['file']
    # with open("c:/nec/members2024v1.csv", 'rt') as f:
    # with open('c:/starnec/testcase.csv', 'rt') as f:
    # reader = csv.reader(r_file)
    # lines = list(reader)

    # Create an empty list of objects of your model
    objects = []

    # Iterate each record of the csv file
    for line in lines:
        obj = StaffMember()
        # obj.mm_num=line[0],
        # obj.sf_dp_code_id = line[0]
        # obj.sf_surname = line[1]
        # obj.sf_fname = line[2]
        # obj.sf_othername = line[3]
        l_emp_code = line[0]
        l_dpt_code = line[1]

        StaffMember.objects.filter(sf_fname=l_emp_code).update(sf_dp_code=l_dpt_code)

    # Add the model to the list of objects
    # objects.append(obj)
    # obj.save()

    # print(line[2])

    # Save all objects simultaniously, instead of saving for each line
    # Member.objects.bulk_create(objects)
    context = {}
    return render(request, template, context)

# Upload Utility Tools
import csv, tempfile, codecs
from django.core.files.storage import default_storage

def VenueUploadView(request):

   #  declaring template
    template = "sadmin/file_upload/member_upload1.html"

    if request.method == "GET":
        return render(request, template)

# Allows to temporarily store files

# Input file: get the name of the file
    csv_file = request.FILES['file']
    if not csv_file:
            return "No File"

    dept_list = default_storage.save(csv_file.name, csv_file)

    csvfile = default_storage.open(dept_list, 'r')
    reader = csv.reader(csvfile)

    lines = list(reader)


# Iterate each record of the csv file
    for line in lines:
        obj = FacilitySpace()

        facility = get_object_or_404(Facility, fc_code=line[0])

        obj.fs_fc_num_id = facility.pk
        obj.fs_desc = line[1]

        obj.save()

        #print(line[2])

# Save all objects simultaniously, instead of saving for each line
    context = {}
    return render(request, template, context)