from django.db import models
    # from django import django.template.defaultfilters
from django.urls import reverse
from django.contrib.auth.models import User
from datetime import date
#from slugify import slugify
from django.template.defaultfilters import slugify

#Level - class representing the Levels of study
class Level(models.Model):
	lv_status_choices = (('1', 'Active'), ('0', 'Inactive'))

	lv_code = models.CharField(verbose_name='Code',primary_key=True,max_length=10, help_text='The Level Code - Primary key for the table')
	lv_name = models.CharField(verbose_name='Level Name',max_length=100, help_text='Leval Name')
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
	
#Subject - class representing the Subjects offerred
class Subject(models.Model):
    type_choice		=	(('1','Academic'),('2', 'Sport'),('3', 'Extra Carricular'))
    status_choice	=	(('1', 'On'),('2' , 'Off'))

    sb_code		=	models.CharField(verbose_name='Code', max_length=10, primary_key=True, help_text='User assigned code for the Subject')
	sb_lv_code	=	models.ForeignKey(Level,on_delete=models.CASCADE,verbose_name='Level', help_text='Foreign key to Level')
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
        return self.sb_code

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.sb_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#SchoolClass -  Class representing a School Class
class SchoolClass(models.Model):
    type_choice		=	(('1','Academic'),('2', 'Sport'),('3', 'Extra Carricular'))
    status_choice	=	(('1', 'On'),('2' , 'Off'))

    sc_code		=	models.CharField(verbose_name='Code', max_length=10, primary_key=True, help_text='User assigned code for the Class Level')
	sc_lv_code	=	models.ForeignKey(Level,on_delete=models.CASCADE,verbose_name='Level', help_text='Foreign key to Level')
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
        verbose_name = 'SchoolClass'

    def __str__(self):
        return self.sc_code

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.sc_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})
    
#LevelClass -  Class representing the class for each level of study
class LevelClass(models.Model):
    type_choice		=	(('1','Academic'),('2', 'Sport'),('3', 'Extra Carricular'))
    status_choice	=	(('1', 'On'),('2' , 'Off'))
    
	lc_num		=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying a Level Class')
    lc_sc_code	=	models.ForeignKey(SchoolClass,on_delete=models.CASCADE,verbose_name='School Class', help_text='Foreign key to SchoolClass')
	lc_lv_code	=	models.ForeignKey(Level,on_delete=models.CASCADE,verbose_name='Level', help_text='Foreign key to Level')
	lc_sb_code	=	models.ForeignKey(Subject,on_delete=models.CASCADE,verbose_name='Subject', help_text='Foreign key to Subject')
    lc_type		=	models.CharField(verbose_name='Type', max_length=1,choices=type_choice, help_text='Type of the Subject')
    lc_desc		=	models.CharField(verbose_name='Name', max_length=100, help_text='The description of the Subject')
    lc_hrs		=	models.DecimalField(verbose_name='Req. Hrs',max_digits=10, decimal_places=2, default=0, help_text='Required hrs for Subject', null=True, blank=True)
    lc_status	=	models.CharField(verbose_name='Status', max_length=1,choices=status_choice,default='1', help_text='Status')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['lc_code']
        verbose_name = 'LevelClass'

    def __str__(self):
        return self.lc_code

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.lc_code)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#ClassMember -  Class representing the class for each Class Member
class ClassMember(models.Model):
    app_status_type_choice		=	(('1','Academic'),('2', 'Sport'),('3', 'Extra Carricular'))
    status_choice	=	(('1', 'On'),('2' , 'Suspended'),('3' , 'Expelled'))
    
	cm_num		=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying a Class Member')
    cm_sc_code	=	models.ForeignKey(SchoolClass,on_delete=models.CASCADE,verbose_name='School Class', help_text='Foreign key to SchoolClass')
	cm_lv_code	=	models.ForeignKey(Level,on_delete=models.CASCADE,verbose_name='Level', help_text='Foreign key to Level')
  	cm_surname	=	models.CharField(verbose_name='Surame', max_length=100, help_text='Class Member Surname')
    cm_fname	=	models.CharField(verbose_name='First Name', max_length=100, help_text='Class Member First Name')
    cm_otherName	=	models.CharField(verbose_name='Other Name', max_length=100, help_text='Class Member s Other Name')
    cm_Guardian	=	models.CharField(verbose_name='Guardian', max_length=100, help_text='Class Member s Guardian')
    cm_Phone	=	models.CharField(verbose_name='Phone', max_length=100, help_text='Contact phone')
    cm_Email	=	models.CharField(verbose_name='Email', max_length=100, help_text='Contact Email')
    cm_dob	=	models.DateTimeField(auto_now=True,verbose_name='Date Of Birth', help_text='Date of birth')  
    cm_doj	=	models.DateTimeField(auto_now=True,verbose_name='Date joined', help_text='Date Joined')
    cm_dol	=	models.DateTimeField(auto_now=True,verbose_name='Date of Leaving', help_text='Date of leaving')
    cm_status	=	models.CharField(verbose_name='Status', max_length=1,choices=status_choice,default='1', help_text='Status')
    cm_app_status	=	models.CharField(verbose_name='Status', max_length=1,choices=app_status_type_choice,default='1', help_text='Status')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['cm_surname']
        verbose_name = 'ClassMember'

    def __str__(self):
        return self.cm_surname

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.cm_surname)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})
    	
