from django.shortcuts import render, redirect
from .models import Application
from django.db.models import Q
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages


def home(request):
    return render(request, 'home.html')


def logout_view(request):
    if 'authenticated_id' in request.session:
        del request.session['authenticated_id']
        del request.session['role']
        del request.session['role_tuple']
    return redirect('home')


def login_view(request):
    if request.method == 'POST':
        id = request.POST['id']
        id = id.upper()
        password = request.POST['password']

        try:
            application_user = Application.objects.get(id=id)

            # Check if the provided password matches the stored encrypted password
            if check_password(password, application_user.password):
                request.session['authenticated_id'] = id
                request.session['role'] = application_user.role
                request.session['role_tuple'] = ['DC', 'SC', 'ZC']
                request.session.set_expiry(86400)
                messages.success(request, 'Successfully Logged In!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid Credentials')
        except Application.DoesNotExist:
            messages.error(request, 'User Not Found')
    else:
        pass

    if 'authenticated_id' in request.session:
        context = {
            'errorMessage': "You're already logged in.",
            'errorCode': 200
        }
        return render(request, 'error.html', context)
    else:
        return render(request, 'login.html')


def approval(request):
    if request.method == 'POST':
        approve_id = request.POST.get('id-to-approve')

        print('ID TO APPROVE: ', approve_id)
        current_user_id = request.session.get('authenticated_id')
        print('Approve ID is: ', approve_id)
        try:
            application = Application.objects.get(id=approve_id)
        except Application.DoesNotExist:
            return render(request, 'error.html', {'error_message': 'Application not found.'})

        if 'DC' in current_user_id:
            application.approved_by_dc = True
            application.status = 'Pending Approval of Zonal Coordinator'
        elif 'ZC' in current_user_id:
            application.approved_by_zc = True
            application.status = 'Pending Approval of State Coordinator'
        elif 'SC' in current_user_id:
            application.approved_by_sc = True
            application.status = 'Approved'
        else:
            pass

        application.save()

        messages.success(request, f'Application has been Approved')

    if 'authenticated_id' in request.session:
        id = request.session.get('authenticated_id')
        current_user = Application.objects.get(id=id)
        if 'AAYESDC' in current_user.id:
            status = 'Pending Approval of District Coordinator'
            applications = Application.objects.filter(~Q(id=current_user.id) & Q(
                district=current_user.district) & Q(status=status))
        elif 'AAYESZC' in current_user.id:
            status = 'Pending Approval of Zonal Coordinator'
            applications = Application.objects.filter(~Q(id=current_user.id) & Q(
                district=current_user.district) & Q(status=status))
        elif 'AAYESSC' in current_user.id:
            status = 'Pending Approval of State Coordinator'
            applications = Application.objects.filter(
                ~Q(id=current_user.id) & Q(status=status))
        else:
            pass
        # applications = Application.objects.filter(~Q(id=current_user.id) & Q(
        #     district=current_user.district) & Q(status=status))
        context = {
            'applications': applications,
            'current_user_role': current_user.role
        }
        return render(request, 'pending-applications.html', context)
    else:
        context = {
            'errorMessage': "You're Not Authenticated to this page.",
            'errorCode': 401
        }
        return render(request, 'error.html', context)


def events(request):
    return render(request, 'events.html')


def modules(request):
    return render(request, 'modules.html')


def status_check(request):
    if 'authenticated_id' in request.session:
        id = request.session.get('authenticated_id')
        application_user = Application.objects.get(id=id)
        context = {
            'application_info': application_user
        }
        return render(request, 'application_status.html', context)
    else:
        context = {
            'errorMessage': "You're Not Authenticated to this page.",
            'errorCode': 401
        }
        return render(request, 'error.html', context)


def registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        date_of_birth = request.POST.get('dob')

        languages_spoken = request.POST.getlist('languages')
        languages_spoken_other = request.POST.getlist('languages_other', None)

        if 'others' in languages_spoken:
            languages_spoken.remove('others')
            languages_spoken += languages_spoken_other

        district = request.POST.get('district')
        mobile_number = request.POST.get('mobile')
        email_address = request.POST.get('email')
        whatsapp_number = request.POST.get('whatsapp')
        address = request.POST.get('address')

        profession = request.POST.get('profession')
        if profession == 'others':
            profession = request.POST.get('profession_other', None)

        educational_qualification = request.POST.get('education_qualification')
        designation = request.POST.get('designation')
        in_service_or_retired = request.POST.get('employment_status')

        role = request.POST.get('role')
        module_of_interest = 'NA'

        type_of_employment = request.POST.get('employment_type')
        if type_of_employment == 'others':
            type_of_employment = request.POST.get(
                'employment_type_other', None)

        if role == "rp":
            module_of_interest = request.POST.get('module_interested', None)
            if module_of_interest == 'others':
                module_of_interest = request.POST.get(
                    'module_interested_other', None)

        community = request.POST.get('community', None)
        marital_status = request.POST.get('marital_status', None)
        monthly_income = request.POST.get('monthly_income', None)
        father_or_spouse_name = request.POST.get('father_or_spouse_name', None)
        father_or_spouse_monthly_income = request.POST.get(
            'father_or_spouse_monthly_income', None)
        father_or_spouse_occupation = request.POST.get(
            'father_or_spouse_occupation', None)
        number_of_children = request.POST.get('number_of_children', None)
        invoved_in_any_social_activities = request.POST.get(
            'social_activities', None)
        affiliated_with_any_ngo_or_trust = request.POST.get(
            'ngo_or_trust', None)
        hours_can_dedicate = request.POST.get(
            'available_hours', None)
        own_vehicle = request.POST.get('own_vehicle', None)
        willing_to_attend_residential_training_programs = request.POST.get(
            'residential_training', None)
        money_can_you_donate_per_month = request.POST.get(
            'money_can_donate', None)
        religion = request.POST.get('religion', None)
        believe_in_god = request.POST.get('believe_in_god', None)
        call_brahmins_for_rituals = request.POST.get(
            'call_brahmins_for_rituals', None)
        believe_in_rituals = request.POST.get('believe_in_rituals', None)
        worship_of_heirlooms = request.POST.get('worship_of_heirlooms', None)
        cause_for_untouchability = request.POST.get(
            'cause_for_untouchability', None)
        main_problem_of_dalits = request.POST.get('problem_of_dalits', None)
        untouchability_related_to_religion = request.POST.get(
            'related_to_religion', None)
        solution_given_by_dr_ambedkar_for_untouchability = request.POST.get(
            'solution_givenby_ambedkar', None)
        solution_for_untouchability_your_pov = request.POST.get(
            'solution_for_untouchability', None)
        read_ambedkar_books = request.POST.get('ambedkar_books', None)
        willing_to_volunteer_for_free = request.POST.get(
            'willing_to_volunteer', None)
        hobby = request.POST.get('hobby', None)
        additional_skills = request.POST.get('additional_skills', None)
        willing_to_visit_adw_hostels = request.POST.get(
            'visit_adw_hostels', None)
        social_media_account = request.POST.get('social_media_account', None)
        do_you_agree_that_conversion_is_a_solution_for_untouchability = request.POST.get(
            'conversion', None)
        is_untouchability_prevalent_nowadays = request.POST.get(
            'untouchability_prevalent', None)
        how_many_assistant_district_coordinators_you_can_gather = request.POST.get(
            'adc_can_gather', None)
        affiliated_to_any_political_party = request.POST.get(
            'political_party', None)
        password = make_password(request.POST.get('password'))

        status = 'Pending Approval of District Coordinator'
        approved_by_dc = False
        approved_by_zc = False
        approved_by_sc = False

        role_value = request.session.get('role')

        if role_value == 'DC':
            status = 'Pending Approval of Zonal Coordinator'
            approved_by_dc = True
            approved_by_zc = False
            approved_by_sc = False
        elif role_value == 'ZC':
            status = 'Pending Approval of State Coordinator'
            approved_by_dc = True
            approved_by_zc = True
            approved_by_sc = False
        elif role_value == 'SC':
            status = 'Approved'
            approved_by_dc = True
            approved_by_zc = True
            approved_by_sc = True
        else:
            pass
#
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
            email_address=email_address,
            role=role,
            module_of_interest=module_of_interest,
            community=community,
            marital_status=marital_status,
            monthly_income=monthly_income,
            father_or_spouse_name=father_or_spouse_name,
            father_or_spouse_monthly_income=father_or_spouse_monthly_income,
            father_or_spouse_occupation=father_or_spouse_occupation,
            number_of_children=number_of_children,
            invoved_in_any_social_activities=invoved_in_any_social_activities,
            affiliated_with_any_ngo_or_trust=affiliated_with_any_ngo_or_trust,
            hours_can_dedicate=hours_can_dedicate,
            own_vehicle=own_vehicle,
            willing_to_attend_residential_training_programs=willing_to_attend_residential_training_programs,
            money_can_you_donate_per_month=money_can_you_donate_per_month,
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
            hobby=hobby,
            additional_skills=additional_skills,
            willing_to_visit_adw_hostels=willing_to_visit_adw_hostels,
            social_media_account=social_media_account,
            do_you_agree_that_conversion_is_a_solution_for_untouchability=do_you_agree_that_conversion_is_a_solution_for_untouchability,
            is_untouchability_prevalent_nowadays=is_untouchability_prevalent_nowadays,
            how_many_assistant_district_coordinators_you_can_gather=how_many_assistant_district_coordinators_you_can_gather,
            affiliated_to_any_political_party=affiliated_to_any_political_party,
            password=password,
            status=status,
            approved_by_dc=approved_by_dc,
            approved_by_zc=approved_by_zc,
            approved_by_sc=approved_by_sc
        )
        application.save()

        messages.success(
            request, f'Registration successful. Your ID is {application.id}. Please note down this ID to track your application status.')
        if 'authenticated_id' in request.session:
            return redirect('home')
        else:
            return redirect('login')
    return render(request, 'registration.html')
