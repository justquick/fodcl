from django.db import models

AREAS = (
(1,'Upper Deep Creek-Cove'),
(2,'Upper Deep Creek-Spur'),
(3,'Upper Deep Creek-Unnamed'),
(4,'Upper Deep Creek-Pergin Cove'),
(5,'Upper Deep Creek-Hickory Ridge Cove'),
(6,'Pawn Run-Cove'),
(7,'Pawn Run-Unnamed'),
(8,'Green Glade-Pine Point'),
(9,'Green Glade-Unnamed'),
(10,'Green Glade-Hazelhurst'),
(11,'Green Glade-Cove'),
(12,'Green Glade-Poland Run'),
(13,'Hoop Pole Run-Cove'),
(14,'Hoop Pole Run-Spur'),
(15,'North Glade Run-Deep Creek Cove'),
(16,'North Glade Run-Spur'),
(17,'North Glade Run-Cove'),
(18,'Shingle Camp-Unnamed Run'),
(19,'Shingle Camp-Brushy Hollow'),
(20,'Shingle Camp-Cove'),
(21,'Marsh Run-West'),
(22,'Marsh Run-North'),
(23,'Marsh Run-Northeast'),
(24,'Marsh Run-Gravely Run'),
(25,'Cherry Creek-Cove'),
(26,'Cherry Creek-Spur'),
)
STATS = (
    (1, 'Board'),
    (2, 'Blue ribbon'),
    (3, 'Government'),
    (4, 'Association'),
    (5, 'Steward'),
    (6, 'Volunteer'),
    (7, 'Activist'),
)

class Donation(models.Model):
    date = models.DateField(auto_now_add=True)
    ammount = models.IntegerField()
    
