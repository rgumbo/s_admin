from django.db import models

# Create your models here.
from django.db import models
# from django import django.template.defaultfilters
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
#from slugify import slugify
from django.template.defaultfilters import slugify

# Term Parameters -  Class representing the Term Parameters for each year
class TermParameter(models.Model):
    status_choice = (('1', 'On'), ('2', 'Off'))
    schstatus_choice = (('0', 'Inactive'), ('1', 'Scheduled'), ('2', 'Processed'))
    billstatus_choice = (('N', 'No'), ('Y', 'Yes'))

    tp_num        = models.AutoField(verbose_name='Number', primary_key=True, help_text='System generated number uniquely identifying a Level Class')
    tp_year       = models.CharField(verbose_name='Year', max_length=4, help_text='Study Year')
    tp_term       = models.IntegerField(verbose_name='Term', help_text='The term of the year of study')
    tp_weeks      = models.IntegerField(verbose_name='Weeks',  default=0, help_text='Weeks in term', null=True, blank=True)
    tp_period_len = models.IntegerField(verbose_name='Period Length',  default=30, help_text='Length of period in minutes', null=True, blank=True)
    tp_days       = models.IntegerField(verbose_name='Days', default=0, help_text='Days in term', null=True, blank=True)
    tp_cycledays  = models.IntegerField(verbose_name=' Cycle Days', default=5, help_text='Days in Cycle', null=True, blank=True)
    tp_start_date = models.DateTimeField(verbose_name='Start Date', help_text='Opening Day')
    tp_end_date   = models.DateTimeField(verbose_name='End Date', help_text='Closng Day')
    tp_status     = models.CharField(verbose_name='Status', max_length=1, choices=status_choice, default='1', help_text='Status')
    tp_schemed    = models.CharField(verbose_name='Schemed?', max_length=1, choices=schstatus_choice, default='0', help_text='Schemed')
    tp_billed    = models.CharField(verbose_name='Billed ?', max_length=1, choices=billstatus_choice, default='N', help_text='Billed')
    ad_user_c     = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a     = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c     = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a     = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c   = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a   = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['tp_year','tp_term']
        verbose_name = 'Term'

    def __str__(self):
        return self.tp_year

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.tp_year)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#Currency Class - class representing the Package type e.g each, cartoon,case,litres, kgs
class Currency(models.Model):
    cu_status_choices = (('1', 'Active'), ('0', 'Inactive'))
    cu_base_choices = (('Y', 'Home Currency'), ('1', 'Currency 1'), ('2', 'Currency 1'))

    cu_num = models.AutoField(verbose_name='Currecny ID',primary_key=True, help_text='Code uniquely identify a Currecny')
    cu_code = models.CharField(verbose_name='Code',max_length=3, help_text='The currency Code')
    cu_name = models.CharField(verbose_name='Currency Name',max_length=100, help_text='Currency Name')
    cu_base = models.CharField(verbose_name='Base Currency ?',max_length=1,choices=cu_base_choices, default='N', help_text='Indicates whether the currency is the base currency')
    cu_rate = models.DecimalField(verbose_name='Rate to base',max_digits=15, decimal_places=2, help_text='Rate to base',default=0)
    cu_valid_from = models.DateTimeField(verbose_name='Valid From',help_text='Date date from which rate is valid')
    cu_status = models.CharField(verbose_name='Status',max_length=1, choices=cu_status_choices, help_text='Status of the currency', default='1')
    ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['cu_code']
        verbose_name = 'Currency'

    def __str__(self):
        return self.cu_name

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.cu_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#Dept -  Class representing the departments

class Dept(models.Model):
    dp_status_choices = (('1', 'Active'), ('0', 'Inactive'))

    dp_code = models.CharField(verbose_name='Code',max_length=10,primary_key=True, help_text='Code uniquely identify a department')
    dp_name = models.CharField(verbose_name='name',max_length=10, help_text='The name of department')
    dp_status = models.CharField(verbose_name='Status',max_length=1, choices=dp_status_choices, help_text='Status of the currency', default='1')
    ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['dp_code']
        verbose_name = 'Department'

    def __str__(self):
        return self.dp_name

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.dp_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