#LevelClassInstance -  Class representing the class for each instance of a class of study
class LevelClassInstance(models.Model):
    type_choice		=	(('1','Academic'),('2', 'Sport'),('3', 'Extra Carricular'))
    status_choice	=	(('1', 'On'),('2' , 'Off'))
    
	ci_num		=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying a Class Instance')
	ci_lc_num	=	models.ForeignKey(LevelClass='Level Class', primary_key=True,help_text='The Level Class')
    ci_sc_code	=	models.ForeignKey(SchoolClass,on_delete=models.CASCADE,verbose_name='School Class', help_text='Foreign key to School Class')
	ci_lv_code	=	models.ForeignKey(Level,on_delete=models.CASCADE,verbose_name='Level', help_text='Foreign key to Level')
	ci_sb_code	=	models.ForeignKey(Subject,on_delete=models.CASCADE,verbose_name='Subject', help_text='Foreign key to Subject')
    ci_type		=	models.CharField(verbose_name='Type', max_length=1,choices=type_choice, help_text='Type of the Subject')
    ci_desc		=	models.CharField(verbose_name='Name', max_length=100, help_text='The description of the Subject')
    ci_hrs		=	models.DecimalField(verbose_name='Req. Hrs',max_digits=10, decimal_places=2, default=0, help_text='Required hrs for Subject', null=True, blank=True)
    ci_status	=	models.CharField(verbose_name='Status', max_length=1,choices=status_choice,default='1', help_text='Status')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['ci_num']
        verbose_name = 'LevelClassInstance'

    def __str__(self):
        return self.ci_sc_code

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.ci_sc_code)])

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

#StaffMember -  Class representing the Staff Members
class StaffMember(models.Model):
    app_status_type_choice		=	(('1','Academic'),('2', 'Sport'),('3', 'Extra Carricular'))
    status_choice	=	(('1', 'Engaged'),('2' , 'Suspended'),('3' , 'Discharged'),('4', 'Pending'),('5', 'In Process'))
    gender_choice	=	(('F', 'Female'),('M' , 'Male'))
	
	sf_num 		    = models.AutoField(verbose_name='Member ID',primary_key=True, help_text='Code uniquely identify a Staff Member')
	sf_dp_code 		= models.ForeignKey(Dept,verbose_name='Department',help_text='Staff member s department')
  	sf_surname		= models.CharField(verbose_name='Surame', max_length=100, help_text='Staff Member Surname')
    sf_fname		= models.CharField(verbose_name='First Name', max_length=100, help_text='Staff Member First Name')
    sf_otherName	= models.CharField(verbose_name='Other Name', max_length=100, help_text='Staff Member s Other Name')
    sf_nok			= models.CharField(verbose_name='Next Of Kin', max_length=100, help_text='Staff Member s next of kin')
    sf_Phone		= models.CharField(verbose_name='Phone', max_length=100, help_text='Contact phone')
    sf_Email		= models.CharField(verbose_name='Email', max_length=100, help_text='Contact Email')
    sf_dob			= models.DateTimeField(auto_now=True,verbose_name='Date Of Birth', help_text='Date of birth')  
    sf_doj			= models.DateTimeField(auto_now=True,verbose_name='Date joined', help_text='Date Joined')
    sf_dol			= models.DateTimeField(auto_now=True,verbose_name='Date of Leaving', help_text='Date of leaving')
    sf_status		= models.CharField(verbose_name='Status', max_length=1,choices=status_choice,default='1', help_text='Status')
	sf_gender		= models.CharField(verbose_name='Gender', max_length=1,choices=gender_choice,default='1', help_text='Gender')
    sf_app_status	= models.CharField(verbose_name='Status', max_length=1,choices=app_status_type_choice,default='1', help_text='Status')
	ad_user_c 		= models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
	ad_user_a 		= models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
	ad_date_c 		= models.DateTimeField(auto_now_add=True, help_text='Date record was created')
	ad_date_a 		= models.DateTimeField(auto_now=True, help_text='Date record was last amended')
	ad_device_c 	= models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
	ad_device_a 	= models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
	ad_ipadress_c 	= models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
	ad_ipadress_a 	= models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

	class Meta:
		ordering = ['sf_surname']
		verbose_name = 'StaffMember'

	def __str__(self):
		return self.sf_surname

	def get_absolute_url(self):
		return reverse('Index', args=[str(self.sf_surname)])

	def get_post_url(self):
		return reverse('edit', kwargs={'pk': self.pk})
	
#StaffSubject Class - class representing the subjects the staff member is competent to take

