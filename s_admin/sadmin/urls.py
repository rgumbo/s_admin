from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView, name='homepage'),
    path('classhome', views.ClassHomeView, name='classhome'),
     path('params', views.ParaHomeView, name='params'),
    path('opspath', views.SchoolOpsView, name='opspath'),
    path('infocentre', views.InfoCentreView, name='infocentre'),
    path('theschool', views.TheSchoolView, name='theschool'),

    path('addsubject', views.SubjectView, name='addsubject'),
    path('subjectdetail/str<pk>/', views.SubjectDetailView.as_view(), name='subjectdetail'),
    path('editsubject/<str:pk>/', views.EditSubject, name='editsubject'),
    path('subject/', views.SubjectIndexView.as_view(), name='subject'),
    path('deletesubject/<str:pk>/', views.DeleteSubject, name='deletesubject'),

    path('addtermparameter', views.TermParameterView, name='addtermparameter'),
    path('termparameterdetail/str<pk>/', views.TermParameterDetailView.as_view(), name='termparameterdetail'),
    path('edittermparameter/<str:pk>/', views.EditTermParameter, name='edittermparameter'),
    path('termparameter/', views.TermParameterIndexView.as_view(), name='termparameter'),
    path('deletetermparameter/<str:pk>/', views.DeleteTermParameter, name='deletetermparameter'),

    path('adddept', views.DeptView, name='adddept'),
    path('deptdetail/str<pk>/', views.DeptDetailView.as_view(), name='deptdetail'),
    path('editdept/<str:pk>/', views.EditDept, name='editdept'),
    path('dept/', views.DeptIndexView.as_view(), name='dept'),
    path('deletedept/<str:pk>/', views.DeleteDept, name='deletedept'),

    path('addfacility', views.FacilityView, name='addfacility'),
    path('facilitydetail/str<pk>/', views.FacilityDetailView.as_view(), name='facilitydetail'),
    path('editfacility/<str:pk>/', views.EditFacility, name='editfacility'),
    path('facility/', views.FacilityIndexView.as_view(), name='facility'),
    path('deletefacility/<str:pk>/', views.DeleteFacility, name='deletefacility'),

    path('addfacilityspace/str<pk>/', views.FacilitySpaceView, name='addfacilityspace'),
    path('addfacilityspace_a/', views.FacilitySpaceView1, name='addfacilityspace_a'),
    path('facilityspacedetail/str<pk>/', views.FacilitySpaceDetailView.as_view(), name='facilityspacedetail'),
    path('editfacilityspace/<str:pk>/', views.EditFacilitySpace, name='editfacilityspace'),
    path('facilityspace<str:pk>/', views.FacilitySpaceIndexView.as_view(), name='facilityspace'),
    # path('facilityspaceall/', views.FacilitySpaceAllIndexView.as_view(), name='facilityspaceall'),
    path('deletefacilityspace/<str:pk>/', views.DeleteFacilitySpace, name='deletefacilityspace'),

    path('addspaceslot/str<pk>/', views.SpaceSlotView, name='addspaceslot'),
    path('addspaceslot_a/', views.SpaceSlotView1, name='addspaceslot_a'),
    path('spaceslotdetail/str<pk>/', views.SpaceSlotDetailView.as_view(), name='spaceslotdetail'),
    path('editspaceslot/<str:pk>/', views.EditSpaceSlot, name='editspaceslot'),
    path('spaceslot<str:pk>/', views.SpaceSlotIndexView.as_view(), name='spaceslot'),
    # path('spaceslotall/', views.SpaceSlotAllIndexView.as_view(), name='spaceslotall'),
    path('deletespaceslot/<str:pk>/', views.DeleteSpaceSlot, name='deletespaceslot'),

    path('addsyllabus', views.SyllabusView, name='addsyllabus'),
    path('syllabusdetail/str<pk>/', views.SyllabusDetailView.as_view(), name='syllabusdetail'),
    path('editsyllabus/<str:pk>/', views.EditSyllabus, name='editsyllabus'),
    path('syllabus', views.SyllabusIndexView.as_view(), name='syllabus'),
    # path('syllabusall/', views.SyllabusAllIndexView.as_view(), name='syllabusall'),
    path('deletesyllabus/<str:pk>/', views.DeleteSyllabus, name='deletesyllabus'),

    path('addschemes/str<pk>/', views.SchemesView, name='addschemes'),
    path('addsubjschemes/str<lc_sb_code>/', views.SubSchemesView, name='addsubjschemes'),
    path('addschemes_a/', views.SchemesView1, name='addschemes_a'),
    path('schemesdetail/str<pk>/', views.SchemesDetailView.as_view(), name='schemesdetail'),
    path('editschemes/<str:pk>/', views.EditSchemes, name='editschemes'),
    path('schemes<str:pk>/', views.SchemesIndexView.as_view(), name='schemes'),
    # path('schemesall/', views.SchemesAllIndexView.as_view(), name='schemesall'),
    path('deleteschemes/<str:pk>/', views.DeleteSchemes, name='deleteschemes'),

    path('adddailyplan/str<pk>/', views.DailyPlanView, name='adddailyplan'),
    path('adddailyplan_a/', views.DailyPlanView1, name='adddailyplan_a'),
    path('dailyplandetail/str<pk>/', views.DailyPlanDetailView.as_view(), name='dailyplandetail'),
    path('editdailyplan/<str:pk>/', views.EditDailyPlan, name='editdailyplan'),
    path('dailyplan<str:pk>/', views.DailyPlanIndexView.as_view(), name='dailyplan'),
    # path('dailyplanall/', views.DailyPlanAllIndexView.as_view(), name='dailyplanall'),
    path('deletedailyplan/<str:pk>/', views.DeleteDailyPlan, name='deletedailyplan'),

    path('addcurrency', views.CurrencyView, name='addcurrency'),
    path('currencydetail/str<pk>/', views.CurrencyDetailView.as_view(), name='currencydetail'),
    path('editcurrency/<str:pk>/', views.EditCurrency, name='editcurrency'),
    path('currency/', views.CurrencyIndexView.as_view(), name='currency'),
    path('deletecurrency/<str:pk>/', views.DeleteCurrency, name='deletecurrency'),

    path('addstaffmember/str<pk>/', views.StaffMemberView, name='addstaffmember'),
    path('addstaffmember_a/', views.StaffMemberView1, name='addstaffmember_a'),
    path('staffmemberdetail/str<pk>/', views.StaffMemberDetailView.as_view(), name='staffmemberdetail'),
    path('editstaffmember/<str:pk>/', views.EditStaffMember, name='editstaffmember'),
    path('staffmember<str:pk>/', views.StaffMemberIndexView.as_view(), name='staffmember'),
    #path('staffmemberall/', views.StaffMemberAllIndexView.as_view(), name='staffmemberall'),
    path('deletestaffmember/<str:pk>/', views.DeleteStaffMember, name='deletestaffmember'),

    path('addstaffsubject/str<pk>/', views.StaffSubjectView, name='addstaffsubject'),
    path('addstaffsubject_a/', views.StaffSubjectView1, name='addstaffsubject_a'),
    path('staffsubjectdetail/str<pk>/', views.StaffSubjectDetailView.as_view(), name='staffsubjectdetail'),
    path('editstaffsubject/<str:pk>/', views.EditStaffSubject, name='editstaffsubject'),
    path('staffsubject<str:pk>/', views.StaffSubjectIndexView.as_view(), name='staffsubject'),
    # path('staffsubjectall/', views.staffsubjectAllIndexView.as_view(), name='staffsubjectall'),
    path('deletestaffsubject/<str:pk>/', views.DeleteStaffSubject, name='deletestaffsubject'),

    path('addlevel/str<pk>/', views.LevelView, name='addlevel'),
    path('leveldetail/str<pk>/', views.LevelDetailView.as_view(), name='leveldetail'),
    path('editlevel/<str:pk>/', views.EditLevel, name='editlevel'),
    path('level<str:pk>/', views.LevelIndexView.as_view(), name='level'),
    path('alllevels/', views.LevelListView.as_view(), name='alllevels'),
    path('deletelevel/<str:pk>/', views.DeleteLevel, name='deletelevel'),

    path('addschoolclass/str<pk>/', views.SchoolClassView, name='addschoolclass'),
    path('addschoolclass_a/', views.SchoolClassView1, name='addschoolclass_a'),
    path('schoolclassdetail/str<pk>/', views.SchoolClassDetailView.as_view(), name='schoolclassdetail'),
    path('editschoolclass/<str:pk>/', views.EditSchoolClass, name='editschoolclass'),
    path('schoolclass<str:pk>/', views.SchoolClassIndexView.as_view(), name='schoolclass'),
    path('regschoolclass/', views.SchoolClassRegIndexView.as_view(), name='regschoolclass'),
    # path('schoolclassall/', views.SchoolClassAllIndexView.as_view(), name='schoolclassall'),
    path('deleteschoolclass/<str:pk>/', views.DeleteSchoolClass, name='deleteschoolclass'),

    path('addlevelclass/str<pk>/', views.LevelClassView, name='addlevelclass'),
    path('levelclassdetail/str<pk>/', views.LevelClassDetailView.as_view(), name='levelclassdetail'),
    path('editlevelclass/<str:pk>/', views.EditLevelClass, name='editlevelclass'),
    path('classlevel<str:pk>/', views.LevelClassIndexView.as_view(), name='classlevel'),
    path('chlevelclassall/', views.LevelClassAllIndexView.as_view(), name='chlevelclassall'),
    path('deletelevelclass/<str:pk>/', views.DeleteLevelClass, name='deletelevelclass'),

    path('addscheme/str<pk>/', views.SchemesView, name='addscheme'),
    path('addchscheme/int<pk>/', views.ChSchemesView, name='addchscheme'),
    path('schemedetail/str<pk>/', views.SchemesDetailView.as_view(), name='schemedetail'),
    path('editscheme/<str:pk>/', views.EditSchemes, name='editscheme'),
    path('chscheme<int:pk>/', views.SchemesIndexView1.as_view(), name='chscheme'),
    path('scheme<str:pk>/', views.SchemesIndexView.as_view(), name='scheme'),
    path('r_schemes<str:pk>/', views.SchemesIndexView1.as_view(), name='r_schemes'),
    # path('schemeall/', views.SchemeAllIndexView.as_view(), name='schemeall'),
    path('deletescheme/<str:pk>/', views.DeleteSchemes, name='deletescheme'),

    path('adddailyplan/str<pk>/', views.DailyPlanView, name='adddailyplan'),
    path('dailyplandetail/str<pk>/', views.DailyPlanDetailView.as_view(), name='dailyplandetail'),
    path('editdailyplan/<str:pk>/', views.EditDailyPlan, name='editdailyplan'),
    path('dailyplan<str:pk>/', views.DailyPlanIndexView.as_view(), name='dailyplan'),
    # path('dailyplanall/', views.DailyPlanAllIndexView.as_view(), name='dailyplanall'),
    path('deletedailyplan/<str:pk>/', views.DeleteDailyPlan, name='deletedailyplan'),

    path('addclassmember/str<pk>/', views.ClassMemberView, name='addclassmember'),
    path('classmemberdetail/str<pk>/', views.ClassMemberDetailView.as_view(), name='classmemberdetail'),
    path('editclassmember/<str:pk>/', views.EditClassMember, name='editclassmember'),
    path('viewstudent/<mr_cm_num>/', views.EditClassMember1, name='viewstudent'),
    path('classmember<str:pk>/', views.ClassMemberIndexView.as_view(), name='classmember'),
    # path('classmemberall/', views.ClassMemberAllIndexView.as_view(), name='classmemberall'),
    path('deleteclassmember/<str:pk>/', views.DeleteClassMember, name='deleteclassmember'),

    path('addclassassessment/str<pk>/', views.ClassAssessmentView, name='addclassassessment'),
    path('classassessmentdetail/str<pk>/', views.ClassAssessmentDetailView.as_view(), name='classassessmentdetail'),
    path('editclassassessment/<str:pk>/', views.EditClassAssessment, name='editclassassessment'),
    path('classassessment<str:pk>/', views.ClassAssessmentIndexView.as_view(), name='classassessment'),
    # path('classassessmentall/', views.ClassAssessmentAllIndexView.as_view(), name='classassessmentall'),
    path('deleteclassassessment/<str:pk>/', views.DeleteClassAssessment, name='deleteclassassessment'),

    path('addlearnerassessment/str<pk>/', views.LearnerAssessmentView, name='addlearnerassessment'),
    path('learnerassessmentdetail/str<pk>/', views.LearnerAssessmentDetailView.as_view(),name='learnerassessmentdetail'),
    path('editlearnerassessment/<str:pk>/', views.EditLearnerAssessment, name='editlearnerassessment'),
    path('learnerassessment<str:pk>/', views.LearnerAssessmentIndexView.as_view(), name='learnerassessment'),
    # path('learnerassessmentall/', views.LearnerAssessmentAllIndexView.as_view(), name='learnerassessmentall'),
    path('deletelearnerassessment/<str:pk>/', views.DeleteLearnerAssessment, name='deletelearnerassessment'),

    path('addmemberregister/str<pk>/', views.MemberRegisterView, name='addmemberregister'),
    path('memberregisterdetail/str<pk>/', views.MemberRegisterDetailView.as_view(), name='memberregisterdetail'),
    path('editmemberregister/<str:pk>/', views.EditMemberRegister, name='editmemberregister'),
    path('viewattendee/<int:mr_num>/', views.EditMemberRegister1, name='viewattendee'),
    path('memberregister<str:pk>/', views.MemberRegisterIndexView.as_view(), name='memberregister'),
    # path('memberregisterall/', views.MemberRegisterAllIndexView.as_view(), name='memberregisterall'),
    path('deletememberregister/<str:pk>/', views.DeleteMemberRegister, name='deletememberregister'),

    path('ratesschoolclass/', views.SchoolClassRatesIndexView.as_view(), name='ratesschoolclass'),
    path('rateslevelclass/', views.LevelClassRatesIndexView.as_view(), name='rateslevelclass'),
    path('addratesschool/str<pk>/', views.ClassBillingView, name='addratesschool'),
    path('addrateslevel/str<pk>/', views.SubjectBillingView, name='addrateslevel'),
    path('ratesschool<str:pk>/', views.ClassBillingIndexView.as_view(), name='ratesschool'),
    path('rateslevel<str:pk>/', views.SubjectBillingIndexView.as_view(), name='rateslevel'),
    path('billgen/', views.GenBillView.as_view(), name='billgen'),