# StaffMember -  Class representing the Staff Members
class StaffMember(models.Model):
    app_status_type_choice = (('1', 'Academic'), ('2', 'Sport'), ('3', 'Extra Carricular'))
    status_choice = (('1', 'Applicant'), ('2', 'Engaged'), ('3', 'Discharged'), ('4', 'Pending'), ('5', 'On Leave'))
    gender_choice = (('F', 'Female'), ('M', 'Male'))

    sf_num = models.AutoField(verbose_name='Member ID', primary_key=True,help_text='Code uniquely identify a Staff Member')
    sf_dp_code = models.ForeignKey(Dept,on_delete=models.CASCADE,verbose_name='Department', help_text='Staff member s department')
    sf_surname = models.CharField(verbose_name='Surame', max_length=100, help_text='Staff Member Surname')
    sf_fname = models.CharField(verbose_name='First Name', max_length=100, help_text='Staff Member First Name')
    sf_othername = models.CharField(verbose_name='Other Name', max_length=100, help_text='Staff Member s Other Name')
    sf_nok = models.CharField(verbose_name='Next Of Kin', max_length=100, help_text='Staff Member s next of kin')
    sf_phone = models.CharField(verbose_name='Phone', max_length=100, help_text='Contact phone')
    sf_email = models.CharField(verbose_name='Email', max_length=100, help_text='Contact Email')
    sf_dob = models.DateTimeField(verbose_name='Date Of Birth', help_text='Date of birth')
    sf_doj = models.DateTimeField(verbose_name='Date joined', help_text='Date Joined')
    sf_dol = models.DateTimeField(verbose_name='Date of Leaving', help_text='Date of leaving')
    sf_status = models.CharField(verbose_name='Status', max_length=1, choices=status_choice, default='1', help_text='Status')
    sf_gender = models.CharField(verbose_name='Gender', max_length=1, choices=gender_choice, default='1', help_text='Gender')
    sf_app_status = models.CharField(verbose_name='Staff Type', max_length=1, choices=app_status_type_choice, default='1', help_text='Indicates Tyoe e.g. Academic')
    ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['sf_surname']
        verbose_name = 'Staff Member'

    def __str__(self):
        return self.sf_surname

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.sf_surname)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#Subject - class representing the Subjects offerred
class Subject(models.Model):
    type_choice		=	(('1','Academic'),('2', 'Sport'),('3', 'Extra Carricular'))
    status_choice	=	(('1', 'On'),('2' , 'Off'))

    sb_code		=	models.CharField(verbose_name='Code', max_length=10, primary_key=True, help_text='User assigned code for the Subject')
    sb_type		=	models.CharField(verbose_name='Type', max_length=1,choices=type_choice, help_text='Type of the Subject')
    sb_desc		=	models.CharField(verbose_name='Name', max_length=100, help_text='The description of the Subject')
    sb_hrs		=	models.DecimalField(verbose_name='Req. Hrs',max_digits=10, decimal_places=2, default=0, help_text='Required hrs for Subject', null=True, blank=True)
    sb_status	=	models.CharField(verbose_name='Status', max_length=1,choices=status_choice,default='1', help_text='Status')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['sb_code']
        verbose_name = 'Subject'

    def __str__(self):
        return self.sb_desc

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.sb_desc)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})
#Level - class representing the Levels of study per subject
class Level(models.Model):
    lv_status_choices = (('1', 'Active'), ('0', 'Inactive'))

    lv_code = models.CharField(verbose_name='Code',primary_key=True,max_length=10, help_text='The Level Code - Primary key for the table')
    lv_name = models.CharField(verbose_name='Level Name',max_length=100, help_text='Leval Name')
    lv_sb_code	=	models.ForeignKey(Subject,on_delete=models.CASCADE,verbose_name='Subject', help_text='The subject for the study level')
    lv_status = models.CharField(verbose_name='Status',max_length=1, choices=lv_status_choices, help_text='Status of the Level', default='1')
    ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['lv_code']
        verbose_name = 'Level'

    def __str__(self):
        return self.lv_name

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.lv_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#SchoolClass -  Class representing a School Class
class SchoolClass(models.Model):
    type_choice		=	(('1','Academic'),('2', 'Sport'),('3', 'Extra Carricular'))
    status_choice	=	(('1', 'On'),('2' , 'Off'))

    sc_code		=	models.CharField(verbose_name='Code', max_length=10, primary_key=True, help_text='User assigned code for the Class Level')
    sc_lv_code	=	models.ForeignKey(Level,on_delete=models.CASCADE,verbose_name='Level', help_text='Foreign key to Level')
    sc_sf_num   = models.ForeignKey(StaffMember, on_delete=models.CASCADE, verbose_name='Staff Member', blank=True, null=True, help_text='Staff member assigned')
    sc_type		=	models.CharField(verbose_name='Type', max_length=1,choices=type_choice, help_text='Type of the School Class')
    sc_desc		=	models.CharField(verbose_name='Name', max_length=100, help_text='The description of the School Class')
    sc_status	=	models.CharField(verbose_name='Status', max_length=1,choices=status_choice,default='1', help_text='Status')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['sc_code']
        verbose_name = 'School Class'

    def __str__(self):
        return self.sc_desc

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.sc_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

# LevelClass -  Class representing the class for each level of study and the subject
class LevelClass(models.Model):
    type_choice = (('1', 'Academic'), ('2', 'Sport'), ('3', 'Extra Carricular'))
    status_choice = (('1', 'On'), ('2', 'Off'))
    scheme_choice = (('N', 'No'), ('Y', 'Yes'))

    lc_num     = models.AutoField(verbose_name='Number', primary_key=True, help_text='System generated number uniquely identifying a Level Class')
    lc_sc_code = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name='School Class',help_text='Foreign key to SchoolClass')
    lc_lv_code = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='Level', help_text='Foreign key to Level')
    lc_sb_code = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Subject', help_text='Foreign key to Subject')
    lc_sf_num  = models.ForeignKey(StaffMember, on_delete=models.CASCADE, verbose_name='Staff Member', help_text='Staff member assigned')
    lc_type    = models.CharField(verbose_name='Type', max_length=1, choices=type_choice, help_text='Type of the Subject')
    lc_desc    = models.CharField(verbose_name='Name', max_length=100, help_text='The description of the Subject')
    lc_hrs     = models.DecimalField(verbose_name='Req. Hrs', max_digits=10, decimal_places=2, default=0,  help_text='Required hrs for Subject', null=True, blank=True)
    lc_status  = models.CharField(verbose_name='Status', max_length=1, choices=status_choice, default='1', help_text='Status')
    lc_scheme_status  = models.CharField(verbose_name='Scheme Status', max_length=1, choices=scheme_choice, default='N', help_text='Indicates whether a scheme has been generated')
    ad_user_c  = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a  = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c  = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a  = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['lc_num']
        verbose_name = 'Level Class'

    def __str__(self):
        return self.lc_desc

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.lc_desc)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

# ClassMember -  Class representing the class for each Class Member
class ClassMember(models.Model):
    app_status_type_choice = (('1', 'Academic'), ('2', 'Sport'), ('3', 'Extra Carricular'))
    status_choice = (('1', 'On'), ('2', 'Suspended'), ('3', 'Expelled'))
    gender_choice = (('F', 'Female'), ('M', 'Male'))

    cm_num = models.AutoField(verbose_name='Number', primary_key=True, help_text='System generated number uniquely identifying a Class Member')
    cm_sc_code = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name='School Class', help_text='Foreign key to SchoolClass')
    cm_lv_code = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='Level', help_text='Foreign key to Level')
    cm_surname = models.CharField(verbose_name='Surname', max_length=100, help_text='Class Member Surname')
    cm_fname = models.CharField(verbose_name='First Name', max_length=100, help_text='Class Member First Name')
    cm_otherName = models.CharField(verbose_name='Other Name', max_length=100, help_text='Class Member s Other Name')
    cm_guardian = models.CharField(verbose_name='Guardian', max_length=100, help_text='Class Member s Guardian')
    cm_phone = models.CharField(verbose_name='Phone', max_length=100, help_text='Contact phone')
    cm_email = models.CharField(verbose_name='Email', max_length=100, help_text='Contact Email')
    cm_dob = models.DateTimeField(verbose_name='Date Of Birth', help_text='Date of birth')
    cm_gender = models.CharField(verbose_name='Gender', max_length=1, choices=gender_choice, default='F', help_text='Gender')
    cm_doj = models.DateTimeField(verbose_name='Date joined', help_text='Date Joined')
    cm_dol = models.DateTimeField(verbose_name='Date of Leaving', help_text='Date of leaving')
    cm_status = models.CharField(verbose_name='Status', max_length=1, choices=status_choice, default='1', help_text='Status')
    cm_app_status = models.CharField(verbose_name='Status', max_length=1, choices=app_status_type_choice, default='1',help_text='Status')
    ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['cm_surname']
        verbose_name = 'Class Member'

    def __str__(self):
        return self.cm_surname

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.cm_surname)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

