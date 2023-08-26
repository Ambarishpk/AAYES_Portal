from django.contrib import admin
from .models import Application, Member


def move_to_members(modeladmin, request, queryset):
    for application in queryset:
        if application.approved_by_sc and application.approved_by_dc and application.approved_by_zc:
            Member.objects.create(

                # General Info
                name=application.name,
                gender=application.gender,
                date_of_birth=application.date_of_birth,
                languages_spoken=application.languages_spoken,
                district=application.district,
                mobile_number=application.mobile_number,
                email_address=application.email_address,
                whatsapp_number=application.whatsapp_number,
                address=application.address,
                profession=application.profession,
                educational_qualification=application.educational_qualification,
                designation=application.designation,
                in_service_or_retired=application.in_service_or_retired,
                type_of_employment=application.type_of_employment,
                role=application.role,
                module_of_interest=application.module_of_interest,

                # Info for SC, ZC, DC, ADC
                community=application.community,
                marital_status=application.marital_status,
                monthly_income=application.monthly_income,
                father_or_spouse_name=application.father_or_spouse_name,
                father_or_spouse_monthly_income=application.father_or_spouse_monthly_income,
                father_or_spouse_occupation=application.father_or_spouse_occupation,
                number_of_children=application.number_of_children,
                invoved_in_any_social_activities=application.invoved_in_any_social_activities,
                affiliated_with_any_ngo_or_trust=application.affiliated_with_any_ngo_or_trust,
                hours_can_you_dedicate=application.hours_can_you_dedicate,
                own_vehicle=application.own_vehicle,
                willing_to_attend_residential_training_programs=application.willing_to_attend_residential_training_programs,
                money_can_you_donate_per_month=application.money_can_you_donate_per_month,
                religion=application.religion,
                believe_in_god=application.believe_in_god,
                call_brahmins_for_rituals=application.call_brahmins_for_rituals,
                believe_in_rituals=application.believe_in_rituals,
                worship_of_heirlooms=application.worship_of_heirlooms,
                cause_for_untouchability=application.cause_for_untouchability,
                main_problem_of_dalits=application.main_problem_of_dalits,
                do_you_think_untouchability_related_to_religion=application.do_you_think_untouchability_related_to_religion,
                solution_given_by_dr_ambedkar_for_untouchability=application.solution_given_by_dr_ambedkar_for_untouchability,
                solution_for_untouchability_in_your_pov=application.solution_for_untouchability_in_your_pov,
                read_ambedkar_books=application.read_ambedkar_books,
                willing_to_volunteer_for_free=application.willing_to_volunteer_for_free,
                hobby=application.hobby,
                additional_skills=application.additional_skills,
                willing_to_visit_adw_hostels=application.willing_to_visit_adw_hostels,
                social_media_account=application.social_media_account,
                do_you_agree_that_conversion_is_a_solution_for_untouchability=application.do_you_agree_that_conversion_is_a_solution_for_untouchability,
                is_untouchability_prevalent_nowadays=application.is_untouchability_prevalent_nowadays,
                how_many_assistant_district_coordinators_you_can_gather=application.how_many_assistant_district_coordinators_you_can_gather,
                affiliated_to_any_political_party=application.affiliated_to_any_political_party,
                approved_by_dc=application.approved_by_dc,
                approved_by_zc=application.approved_by_zc,
                approved_by_sc=application.approved_by_sc,
            )
            application.delete()


move_to_members.short_description = "Move selected applications to Members"


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'approved_by_dc',
                    'approved_by_zc', 'approved_by_sc']
    actions = [move_to_members]


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Member)
