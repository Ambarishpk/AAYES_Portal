from django.shortcuts import render, redirect
from .models import Application


def home(request):
    return render(request, 'base.html')


def registration(request):
    if request.method == 'POST':
        name = request.POST['']
        gender = request.POST['']
        date_of_birth = request.POST['']
        languages_spoken = request.POST['']
        district = request.POST['']
        mobile_number = request.POST['']
        whatsapp_number = request.POST['']
        address = request.POST['']
        profession = request.POST['']
        educational_qualification = request.POST['']
        designation = request.POST['']
        in_service_or_retired = request.POST['']
        type_of_employment = request.POST['']
        member_of = request.POST['']
        email_address = request.POST['']
        role = request.POST['']
        field_of_intrest = request.POST['']
        previous_experience = request.POST['']
        marital_status = request.POST['']
        monthly_income = request.POST['']
        father_or_spouse_name = request.POST['']
        father_or_spouse_monthly_income = request.POST['']
        father_or_spouse_occupation = request.POST['']
        number_of_children = request.POST['']
        invoved_in_any_social_activities = request.POST['']
        affiliated_with_any_ngo_or_trust = request.POST['']
        hours_can_you_dedicate_in_a_week = request.POST['']
        own_vehicle = request.POST['']
        willing_to_attend_workshop = request.POST['']
        willing_to_attend_residential_training_programs = request.POST['']
        willing_to_pay_workshop_registration_fee = request.POST['']
        how_much_money_can_donate_per_month = request.POST['']
        religion = request.POST['']
        believe_in_god = request.POST['']
        call_brahmins_for_rituals = request.POST['']
        believe_in_rituals = request.POST['']
        worship_of_heirlooms = request.POST['']
        cause_for_untouchability = request.POST['']
        main_problem_of_dalits = request.POST['']
        untouchability_related_to_religion = request.POST['']
        solution_given_by_dr_ambedkar_for_untouchability = request.POST['']
        solution_for_untouchability_your_pov = request.POST['']
        read_ambedkar_books = request.POST['']
        willing_to_volunteer_for_free = request.POST['']
        additional_skills = request.POST['']
        willing_to_visit_adw_hostels = request.POST['']
        social_media_account = request.POST['']
        do_you_agree_that_conversion_is_a_solution_for_untouchability = request.POST['']
        is_untouchability_prevalent_nowadays = request.POST['']
        how_many_assistant_district_coordinators_you_can_gather = request.POST['']
        affiliated_to_any_political_party = request.POST['']

        # Create the user instance
        application = Application(
            name=name,
            gender=gender,
            date_of_birth=date_of_birth,
            languages_spoken=languages_spoken,
            district=district,
            mobile_number=mobile_number,
            whatsapp_number=whatsapp_number,
            address=address,
            profession=profession,
            educational_qualification=educational_qualification,
            designation=designation,
            in_service_or_retired=in_service_or_retired,
            type_of_employment=type_of_employment,
            member_of=member_of,
            email_address=email_address,
            role=role,
            field_of_intrest=field_of_intrest,
            previous_experience=previous_experience,
            marital_status=marital_status,
            monthly_income=monthly_income,
            father_or_spouse_name=father_or_spouse_name,
            father_or_spouse_monthly_income=father_or_spouse_monthly_income,
            father_or_spouse_occupation=father_or_spouse_occupation,
            number_of_children=number_of_children,
            invoved_in_any_social_activities=invoved_in_any_social_activities,
            affiliated_with_any_ngo_or_trust=affiliated_with_any_ngo_or_trust,
            hours_can_you_dedicate_in_a_week=hours_can_you_dedicate_in_a_week,
            own_vehicle=own_vehicle,
            willing_to_attend_workshop=willing_to_attend_workshop,
            willing_to_attend_residential_training_programs=willing_to_attend_residential_training_programs,
            willing_to_pay_workshop_registration_fee=willing_to_pay_workshop_registration_fee,
            how_much_money_can_donate_per_month=how_much_money_can_donate_per_month,
            religion=religion,
            believe_in_god=believe_in_god,
            call_brahmins_for_rituals=call_brahmins_for_rituals,
            believe_in_rituals=believe_in_rituals,
            worship_of_heirlooms=worship_of_heirlooms,
            cause_for_untouchability=cause_for_untouchability,
            main_problem_of_dalits=main_problem_of_dalits,
            untouchability_related_to_religion=untouchability_related_to_religion,
            solution_given_by_dr_ambedkar_for_untouchability=solution_given_by_dr_ambedkar_for_untouchability,
            solution_for_untouchability_your_pov=solution_for_untouchability_your_pov,
            read_ambedkar_books=read_ambedkar_books,
            willing_to_volunteer_for_free=willing_to_volunteer_for_free,
            additional_skills=additional_skills,
            willing_to_visit_adw_hostels=willing_to_visit_adw_hostels,
            social_media_account=social_media_account,
            do_you_agree_that_conversion_is_a_solution_for_untouchability=do_you_agree_that_conversion_is_a_solution_for_untouchability,
            is_untouchability_prevalent_nowadays=is_untouchability_prevalent_nowadays,
            how_many_assistant_district_coordinators_you_can_gather=how_many_assistant_district_coordinators_you_can_gather,
            affiliated_to_any_political_party=affiliated_to_any_political_party,
        )
        application.save()
        # Redirect to registration page after successful registration
        return redirect('registration')
    return render(request, 'registration.html')