class MemberRegister(models.Model):
    status_choice  = (('1', 'On'), ('2', 'Suspended'), ('3', 'Expelled'))
    mark_choice    = (('P', 'Present'), ('S', 'Sick'), ('A', 'Absent'))

    mr_num        = models.AutoField(verbose_name='Number', primary_key=True, help_text='System generated number uniquely identifying a register record')
    mr_cm_num     = models.ForeignKey(ClassMember, on_delete=models.CASCADE,verbose_name='Student',help_text='The Student')
    mr_sc_code    = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name='School Class', help_text='Foreign key to SchoolClass')
    mr_year         = models.CharField(verbose_name='Year', max_length=4, help_text='Study Year')
    mr_term         = models.IntegerField(verbose_name='Term', help_text='The term of the year of study')
    mr_comment    = models.CharField(verbose_name='Other Name', max_length=100, help_text='Class Member s Other Name')
    mr_date       = models.DateTimeField(verbose_name='Date', help_text='The date of attendance')
    mr_day        = models.IntegerField(verbose_name='Day Number', help_text='The day number')
    mr_mark       = models.CharField(verbose_name='Marked', max_length=1, choices=mark_choice, default='P', help_text='Marked Indicator')
    mr_status     = models.CharField(verbose_name='Status', max_length=1, choices=status_choice, default='1', help_text='Status')
    ad_user_c     = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a     = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c     = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a     = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c   = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a   = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['mr_cm_num']
        verbose_name = 'Member Register'

    def __str__(self):
        return self.mr_mark

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.mr_mark)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

