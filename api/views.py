from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Organisation, Scholarship, Application
import json
from json import JSONDecodeError
from django.forms.models import model_to_dict
from django.db.models import Q


@csrf_exempt
def post_organisation(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid JSON")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Organisation.objects.filter(uid=uid)
    if len(existing) > 0:
        try:
            existing.update(**content)
        except Exception:
            print("Invalid update")
            return JsonResponse({'success': False})
    else:
        try:
            new_org = Organisation(**content)
        except Exception:
            print("Invalid create")
            return JsonResponse({'success': False})
        new_org.save()
    return JsonResponse({'success': True})


@csrf_exempt
def get_organisation(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid POST")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Organisation.objects.filter(uid=uid)
    if len(existing) == 0:
        return JsonResponse({'success': True, 'exists': False})
    else:
        organisation_dict = model_to_dict(existing[0])
        organisation_dict['exists'] = True
        organisation_dict['success'] = True
        return JsonResponse(organisation_dict)


@csrf_exempt
def post_student(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid JSON")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Student.objects.filter(uid=uid)
    if len(existing) > 0:
        try:
            existing.update(**content)
        except Exception:
            print("Invalid update")
            return JsonResponse({'success': False})
    else:
        try:
            new_org = Student(**content)
        except Exception:
            print("Invalid create")
            return JsonResponse({'success': False})
        new_org.save()
    return JsonResponse({'success': True})


@csrf_exempt
def get_student(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid POST")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Student.objects.filter(uid=uid)
    if len(existing) == 0:
        return JsonResponse({'success': True, 'exists': False})
    else:
        student_dict = model_to_dict(existing[0])
        student_dict['exists'] = True
        student_dict['success'] = True
        return JsonResponse(student_dict)


@csrf_exempt
def get_type(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid POST")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Student.objects.filter(uid=uid)
    if len(existing) > 0:
        return JsonResponse({'success': True, 'type': 'student'})
    existing = Organisation.objects.filter(uid=uid)
    if len(existing) > 0:
        return JsonResponse({'success': True, 'type': 'organisation'})
    return JsonResponse({'success': True, 'type': 'none'})


@csrf_exempt
def get_scholarship(request):
    all_scholarships = Scholarship.objects.all()
    scholarships = []
    for scholarship in all_scholarships:
        scholarship_entry = {"id": scholarship.id, "name": scholarship.name, "organisation_name":
                             scholarship.organisation.name, "description": scholarship.scholarship_description[:50]}
        scholarships.append(scholarship_entry)
    scholarship_dict = {'scholarships': scholarships, 'success': True}
    return JsonResponse(scholarship_dict)


@csrf_exempt
def get_scholarship_eligible(request):
    body_unicode = request.body.decode('utf-8')
    try:
        content = json.loads(body_unicode)
    except JSONDecodeError:
        print("Invalid POST")
        return JsonResponse({'success': False})
    try:
        uid = content['uid']
    except KeyError:
        return JsonResponse({'success': False})
    existing = Student.objects.filter(uid=uid)
    if len(existing) == 0:
        return JsonResponse({'success': False})
    student = existing[0]
    gender = student.gender
    state = student.state
    religion = student.religion
    max_annual_income = student.annual_income
    category = student.category
    course = student.course_interested_in
    physically_challenged = student.physically_challenged
    filtered_scholarships = Scholarship.objects.filter(Q(gender=gender) | Q(gender='')).filter(Q(state=state) | Q(state='')).filter(Q(religion=religion) | Q(religion='')).filter(Q(max_annual_income=max_annual_income) | Q(
        max_annual_income='')).filter(Q(category=category) | Q(category='')).filter(Q(course=course)).filter(Q(physically_challenged=physically_challenged) | Q(physically_challenged=''))
    scholarships = []
    for scholarship in filtered_scholarships:
        scholarship_entry = {"id": scholarship.id, "name": scholarship.name, "organisation_name":
                             scholarship.organisation.name, "description": scholarship.scholarship_description[:50]}
        scholarships.append(scholarship_entry)
    scholarship_dict = {'scholarships': scholarships, 'success': True}
    return JsonResponse(scholarship_dict)
