from django.db import models


class Application(models.Model):

    # General Info
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
    role = models.CharField(max_length=50)
    module_of_interest = models.CharField(max_length=100)

    # Info for SC, ZC, DC, ADC
    community = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100)
    monthly_income = models.CharField(max_length=100)
    father_or_spouse_name = models.CharField(max_length=100)
    father_or_spouse_monthly_income = models.CharField(max_length=15)
    father_or_spouse_occupation = models.CharField(max_length=100)
    number_of_children = models.CharField(max_length=10)
    invoved_in_any_social_activities = models.CharField(max_length=100)
    affiliated_with_any_ngo_or_trust = models.CharField(max_length=100)
    hours_can_you_dedicate = models.CharField(max_length=50)
    own_vehicle = models.CharField(max_length=50)
    willing_to_attend_residential_training_programs = models.CharField(
        max_length=50)
    money_can_you_donate_per_month = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    believe_in_god = models.CharField(max_length=50)
    call_brahmins_for_rituals = models.CharField(max_length=50)
    believe_in_rituals = models.CharField(max_length=50)
    worship_of_heirlooms = models.CharField(max_length=50)
    cause_for_untouchability = models.CharField(max_length=50)
    main_problem_of_dalits = models.CharField(max_length=100)
    do_you_think_untouchability_related_to_religion = models.CharField(
        max_length=50)
    solution_given_by_dr_ambedkar_for_untouchability = models.CharField(
        max_length=50)
    solution_for_untouchability_in_your_pov = models.CharField(max_length=50)
    read_ambedkar_books = models.CharField(max_length=50)
    willing_to_volunteer_for_free = models.CharField(max_length=50)
    hobby = models.CharField(max_length=100)
    additional_skills = models.CharField(max_length=50)
    willing_to_visit_adw_hostels = models.CharField(max_length=50)
    social_media_account = models.CharField(max_length=50)
    do_you_agree_that_conversion_is_a_solution_for_untouchability = models.CharField(
        max_length=50)
    is_untouchability_prevalent_nowadays = models.CharField(max_length=50)
    how_many_assistant_district_coordinators_you_can_gather = models.CharField(
        max_length=50)
    affiliated_to_any_political_party = models.CharField(max_length=100)
    approved_by_dc = models.BooleanField(default=False)
    approved_by_zc = models.BooleanField(default=False)
    approved_by_sc = models.BooleanField(default=False)


class Member(models.Model):

    # General Info
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
    role = models.CharField(max_length=50)
    module_of_interest = models.CharField(max_length=100)

    # Info for SC, ZC, DC, ADC
    community = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=100)
    monthly_income = models.CharField(max_length=100)
    father_or_spouse_name = models.CharField(max_length=100)
    father_or_spouse_monthly_income = models.CharField(max_length=15)
    father_or_spouse_occupation = models.CharField(max_length=100)
    number_of_children = models.CharField(max_length=10)
    invoved_in_any_social_activities = models.CharField(max_length=100)
    affiliated_with_any_ngo_or_trust = models.CharField(max_length=100)
    hours_can_you_dedicate = models.CharField(max_length=50)
    own_vehicle = models.CharField(max_length=50)
    willing_to_attend_residential_training_programs = models.CharField(
        max_length=50)
    money_can_you_donate_per_month = models.CharField(max_length=50)
    religion = models.CharField(max_length=50)
    believe_in_god = models.CharField(max_length=50)
    call_brahmins_for_rituals = models.CharField(max_length=50)
    believe_in_rituals = models.CharField(max_length=50)
    worship_of_heirlooms = models.CharField(max_length=50)
    cause_for_untouchability = models.CharField(max_length=50)
    main_problem_of_dalits = models.CharField(max_length=100)
    do_you_think_untouchability_related_to_religion = models.CharField(
        max_length=50)
    solution_given_by_dr_ambedkar_for_untouchability = models.CharField(
        max_length=50)
    solution_for_untouchability_in_your_pov = models.CharField(max_length=50)
    read_ambedkar_books = models.CharField(max_length=50)
    willing_to_volunteer_for_free = models.CharField(max_length=50)
    hobby = models.CharField(max_length=100)
    additional_skills = models.CharField(max_length=50)
    willing_to_visit_adw_hostels = models.CharField(max_length=50)
    social_media_account = models.CharField(max_length=50)
    do_you_agree_that_conversion_is_a_solution_for_untouchability = models.CharField(
        max_length=50)
    is_untouchability_prevalent_nowadays = models.CharField(max_length=50)
    how_many_assistant_district_coordinators_you_can_gather = models.CharField(
        max_length=50)
    affiliated_to_any_political_party = models.CharField(max_length=100)
    approved_by_dc = models.BooleanField(default=False)
    approved_by_zc = models.BooleanField(default=False)
    approved_by_sc = models.BooleanField(default=False)


def __str__(self):
    return self.name