# LevelClassInstance -  Class representing the class for each instance of a class of study
class LevelClassInstance(models.Model):
    type_choice = (('1', 'Academic'), ('2', 'Sport'), ('3', 'Extra Carricular'))
    status_choice = (('1', 'On'), ('2', 'Off'))

    ci_num = models.AutoField(verbose_name='Number', primary_key=True, help_text='System generated number uniquely identifying a Class Instance')
    ci_lc_num = models.ForeignKey(LevelClass, on_delete=models.CASCADE,verbose_name='Level Class' ,help_text='The Level Class')
    ci_sc_code = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name='School Class', help_text='Foreign key to School Class')
    ci_lv_code = models.ForeignKey(Level, on_delete=models.CASCADE, verbose_name='Level', help_text='Foreign key to Level')
    ci_sb_code = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name='Subject',help_text='Foreign key to Subject')
    ci_type = models.CharField(verbose_name='Type', max_length=1, choices=type_choice, help_text='Type of the Subject')
    ci_desc = models.CharField(verbose_name='Name', max_length=100, help_text='The description of the Subject')
    ci_hrs = models.DecimalField(verbose_name='Req. Hrs', max_digits=10, decimal_places=2, default=0,help_text='Required hrs for Subject', null=True, blank=True)
    ci_status = models.CharField(verbose_name='Status', max_length=1, choices=status_choice, default='1', help_text='Status')
    ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['ci_num']
        verbose_name = 'Level Class Instance'

    def __str__(self):
        return self.ci_sc_code

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.ci_sc_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#Syllabus - class representing the Syllabus for the Subject offered
class Syllabus(models.Model):
    type_choice   = (('1','Academic'),('2', 'Sport'),('3', 'Extra Curricular'))
    type1_choice  = (('1','Zim Sec'),('2', 'Cambridge'))
    status_choice = (('1', 'On'),('2' , 'Off'))

    sy_code       = models.CharField(verbose_name='Code', max_length=10, primary_key=True, help_text='User assigned code for the Subject')
    sb_ex_board   = models.CharField(verbose_name='Exam Board', max_length=1,choices=type1_choice,default='1', help_text='Examination Board')
    sy_lv_code    = models.ForeignKey(Level,on_delete=models.CASCADE,verbose_name='Level',help_text='The Study Level')
    sy_sb_code    = models.ForeignKey(Subject,on_delete=models.CASCADE,verbose_name='Subject', help_text='The subject for the study level')
    sy_type       = models.CharField(verbose_name='Type', max_length=1,choices=type_choice, help_text='Type of the Syllabus')
    sy_desc       = models.CharField(verbose_name='Description', max_length=100, help_text='The description of the Subject')
    sy_eff_date   = models.DateTimeField(verbose_name='Effetive Date', help_text='Effetive Date', null=True, blank=True)
    sb_status     = models.CharField(verbose_name='Status', max_length=1,choices=status_choice,default='1', help_text='Status')
    ad_user_c     = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a     = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c     = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a     = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c   = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a   = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['sy_code']
        verbose_name = 'Syllabus'

    def __str__(self):
        return self.sy_desc

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.sy_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#Schemes - class representing the Schemes for the Subject offered
class Schemes(models.Model):
    type_choice   = (('1','Academic'),('2', 'Sport'),('3', 'Extra Curricular'))
    type1_choice  = (('1','Zim Sec'),('2', 'Cambridge'))
    status_choice = (('0', 'New'),('1', 'Done'), ('2' , 'Pending'), ('3', 'Cancelled'))

    ch_num          = models.AutoField(verbose_name='Number',primary_key=True, help_text='Unique identifier for the scheme')
    ch_lc_num       = models.ForeignKey(LevelClass, on_delete=models.CASCADE, verbose_name='Level Class',help_text='Level Class')
    ch_sc_code      = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name='School Class',help_text='Foreign key to School Class')
    ch_sf_num       = models.ForeignKey(StaffMember, on_delete=models.CASCADE, verbose_name='Staff Member', help_text='Staff member assigned')
    ch_lv_code      = models.ForeignKey(Level ,on_delete=models.CASCADE,verbose_name='Level',help_text='The Study Level')
    ch_sb_code      = models.ForeignKey(Subject,on_delete=models.CASCADE,verbose_name='Subject', help_text='The subject for the study level')
    ch_sy_code      = models.ForeignKey(Syllabus,on_delete=models.CASCADE,verbose_name='Syllabus', help_text='The syllabus for subject of the study level')
    ch_ex_board     = models.CharField(verbose_name='Exam Board', max_length=1,choices=type1_choice,default='1', help_text='Examination Board')
    ch_year         = models.CharField(verbose_name='Year', max_length=4, help_text='Study Year')
    ch_term         = models.IntegerField(verbose_name='Term', help_text='The term of the year of study')
    ch_week         = models.IntegerField(verbose_name='Week', null=True, blank=True, help_text='Week covered')
    ch_type         = models.CharField(verbose_name='Type', max_length=1,blank=True, null=True,choices=type_choice, help_text='Type of the Syllabus')
    ch_topic        = models.CharField(verbose_name='Topic', max_length=100, blank=True, null=True,help_text='The Topic covered')
    ch_references   = models.CharField(verbose_name='Sources', max_length=100,blank=True, null=True, help_text='The sources of materials')
    ch_objectives   = models.CharField(verbose_name='Objetives', max_length=100,blank=True, null=True, help_text='The objectives for the period')
    ch_competencies = models.CharField(verbose_name='Competencies', max_length=100,blank=True, null=True, help_text='The competencies to be acquired')
    ch_methods      = models.CharField(verbose_name='Methods', max_length=100,blank=True, null=True, help_text='The methods to be used')
    ch_evaluation   = models.CharField(verbose_name='Evaluation', max_length=100,blank=True, null=True, help_text='The Evaluation')
    ch_review1      = models.CharField(verbose_name='Review1', max_length=100, help_text='The first reviewer')
    ch_review2      = models.CharField(verbose_name='Review2', max_length=100,blank=True, null=True, help_text='The second reviewer')
    ch_eff_date     = models.DateTimeField(verbose_name='Effetive Date',help_text='Effetive Date', null=True, blank=True)
    ch_status       = models.CharField(verbose_name='Status', max_length=1,choices=status_choice,default='0', help_text='Status')
    ad_user_c       = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a       = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c       = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a       = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c     = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a     = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c   = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a   = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['ch_num']
        verbose_name = 'Schemes'

    def __str__(self):
        return self.ch_topic or ' '

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.ch_topic)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#DailyPlan - class representing the Daily Plan for the Subject offered
class DailyPlan(models.Model):
    type_choice   = (('1','Academic'),('2', 'Sport'),('3', 'Extra Curricular'))
    absorb_choice  = ((80,'more than 80 %'),(75, '75 %'),(50, '50 %'),(25, 'Less than 25 %'))
    status_choice = (('0', 'Planned'),('1' , 'Delivered'),('2' , 'Deferred'),('W', 'Weekend'))

    sp_num         = models.AutoField(verbose_name='Number', primary_key=True, help_text='Unique identifier for the daily plan')
    sp_ch_num      = models.ForeignKey(Schemes, on_delete=models.CASCADE,verbose_name='Scheme',help_text='Scheme Plan')
    sp_lc_num      = models.ForeignKey(LevelClass, on_delete=models.CASCADE, verbose_name='Level Class', help_text='Level Class')
    sp_sc_code     = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, verbose_name='School Class',help_text='Foreign key to School Class')
    sp_sb_code     = models.ForeignKey(Subject,on_delete=models.CASCADE,verbose_name='Subject', help_text='The subject for the study level')
    sp_year        = models.CharField(verbose_name='Year', max_length=4, help_text='Study Year')
    sp_term        = models.IntegerField(verbose_name='Term', help_text='The term of the year of study')
    sp_cycle       = models.IntegerField(verbose_name='Cycle', null=True, blank=True, help_text='Cycle of the session')
    sp_day         = models.IntegerField(verbose_name='day', null=True, blank=True, help_text='Day of the session')
    sp_start_time  = models.TimeField(verbose_name='Start Time', null=True, blank=True, help_text='Starting Time')
    sp_finish_time = models.TimeField(verbose_name='Finish Time', null=True, blank=True, help_text='Finishing Time')
    sp_hrs         = models.DecimalField(verbose_name='Req. Hrs', max_digits=10, decimal_places=2, default=0,help_text='Duration', null=True, blank=True)
    sp_area        = models.CharField(verbose_name='Type', max_length=1,choices=type_choice, help_text='Type of the Syllabus', null=True, blank=True)
    sp_topic       = models.CharField(verbose_name='Topic', max_length=100, help_text='The Topic covered', null=True, blank=True)
    sp_objective   = models.CharField(verbose_name='Objetives', max_length=100, help_text='The objectives for the period', null=True, blank=True)
    sp_absorption  = models.CharField(verbose_name='Methods', max_length=100, help_text='The methods to be used', null=True, blank=True)
    sp_paction     = models.IntegerField(verbose_name='Post Action', choices=absorb_choice, help_text='Follow on action post delivery', null=True, blank=True)
    sp_top         = models.CharField(verbose_name='Top Group', max_length=100, help_text='Upper Group Members', null=True, blank=True)
    sp_middle      = models.CharField(verbose_name='Normal Group', max_length=100, help_text='Normal Group Members', null=True, blank=True)
    sp_lower       = models.CharField(verbose_name='Lower Group', max_length=100, help_text='Lower Group Members', null=True, blank=True)
    sp_del_date    = models.DateTimeField(verbose_name='Delivery Date', help_text='Date of execution of lesson', null=True, blank=True)
    sp_plan_date   = models.DateTimeField(verbose_name='Planned Date', help_text='Planned date of execution of lesson', null=True, blank=True)
    sp_status      = models.CharField(verbose_name='Status', max_length=1,choices=status_choice,default='0', help_text='Status')
    sp_type        = models.CharField(verbose_name='Type', max_length=1,choices=type_choice,default='1', help_text='Type')
    ad_user_c      = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a      = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c      = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a      = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c    = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a    = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c  = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a  = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['sp_num']
        verbose_name = 'DailyPlan'

    def __str__(self):
        return self.sp_type

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.sp_type)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

