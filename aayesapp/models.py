from django.db import models
from django.contrib.auth.hashers import make_password


def Choices():
    Choices = [
        ('DC', 'District Coordinator'),
        ('ADC', 'Associate District Coordinator'),
        ('ZC', 'Zonal District Coordinator'),
        ('SC', 'State Coordinator'),
        ('DADW', 'District of Adi Dravida Welfare'),
        ('WARDAN', 'Wardan'),
        ('DONOR', 'Donor'),
        ('RP', 'Resource Person'),
        # ... Add other roles if needed
    ]

    return Choices


class Application(models.Model):

    ROLE_CHOICES = Choices()
    # General Info
    id = models.CharField(max_length=20, primary_key=True,
                          editable=False)
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    languages_spoken = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    mobile_number = models.CharField(max_length=10)
    email_address = models.EmailField()
    whatsapp_number = models.CharField(max_length=10)
    address = models.TextField()
    profession = models.CharField(max_length=100)
    educational_qualification = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    in_service_or_retired = models.CharField(max_length=20)
    type_of_employment = models.CharField(max_length=100)
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    module_of_interest = models.CharField(max_length=100)

    # Info for SC, ZC, DC, ADC
    community = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100, null=True)
    monthly_income = models.CharField(max_length=100, null=True)
    father_or_spouse_name = models.CharField(
        max_length=100, null=True)
    father_or_spouse_monthly_income = models.CharField(
        max_length=15, null=True)
    father_or_spouse_occupation = models.CharField(
        max_length=100, null=True)
    number_of_children = models.CharField(
        max_length=10, null=True)
    invoved_in_any_social_activities = models.CharField(
        max_length=100, null=True)
    affiliated_with_any_ngo_or_trust = models.CharField(
        max_length=100, null=True)
    hours_can_dedicate = models.CharField(
        max_length=50, null=True)
    own_vehicle = models.CharField(max_length=50, null=True)
    willing_to_attend_residential_training_programs = models.CharField(
        max_length=50, null=True)
    money_can_you_donate_per_month = models.CharField(
        max_length=50, null=True)
    religion = models.CharField(max_length=50, null=True)
    believe_in_god = models.CharField(max_length=50, null=True)
    call_brahmins_for_rituals = models.CharField(
        max_length=50, null=True)
    believe_in_rituals = models.CharField(
        max_length=50, null=True)
    worship_of_heirlooms = models.CharField(
        max_length=50, null=True)
    cause_for_untouchability = models.CharField(
        max_length=50, null=True)
    main_problem_of_dalits = models.CharField(
        max_length=100, null=True)
    untouchability_related_to_religion = models.CharField(
        max_length=50, null=True)
    solution_given_by_dr_ambedkar_for_untouchability = models.CharField(
        max_length=50, null=True)
    solution_for_untouchability_your_pov = models.CharField(
        max_length=50, null=True)
    read_ambedkar_books = models.CharField(
        max_length=50, null=True)
    willing_to_volunteer_for_free = models.CharField(
        max_length=50, null=True)
    hobby = models.CharField(max_length=100, null=True)
    additional_skills = models.CharField(
        max_length=50, null=True)
    willing_to_visit_adw_hostels = models.CharField(
        max_length=50, null=True)
    social_media_account = models.CharField(
        max_length=50, null=True)
    do_you_agree_that_conversion_is_a_solution_for_untouchability = models.CharField(
        max_length=50, null=True)
    is_untouchability_prevalent_nowadays = models.CharField(
        max_length=50, null=True)
    how_many_assistant_district_coordinators_you_can_gather = models.CharField(
        max_length=50, null=True)
    affiliated_to_any_political_party = models.CharField(
        max_length=100, null=True)
    status = models.CharField(
        max_length=100, default="Pending Approval of District Coordinator")
    approved_by_dc = models.BooleanField(default=False)
    approved_by_zc = models.BooleanField(default=False)
    approved_by_sc = models.BooleanField(default=False)

    password = models.CharField(max_length=150, null=False, default="admin")

    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        if not self.id:
            if self.role in ('DC', 'ADC', 'ZC', 'SC'):
                prefix = 'AAYES' + self.role
                last_id = Application.objects.filter(
                    role=self.role).order_by('-id').first()
                if last_id:
                    last_number = int(last_id.id[-2:]) + 1
                else:
                    last_number = 1
                self.id = f'{prefix}{last_number:02}'
            else:
                last_member_id = Application.objects.filter(
                    role='MBR').order_by('-id').first()
                if last_member_id:
                    last_member_number = int(last_member_id.id[-3:]) + 1
                else:
                    last_member_number = 1
                self.id = f'AAYESMBR{last_member_number:03}'

        super(Application, self).save(*args, **kwargs)


def __str__(self):
    return self.name