class StaffSubject(models.Model):
	ss_status_choices = (('1', 'Active'), ('0', 'Inactive'))

	ss_num = models.AutoField(verbose_name='Number',primary_key=True, help_text='Code uniquely identify a record')
    ss_sf_num	=	models.ForeignKey(StaffMember,on_delete=models.CASCADE,verbose_name='Staff Member', help_text='Staff Member')
    ss_sb_code	=	models.ForeignKey(Subject,on_delete=models.CASCADE,verbose_name='Subject', help_text='Foreign key to Subject')
	ss_lv_code	=	models.ForeignKey(Level,on_delete=models.CASCADE,verbose_name='Up to Level', help_text='Teaches up to level ?')
	ss_status   = models.CharField(verbose_name='Status',max_length=1, choices=cu_status_choices, help_text='Status of the currency', default='1')
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

#FacilitySpace -  Class representing the FacilitySpace in FacilitySpace
class FacilitySpace(models.Model):
    status_choice	=	(('1', 'On'),('2' , 'Off'))
    
	fs_num		=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying a FacilitySpace')
    fs_fc_num	=	models.ForeignKey(Facility,on_delete=models.CASCADE,verbose_name='Facility', help_text='Foreign key to Facility')
    fs_desc		=	models.CharField(verbose_name='Name', max_length=100, help_text='The description of the space')
    fs_status	=	models.CharField(verbose_name='Status', max_length=1,choices=status_choice,default='1', help_text='Status')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['fs_num']
        verbose_name = 'FacilitySpace'

    def __str__(self):
        return self.fs_desc

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.fs_desc)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#SpaceSlot -  Class representing the Slot for each Space of the Facility
class SpaceSlot(models.Model):
    type_choice		=	(('1','Academic'),('2', 'Sport'),('3', 'Extra Carricular'))
    status_choice	=	(('1', 'On'),('2' , 'Off'))
    
	sp_num		=	models.AutoField(verbose_name='Number', primary_key=True,help_text='System generated number uniquely identifying a Level Class')
    sp_fs_num	=	models.ForeignKey(SchoolClass,on_delete=models.CASCADE,verbose_name='School Class', help_text='Foreign key to SchoolClass')
    sp_type		=	models.CharField(verbose_name='Type', max_length=1,choices=type_choice, help_text='Type of the Subject')
    sp_desc		=	models.CharField(verbose_name='Name', max_length=100, help_text='The description of the Subject')
    sp_hrs		=	models.DecimalField(verbose_name='Duration',max_digits=10, decimal_places=2, default=0, help_text='Duration of the slot', null=True, blank=True)
    sp_fromtime	=	models.DateTimeField(verbose_name='From Time', help_text='Required hrs for Subject', null=True, blank=True)
    sp_totime	=	models.DateTimeField(verbose_name='To Time', help_text='Required hrs for Subject', null=True, blank=True)
    sp_status	=	models.CharField(verbose_name='Status', max_length=1,choices=status_choice,default='1', help_text='Status')
    ad_user_c	=	models.CharField(max_length=30, blank=True, null=True, help_text='The user creating the record')
    ad_user_a	=	models.CharField(max_length=30, blank=True, null=True, help_text='The last amending user')
    ad_date_c	=	models.DateTimeField(auto_now_add=True, help_text='Date record was created')
    ad_date_a	=	models.DateTimeField(auto_now=True, help_text='Date record was last amended')
    ad_device_c	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Device creating the record')
    ad_device_a	=	models.CharField(max_length=100, blank=True, null=True, help_text='The Last amending device')
    ad_ipadress_c	=	models.CharField(max_length=50, blank=True, null=True, help_text='The record creating ip address')
    ad_ipadress_a	=	models.CharField(max_length=50, blank=True, null=True, help_text='The last amending ip address')

    class Meta:
        ordering = ['sp_num']
        verbose_name = 'SpaceSlot'

    def __str__(self):
        return self.sp_desc

    def get_absolute_url(self):
        return reverse('Index', args=[str(self.sp_desc)])

    def get_post_url(self):
        return reverse('edit', kwargs={'pk': self.pk})

#Currency Class - class representing the currency

class Currency(models.Model):
	cu_status_choices = (('1', 'Active'), ('0', 'Inactive'))

	cu_num = models.AutoField(verbose_name='Currency ID',primary_key=True, help_text='Code uniquely identify a Currency')
	cu_code = models.CharField(verbose_name='Code',max_length=10, help_text='The currency Code')
	cu_name = models.CharField(verbose_name='Currency Name',max_length=100, help_text='Currency Name')
	cu_base = models.CharField(verbose_name='Base Currency ?',max_length=1, help_text='Indicates whether the currency is the base currency')
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
	
    # Settings.py Original
	
    """
Django settings for s_admin project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-m@u*uc-a^r)ohbv9uhkhydt%#l)1#7j5(%nau#bo+320q%wds8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 's_admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 's_admin.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

	