# ClassAssessment -  Class representing the assessments given to a class
class ClassAssessment(models.Model):
    type_choice = (('1', 'Homework'), ('2', 'Tests'), ('3', 'End Of Session Exam'))
    status_choice = (('1', 'On'), ('2', 'Off'))

    as_num = models.AutoField(verbose_name='Number', primary_key=True, help_text='System generated number uniquely identifying an Assessment')
    as_lc_num = models.ForeignKey(LevelClass, on_delete=models.CASCADE,related_name='level_key',verbose_name='Level Class' ,help_text='The Level Class')
    as_sc_code = models.ForeignKey(SchoolClass, on_delete=models.CASCADE,related_name='sc_key', verbose_name='School Class', help_text='Foreign key to School Class')
    as_ch_num = models.ForeignKey(Schemes, on_delete=models.CASCADE,related_name='ch_key', verbose_name='Scheme', blank=True, null=True, help_text='Foreign key to Schemes')
    as_sb_code = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='sb_key', verbose_name='Subject',help_text='Foreign key to Subject')
    as_type = models.CharField(verbose_name='Type', max_length=1, choices=type_choice, help_text='Type of the assessment')
    as_name = models.CharField(verbose_name='Name', max_length=100, help_text='Name of the assessment')
    as_remark = models.CharField(verbose_name='Remark', max_length=100, help_text='Any remarks')
    as_exception = models.CharField(verbose_name='Exceptions', max_length=100, help_text='Exceptions noted')
    as_comment = models.CharField(verbose_name='Comment', max_length=100, help_text='Any comments')
    as_review = models.CharField(verbose_name='Review', max_length=100, help_text='Review of the assessment')
    as_resources = models.CharField(verbose_name='Resources', max_length=100, help_text='Resource requirements')
    as_trans_date = models.DateTimeField(verbose_name='Trans Date',help_text='Date to be taken')
    as_status = models.CharField(verbose_name='Status', max_length=1, choices=status_choice, default='1', help_text='Status')
    ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['as_num']
        verbose_name = 'Class Assessment'

    def __str__(self):
        return self.as_name

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.as_name)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

# Learner Assessment -  Class representing the assessment taken by learners
class LearnerAssessment(models.Model):
    type_choice = (('1', 'Academic'), ('2', 'Sport'), ('3', 'Extra Carricular'))
    status_choice = (('1', 'On'), ('2', 'Off'))

    la_num = models.AutoField(verbose_name='Number', primary_key=True, help_text='Unique identifier for a Learner Assessment')
    la_as_num = models.ForeignKey(ClassAssessment, on_delete=models.CASCADE,related_name='la_as_num', verbose_name='Assessment', help_text='Student s assessment')
    la_cm_num = models.ForeignKey(ClassMember, on_delete=models.CASCADE,related_name='la_cm_key',verbose_name='Student' ,help_text='The Student')
    la_lc_num = models.ForeignKey(LevelClass, on_delete=models.CASCADE,related_name='la_lc_key',verbose_name='Level Class' ,help_text='The Level Class')
    la_sc_code = models.ForeignKey(SchoolClass, on_delete=models.CASCADE,related_name='la_sc_key', verbose_name='School Class', help_text='Foreign key to School Class')
    la_sb_code = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='la_sb_key',blank=True, null=True, verbose_name='Subject',default=1,help_text='Subject of study')
    la_type = models.CharField(verbose_name='Type', max_length=1, choices=type_choice, help_text='Type of the Subject')
    la_remark = models.CharField(verbose_name='Remark', max_length=100, help_text='The remark on the Learner Assessment')
    la_comment = models.CharField(verbose_name='Comment', max_length=100, help_text='Comment on the Learner Assessment')
    la_mark_f = models.DecimalField(verbose_name='Forcast Mark', max_digits=5, decimal_places=2, default=0,help_text='Forecasted mark', null=True, blank=True)
    la_grade_f = models.CharField(verbose_name='Forcast Grade', max_length=5, help_text='Forcast grade')
    la_mark_a = models.DecimalField(verbose_name='Actual Mark', max_digits=5, decimal_places=2, default=0,help_text='Actual mark', null=True, blank=True)
    la_grade_a = models.CharField(verbose_name='Actual Grade', max_length=5, help_text='Actual grade')
    la_status = models.CharField(verbose_name='Status', max_length=1, choices=status_choice, default='1', help_text='Status')
    ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['la_num']
        verbose_name = 'Learner Assessment'

    def __str__(self):
        return self.la_type

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.la_type)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#StaffSubject Class - class representing the subjects the staff member is competent to take

class StaffSubject(models.Model):
    ss_status_choices = (('1', 'Active'), ('0', 'Inactive'))

    ss_num = models.AutoField(verbose_name='Number',primary_key=True, help_text='Code uniquely identify a record')
    ss_sf_num	=	models.ForeignKey(StaffMember,on_delete=models.CASCADE,verbose_name='Staff Member', help_text='Staff Member')
    ss_sb_code	=	models.ForeignKey(Subject,on_delete=models.CASCADE,verbose_name='Subject', help_text='Foreign key to Subject')
    ss_lv_code	=	models.ForeignKey(Level,on_delete=models.CASCADE,verbose_name='Up to Level', help_text='Teaches up to level ?')
    ss_status   = models.CharField(verbose_name='Status',max_length=1, choices=ss_status_choices, help_text='Status of the currency', default='1')
    ad_user_c   = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a   = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c   = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a   = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['ss_sb_code']
        verbose_name = 'Staff Subject'

    def __str__(self):
        return self.ss_status

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.ss_status)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#Facility Class - class representing the Facility

class Facility(models.Model):
    fc_status_choices = (('1', 'Active'), ('0', 'Inactive'))
    fc_type_choices = (('1', 'Academic'), ('2', 'Residential'),('3', 'Other'))

    fc_num = models.AutoField(verbose_name='Currency ID',primary_key=True, help_text='Code uniquely identify a facility')
    fc_code = models.CharField(verbose_name='Code',max_length=10, help_text='The facility Code')
    fc_name = models.CharField(verbose_name='Name',max_length=100, help_text='The facility s Name')
    fc_desc = models.CharField(verbose_name='Description',max_length=100, help_text='The facility s Description')
    fc_status = models.CharField(verbose_name='Status',max_length=1, choices=fc_status_choices, help_text='Status of the facility', default='1')
    fc_type = models.CharField(verbose_name='Type',max_length=1, choices=fc_type_choices, help_text='Type of the facility', default='1')
    ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['fc_code']
        verbose_name = 'Facility'

    def __str__(self):
        return self.fc_name

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.fc_name)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

# FacilitySpace -  Class representing the FacilitySpace in FacilitySpace
class FacilitySpace(models.Model):
    status_choice = (('1', 'On'), ('2', 'Off'))

    fs_num = models.AutoField(verbose_name='Number', primary_key=True, help_text='System generated number uniquely identifying a FacilitySpace')
    fs_fc_num = models.ForeignKey(Facility, on_delete=models.CASCADE, verbose_name='Facility', help_text='Foreign key to Facility')
    fs_desc = models.CharField(verbose_name='Name', max_length=100, help_text='The description of the space')
    fs_status = models.CharField(verbose_name='Status', max_length=1, choices=status_choice, default='1', help_text='Status')
    ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['fs_num']
        verbose_name = 'Facility Space'

    def __str__(self):
        return self.fs_desc

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.fs_desc)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