class Record(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    lake_addr = models.CharField(max_length=255,blank=True,null=True)
    home_addr = models.CharField(max_length=255,blank=True,null=True)
    email = models.CharField(max_length=255,blank=True,null=True)
    comments = models.TextField(blank=True,null=True)
    lake_phone = models.CharField(max_length=255,blank=True,null=True)
    home_phone = models.CharField(max_length=255,blank=True,null=True)
    area = models.IntegerField(choices=AREAS,blank=True,null=True)
    donations = models.ManyToManyField(Donation,blank=True,null=True)
    status = models.IntegerField(choices=STATS,blank=True,null=True)
    
    def __unicode__(self): return self.name
  
from django.contrib.localflavor.us.models import PhoneNumberField

class StreamWader(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone1 = PhoneNumberField()
    phone2 = PhoneNumberField()
    contact = models.CharField(max_length=255,help_text='Best way to contact you for last minute updates, changes')
    is_attending = models.BooleanField(help_text='Yes I want to attend the Stream Waders Training program Saturday February 28 from 8:30 to 3:30 in Clear Spring Maryland. Please send me details.')
    is_participating = models.BooleanField(help_text='Yes I want to participate in the Stream Waders tributary assessment the beginning of April.')
    best_dates = models.CharField(max_length=255,null=True,blank=True,help_text='What are the best dates for you in the first 2 weeks of April?')
    stream = models.CharField(max_length=255,help_text='Is there a particular stream which feeds DCL which you would like to study')
    has_gps = models.BooleanField(help_text='I can contribute a mobile GPS to mark our locations')
    has_camera = models.BooleanField(help_text='I can contribute a camera to record our work')
    has_boots = models.BooleanField(help_text='I have an extra pair of wading boots to lend')
    can_lead = models.BooleanField(help_text='I am willing to lead a group of high school students')
    can_volunteer = models.BooleanField(help_text='We need volunteers in March to obtain permission to cross private lands which abut the streams. We can tell you what we need. Would you be willing to help to obtain these permissions?')
 
 
    def __unicode__(self):
        return self.name
    
from django import forms
buy_down = models.BooleanField()
class StreamWaderForm(forms.ModelForm):
    class Meta:
        model = StreamWader

RATINGS = (
   (0, 'No Opinion'),
   (1, '1'),
   (2, '2'),
   (3, '3'),
   (4, '4'),
   (5, '5'),
)


DOCKS = (
   (1, 'Type A ($200 Fee)'),
   (2, 'Common ($160 Fee)'),
   (3, 'Other'),
   (0, 'None')
)

MONTHS1  = (
   (1, 'March'),
   (2, 'April'),
   (3, 'May'),
   (4, 'June'),
   (5, 'July'),
   (0, 'It Stays In')
)

MONTHS2 = (
   (1, 'July'),
   (2, 'August'),
   (3, 'September'),
   (4, 'October'),
   (5, 'November'),
   (0, 'It Stays In')
)

LAKE_ACTIVITIES = (
   (0, 'Boating / Jet Ski'),
   (1, 'Sailing'),
   (2, 'Fishing'),
   (3, 'Swimming'),
   (4, 'Water Sports'),
   (5, 'Kayaking / Canoeing'),
   (6, 'Relaxing on the dock')
)

class Survey(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length = 50)

    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100,blank=True,null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=11)
    zipcode = models.CharField(max_length=10)

    maddress1 = models.CharField(max_length=255,blank=True,null=True)
    maddress2 = models.CharField(max_length=255,blank=True,null=True)
    mcity = models.CharField(max_length=255,blank=True,null=True)
    mstate = models.CharField(max_length=255,blank=True,null=True)
    mzipcode = models.CharField(max_length=255,blank=True,null=True)


    phone = PhoneNumberField()
    email = models.EmailField(blank=True,null=True)
    people_family = models.IntegerField()
    people_kids = models.IntegerField()
    full_time = models.BooleanField()
    weeks_year = models.IntegerField(blank=True,null=True)
    buy_down = models.BooleanField()

    dnr_dealings = models.BooleanField()
    dnr_describe = models.TextField(blank=True,null=True)
    dnr_rating = models.IntegerField(choices=RATINGS,default=0)

    dock_type = models.IntegerField(choices=DOCKS,default=0)
    know_budget = models.BooleanField()


    dock_in = models.IntegerField(choices=MONTHS1,default=0) 
    dock_out = models.IntegerField(choices=MONTHS2,default=0)

    increase_fees = models.BooleanField()
    how_much = models.IntegerField(blank=True,null=True)

    activities_boating = models.BooleanField()
    activities_sailing = models.BooleanField()
    activities_fishing = models.BooleanField()
    activities_swimming = models.BooleanField()
    activities_sports = models.BooleanField()
    activities_kayaking = models.BooleanField()
    activities_relaxing = models.BooleanField()

    activities_boating2 = models.BooleanField()
    activities_sailing2 = models.BooleanField()
    activities_fishing2 = models.BooleanField()
    activities_swimming2 = models.BooleanField()
    activities_sports2 = models.BooleanField()
    activities_kayaking2 = models.BooleanField()
    activities_relaxing2 = models.BooleanField()

    change_quality = models.TextField(blank=True,null=True)
    change_shoreline = models.TextField(blank=True,null=True)
    change_weeds = models.TextField(blank=True,null=True)
    change_other = models.TextField(blank=True,null=True)

    discovery_aware = models.BooleanField()
    discovery_attend = models.BooleanField()
    discovery_attend_often = models.IntegerField(blank=True,null=True)
    discovery_rating = models.IntegerField(choices=RATINGS,default=0)
    discovery_fees = models.BooleanField()

    POA_member = models.BooleanField()
    POA_meeting = models.BooleanField()
    POA_meeting_useful = models.BooleanField()
    POA_rating = models.IntegerField(choices=RATINGS,default=0)

    PRB_know = models.BooleanField()
    PRB_rating = models.IntegerField(choices=RATINGS,default=0)

    fodcl_do = models.TextField(blank=True,null=True)
    other_comments = models.TextField(blank=True,null=True)


class SurveyForm(forms.ModelForm):
    class Meta:
	model = Survey