#Reports

    path('classlist', views.ClassListView, name='classlist'),
    path('schemeslist', views.SchemesListView, name='schemeslist'),
    path('dayplanlist/<str:sc_code>', views.DailyPlanListView, name='dayplanlist'),
    path('classassessmentlist/<str:sc_code>', views.ClassAssessmentListView, name='classassessmentlist'),
    path('learnerassesslist/<int:as_num>', views.LearnerAssessmentListView, name='learnerassesslist'),
    path('memberregister/<str:sc_code>', views.MemberRegisterListView, name='memberregister'),

    path('genscheme', views.GenSchemeView.as_view(), name='genscheme'),
    path('genregister', views.GenRegisterView.as_view(), name='genregister'),
    path('genclasseats', views.GenSeatsView.as_view(), name='genclasseats'),

    path('memberpay/<int:mr_num>/', views.MemberPayView,name='memberpay'),
    path('editmembrec/<int:mr_num>/', views.EditMemberRecordView, name='editmembrec'),
    path('receipt/<int:mr_num>/', views.ReceiptView, name='receipt'),

    path('snapshot', views.SnapShotView, name='snapshot'),
    path('paylist', views.PayListView, name='paylist'),
    path('g_position', views.g_position, name='g_position'),

#Subject Schedules

    path('subjsched', views.SubjectSchedView, name='subjsched'),
    path('classsched', views.SchClassSchedView, name='classsched'),
    path('staffsched', views.StaffSchedView, name='staffsched'),
    path('schemesched', views.SchmeSchedView, name='schemesched'),
    path('attendsched', views.MemberRegView, name='attendsched'),
    path('spacesched', views.SpacesView, name='spacesched'),
    path('studentacc/<int:mr_cm_num>/', views.StudentAccView, name='studentacc'),

 #   path('i_flash', views.InstFlashView, name='i_flash'),
  #  path('i_summary', views.HoldingInstSearchView, name='i_summary'),

   # path('r_summary', views.InstResourceView, name='r_summary'),
   # path('r_flash', views.InstResChartView, name='r_flash'),

  #  path('g_position_tab', views.MyOrdersView, name='g_position_tab'),
  #  path('g_position_tab1', views.OrdersHTMxTableView.as_view(), name='g_position_tab1'),
    #path('memberrecord_htmx', views.TransHTMxTable1, name='memberrecord_htmx'),

#Blog URLs

    path('bloghome', views.PostList.as_view(), name='bloghome'),
    path('blogadmin', views.PostListAdmin.as_view(), name='blogadmin'),
    #path('<slug:slug>/', views.PostDetail.as_view(), name='postdetail'),
    path('post_detail/<slug>/', views.Post_Detail, name='post_detail'),
    path('post_new/', views.post_new, name='post_new'),
    #path('post/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('post_edit/<slug>/', views.post_edit, name='post_edit'),
    path('post_remove/<slug>/', views.post_remove, name='post_remove'),
    path('cont_approve/<int:pk>/', views.cont_approve, name='cont_approve'),
    path('cont_remove/<int:pk>/', views.cont_remove, name='cont_remove'),

    #File uploads
  #  path('regionload', views.RegionsUploadView, name='regionload'),
  #  path('townupload', views.TownsUploadView, name='townupload'),
  #  path('distupload', views.DistrictsUploadView, name='distupload'),
  #  path('wardupload', views.WardsUploadView, name='wardupload'),
 ]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
 ]