# SpaceSlot -  Class representing the Slot for each Space of the Facility
class SpaceSlot(models.Model):
    type_choice = (('1', 'Academic'), ('2', 'Sport'), ('3', 'Extra Carricular'))
    status_choice = (('1', 'On'), ('2', 'Off'))

    sp_num = models.AutoField(verbose_name='Number', primary_key=True, help_text='System generated number uniquely identifying a Level Class')
    sp_fs_num = models.ForeignKey(FacilitySpace, on_delete=models.CASCADE, verbose_name='Facility', help_text='Foreign key to Facility')
    sp_type = models.CharField(verbose_name='Type', max_length=1, choices=type_choice, help_text='Type of the Subject')
    sp_desc = models.CharField(verbose_name='Name', max_length=100, help_text='The description of the Subject')
    sp_hrs = models.DecimalField(verbose_name='Duration', max_digits=10, decimal_places=2, default=0, help_text='Duration of the slot', null=True, blank=True)
    sp_fromtime = models.DateTimeField(verbose_name='From Time', help_text='Required hrs for Subject', null=True,blank=True)
    sp_totime = models.DateTimeField(verbose_name='To Time', help_text='Required hrs for Subject', null=True, blank=True)
    sp_status = models.CharField(verbose_name='Status', max_length=1, choices=status_choice, default='1',help_text='Status')
    ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['sp_num']
        verbose_name = 'Space Slot'

    def __str__(self):
        return self.sp_desc

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.sp_desc)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

# ClassBilling -  Class representing the fees bill for each class
class ClassBilling(models.Model):
    type_choice = (('1', 'Academic'), ('2', 'Sport'), ('3', 'Extra Carricular'), ('4', 'Practical'))
    status_choice = (('1', 'On'), ('2', 'Off'))

    cb_num        = models.AutoField(verbose_name='Number', primary_key=True, help_text='System generated number uniquely identifying a Level Class')
    cb_sc_code    = models.ForeignKey(SchoolClass, on_delete=models.CASCADE,related_name='cb_sc', verbose_name='School Class',blank=True, null=True,help_text='Foreign key to SchoolClass')
    cb_lv_code    = models.ForeignKey(Level, on_delete=models.CASCADE,related_name='cb_lv', verbose_name='Level',blank=True, null=True, help_text='Foreign key to Level')
    cb_type       = models.CharField(verbose_name='Type', max_length=1, choices=type_choice,default='1', help_text='Type of the Subject')
    cb_desc       = models.CharField(verbose_name='Name', max_length=100, help_text='The description of the Rate')
    cb_rate       = models.DecimalField(verbose_name='Rate', max_digits=10, decimal_places=2, default=0,  help_text='Rate', null=True, blank=True)
    cb_year       = models.CharField(verbose_name='Year', max_length=4,blank=True, null=True, help_text='Study Year')
    cb_term       = models.IntegerField(verbose_name='Term',blank=True, null=True, help_text='The term of the year of study')
    cb_status     = models.CharField(verbose_name='Status', max_length=1, choices=status_choice, default='1', help_text='Status')
    ad_user_c     = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a     = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c     = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a     = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c   = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a   = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['cb_num']
        verbose_name = 'ClassBilling'

    def __str__(self):
        return self.cb_desc

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.cb_desc)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

# SubjectBilling -  Class representing the fees billing for each class and subject specific
class SubjectBilling(models.Model):
    type_choice = (('1', 'Academic'), ('2', 'Sport'), ('3', 'Extra Carricular'), ('4', 'Practical'))
    status_choice = (('1', 'On'), ('2', 'Off'))

    jb_num        = models.AutoField(verbose_name='Number', primary_key=True, help_text='System generated number uniquely identifying a Level Class')
    jb_lc_num     = models.ForeignKey(LevelClass, on_delete=models.CASCADE,related_name='jb_lc', verbose_name='Level Class',blank=True, null=True, help_text='Foreign key to Level Class')
    jb_sc_code    = models.ForeignKey(SchoolClass, on_delete=models.CASCADE,related_name='jb_sc', verbose_name='School Class',blank=True, null=True,help_text='Foreign key to SchoolClass')
    jb_lv_code    = models.ForeignKey(Level, on_delete=models.CASCADE,related_name='jb_lv', verbose_name='Level',blank=True, null=True, help_text='Foreign key to Level')
    jb_sb_code    = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='jb_sb', verbose_name='Subject',blank=True, null=True, help_text='Foreign key to Subject')
    jb_type       = models.CharField(verbose_name='Type', max_length=1, choices=type_choice,default='1', help_text='Type of the Subject')
    jb_desc       = models.CharField(verbose_name='Name', max_length=100, help_text='The description of the billing head')
    jb_rate       = models.DecimalField(verbose_name='Rate', max_digits=10, decimal_places=2, default=0,  help_text='Rate', null=True, blank=True)
    jb_status     = models.CharField(verbose_name='Status', max_length=1, choices=status_choice, default='1', help_text='Status')
    jb_year       = models.CharField(verbose_name='Year', max_length=4,blank=True, null=True, help_text='Study Year')
    jb_term       = models.IntegerField(verbose_name='Term', blank=True, null=True,help_text='The term of the year of study')
    ad_user_c     = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a     = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c     = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a     = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c   = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a   = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['jb_num']
        verbose_name = 'SubjectBilling'

    def __str__(self):
        return self.jb_desc

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.jb_desc)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#MemberRecord Class - Table contains record of fund groups members transctions
class MemberRecord(models.Model):
        mr_status_choices = (('1', 'Live'), ('2', 'Reversed'), ('3', 'Cancelled'))
        mr_cat_choices = (('1', 'Contributions'), ('2', 'Advances'),('3', 'Interest'),('4', 'Penalties'),('G', 'General'))
        mr_pay_choices = (('1', 'Cheque'), ('2', 'Transfer'), ('3', 'Cash'), ('4', 'Mobile Money'))
        mr_num = models.AutoField(verbose_name='Number', primary_key=True, help_text='System generated number uniquely identifying a group member transaction')
        mr_cm_num = models.ForeignKey(ClassMember, on_delete=models.CASCADE, related_name='mr_cm', verbose_name='Member', help_text='Learner')
        mr_sc_code = models.ForeignKey(SchoolClass, on_delete=models.CASCADE,related_name='mr_sc', verbose_name='School Class', help_text='The Class')
        mr_lv_code = models.ForeignKey(Level, on_delete=models.CASCADE,related_name='mr_lv', verbose_name='Level', help_text='The study Level')
        mr_cb_num = models.ForeignKey(ClassBilling, on_delete=models.CASCADE,related_name='mr_lv',blank=True, null=True, verbose_name='Billing Head', help_text='Name of the class based fee ')
        mr_jb_num = models.ForeignKey(SubjectBilling, on_delete=models.CASCADE,related_name='mr_sb',blank=True, null=True, verbose_name='Billing Head', help_text='Name of the subject based fee')
        mr_year = models.IntegerField(verbose_name='Period', help_text='Year for which the fees are considered')
        mr_term = models.IntegerField(verbose_name='Term', help_text='Term for which the fees are considered')
        mr_trans_date = models.DateTimeField(verbose_name='Transaction Date', help_text='Transaction Date')
        mr_due_date = models.DateTimeField(verbose_name='Due Date', help_text='Transaction s due date',  blank=True, null=True)
        mr_pamount = models.DecimalField(verbose_name='Projected Amount', max_digits=15, default=0, decimal_places=2, help_text='The amount')
        mr_aamount = models.DecimalField(verbose_name='Actual Amount', max_digits=15, default=0, decimal_places=2, help_text='The actual transaction amount')
        mr_pay_ref = models.CharField(verbose_name='Payment Ref', blank=True, null=True, max_length=20, help_text='The payment reference')
        mr_category = models.CharField(verbose_name='Category', max_length=1, default='1',choices=mr_cat_choices, help_text='Category of the transaction')
        mr_dr_cr = models.CharField(verbose_name='Debit/Credit', max_length=1, default='D', help_text='The Transaction is a debit or a credit')
        mr_paid = models.CharField(verbose_name='Paid', max_length=1, help_text='Indicates payment in settlement for this transaction', default='N')
        mr_status = models.CharField(verbose_name='Status',default='1', max_length=1, choices=mr_status_choices, help_text='Status of the transaction')
        mr_processed = models.CharField(verbose_name='Processed', max_length=1, help_text='Indicates transaction has been processed', default='N')
        mr_pay_type = models.CharField(verbose_name='Payment Type',blank=True, null=True, max_length=1, choices=mr_pay_choices, help_text='Payment type', default='N')
        ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
        ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
        ad_date_c = models.DateTimeField(auto_now_add=True, blank=True, null=True,help_text='Date record was created')
        ad_date_a = models.DateTimeField(auto_now=True, blank=True, null=True,help_text='Date record was last amended')
        ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
        ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
        ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
        ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

        class Meta:
            ordering = ['mr_num']
            verbose_name = 'Member Record'
        def __str__(self):
            return self.mr_status
        def get_absolute_url(self):
            return reverse('Index', args=[str(self.mr_num)])
        def get_post_url(self):
            return reverse('edit', kwargs={'pk': self.pk})

#Receipt Class - Table contains record of receipt for a payment
class Receipt(models.Model):
    rc_status_choices = (('1', 'Live'), ('2', 'Reversed'), ('3', 'Cancelled'))
    rc_proc_choices = (('1', 'Pending'), ('2', 'Processed'))
    rc_pay_choices = (('1', 'Cheque'), ('2', 'Transfer'), ('3', 'Cash'), ('4', 'Mobile Money'))
    rc_num = models.AutoField(verbose_name='Number', primary_key=True, help_text='System generated number uniquely identifying a receipt')
    rc_cm_num = models.ForeignKey(ClassMember, on_delete=models.CASCADE, related_name='rc_cm', verbose_name='Member', blank=True, null=True, help_text='Learner')
    rc_sc_code = models.ForeignKey(SchoolClass, on_delete=models.CASCADE, related_name='rc_sc', verbose_name='School Class', blank=True, null=True, help_text='The Class')
    rc_lv_code = models.ForeignKey(Level, on_delete=models.CASCADE, related_name='mr_rc', verbose_name='Level', blank=True, null=True, help_text='The study Level')
    rc_mr_num = models.CharField(verbose_name='Member Record', max_length=20, default='0', help_text='The member transaction to which funds to be applied')
    rc_year = models.IntegerField(verbose_name='Year', blank=True, null=True, help_text='Year for which the fees are considered')
    rc_term = models.IntegerField(verbose_name='Period', blank=True, null=True, help_text='Term for which the fees are considered')
    rc_period = models.IntegerField(verbose_name='Period', blank=True, null=True, help_text='Period in which transaction occurred')
    rc_trans_date = models.DateTimeField(verbose_name='Transaction Date', blank=True, null=True, help_text='Transaction Date')
    rc_value_date = models.DateTimeField(verbose_name='Value Date', help_text='Transaction s value date', blank=True, null=True)
    rc_due_date = models.DateTimeField(verbose_name='Due Date', help_text='Transaction s due date', blank=True, null=True)
    rc_pamount = models.DecimalField(verbose_name='Projected Amount', max_digits=15, default=0, decimal_places=2, help_text='The projected trans amount')
    rc_aamount = models.DecimalField(verbose_name='Actual Amount', max_digits=15, default=0, decimal_places=2, help_text='The actual transaction amount')
    rc_balance = models.DecimalField(verbose_name='Balance', max_digits=15, default=0, decimal_places=2, help_text='The balance on the advance')
    rc_pay_ref = models.CharField(verbose_name='Payment Ref', max_length=20, blank=True, null=True, help_text='The payment reference')
    rc_dr_cr = models.CharField(verbose_name='Debit/Credit', default='D', max_length=1, help_text='The Transaction is a debit or a credit')
    rc_paid = models.CharField(verbose_name='Paid', max_length=1, help_text='Indicates payment in settlement for this transaction', default='N')
    rc_status = models.CharField(verbose_name='Status', default='1', max_length=1, choices=rc_status_choices, help_text='Status of the transaction')
    rc_processed = models.CharField(verbose_name='Processed', max_length=1, choices=rc_proc_choices, help_text='Processed ?', default='1')
    rc_pay_type = models.CharField(verbose_name='Payment Type', max_length=1, choices=rc_pay_choices, help_text='Payment type', default='3')
    ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c = models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['rc_num']
        verbose_name = 'Receipt'

    def __str__(self):
        return self.rc_status

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.rc_num)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

# Start Blog Models
class PostCategory(models.Model):
        ct_code = models.CharField(verbose_name='Code', max_length=10, primary_key=True,
                                   help_text='Enter code uniquely identifying post category')
        ct_desc = models.CharField(max_length=50, blank=True, null=True, help_text='The description of the category')
        ct_seo_title = models.CharField(verbose_name='SEO Title', max_length=300, blank=True, null=True,
                                        help_text='The SEO title of the blog')
        ct_seo_desc = models.CharField(verbose_name='SEO Description', max_length=250, blank=True, null=True,
                                       help_text='The SEO description of the blog')
        slug = models.SlugField(max_length=250, unique=True,
                                help_text='The slug field for the blog for user facing title', blank=True)
        ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
        ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
        ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
        ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
        ad_device_c = models.CharField(max_length=100, blank=True, null=True,
                                       help_text='The Device creating the record')
        ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
        ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True,
                                         help_text='The record creating ip address')
        ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

        class Meta:
            ordering = ['ct_desc']
            verbose_name = 'Blog Category'

        def save(self, *arg, **kwargs):
            self.slug = slugify(self.ct_desc)
            super(PostCategory, self).save(*arg, **kwargs)

        def __str__(self):
            return self.ct_desc

        def get_absolute_url(self):
            return reverse('IndexView', args=[str(self.ct_desc)])

        def get_post_url(self):
            return reverse('edit', kwargs={'pk': self.pk})

class PostOrigin(models.Model):
        po_num = models.CharField(verbose_name='Code', max_length=10, primary_key=True,
                                  help_text='Enter code uniquely identifying originator of the post')
        po_name = models.CharField(max_length=100, blank=True, null=True, help_text='The name of the originator')
        po_position = models.CharField(max_length=50, blank=True, null=True,
                                       help_text='The position/title of the originator')
        ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
        ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
        ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
        ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
        ad_device_c = models.CharField(max_length=100, blank=True, null=True,
                                       help_text='The Device creating the record')
        ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
        ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True,
                                         help_text='The record creating ip address')
        ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

        class Meta:
            ordering = ['po_name']
            verbose_name = 'PostOrigin'

        def __str__(self):
            return self.po_name

        def get_absolute_url(self):
            return reverse('IndexView', args=[str(self.po_name)])

        def get_post_url(self):
            return reverse('edit', kwargs={'pk': self.pk})

class BlogPost(models.Model):
        bp_choices = (('D', 'Draft'), ('R', 'Peered'), ('P', 'Publish'))
        bp_num = models.AutoField(verbose_name='Post Number', primary_key=True,
                                  help_text='Number uniquely identifying the post')
        bp_ct_code = models.ForeignKey(PostCategory, on_delete=models.CASCADE, verbose_name='Category',
                                       help_text='Category into which this post falls')
        bp_po_num = models.ForeignKey(PostOrigin, on_delete=models.CASCADE, verbose_name='Originator',
                                      help_text='The originator of the post')
        bp_heading = models.CharField(verbose_name='Heading', max_length=100, help_text='The heading of the post')
        bp_seo_title = models.CharField(verbose_name='SEO Title', max_length=300, blank=True, null=True,
                                        help_text='The SEO title of the blog')
        bp_seo_desc = models.CharField(verbose_name='SEO Description', max_length=250, blank=True, null=True,
                                       help_text='The SEO description of the blog')
        slug = models.SlugField(max_length=250, unique=True,
                                help_text='The slug field for the blog for user facing title', blank=True)
        bp_date = models.DateTimeField(auto_now_add=True, help_text='Date on which this post was created')
        bp_body = models.TextField(verbose_name='Message', max_length=350, help_text='The post s message')
        bp_status = models.CharField(verbose_name='Status', max_length=1, choices=bp_choices, default='D',
                                     help_text='Enter the status of the post')
        bp_file = models.FileField(upload_to='media/', verbose_name='Attachment File',
                                   help_text='Choose File to upload', blank=True, null=True)
        bp_image = models.ImageField(upload_to='media/', verbose_name='Image', help_text='Choose image to upload',
                                     blank=True, null=True)
        ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
        ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
        ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
        ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
        ad_device_c = models.CharField(max_length=100, blank=True, null=True,
                                       help_text='The Device creating the record')
        ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
        ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True,
                                         help_text='The record creating ip address')
        ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

        class Meta:
            ordering = ['bp_date']
            verbose_name = 'Blog Post'

        def save(self, *arg, **kwargs):
            self.slug = slugify(self.bp_heading)
            super(BlogPost, self).save(*arg, **kwargs)

        def __str__(self):
            return self.bp_heading

        def get_absolute_url(self):
            # return reverse('Index', args=[str(self.bp_heading)])
            return reverse('index', kwargs={'pk': self.pk, 'slug': self.slug})

        def get_post_url(self):
            return reverse('edit', kwargs={'pk': self.pk})

class PostContribution(models.Model):
        pc_num = models.AutoField(verbose_name='Contribution Number', primary_key=True,
                                  help_text='Number uniquely identifying the contribution')
        pc_bp_num = models.ForeignKey(BlogPost, on_delete=models.CASCADE, verbose_name='BlogPost',
                                      db_column='pc_bp_num', related_name='contributions',
                                      help_text='The Reference post for this contribution')
        pc_contribution = models.TextField(verbose_name='Contribution', max_length=350,
                                           help_text='The contribution to a post')
        pc_email = models.EmailField(verbose_name='Email', blank=True, null=True, help_text='The contributor s email')
        pc_contributor = models.CharField(verbose_name='Contributor', max_length=50, blank=True, null=True,
                                          help_text='The name of the contributor')
        pc_active = models.BooleanField(verbose_name='Accepted', default=False,
                                        help_text='Indicates whether contribution is accepted or not')
        ad_user_c = models.CharField(max_length=30, blank=True, null=True, help_text='The Creating record')
        ad_user_a = models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
        ad_date_c = models.DateTimeField(auto_now_add=True, help_text='Date record was created')
        ad_date_a = models.DateTimeField(auto_now=True, help_text='Date record was last amended')
        ad_device_c = models.CharField(max_length=100, blank=True, null=True,
                                       help_text='The Device creating the record')
        ad_device_a = models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
        ad_ipadress_c = models.CharField(max_length=50, blank=True, null=True,
                                         help_text='The record creating ip address')
        ad_ipadress_a = models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

        class Meta:
            ordering = ['ad_date_c']
            verbose_name = 'Contribution'

        def __str__(self):
            return self.pc_contribution

        def get_absolute_url(self):
            return reverse('Index', args=[str(self.pc_num)])

        def get_post_url(self):
            return reverse('edit', kwargs={'pk': self.pk})

        def approve_contributions(self):
            self.pc_active = True
            self.save()
