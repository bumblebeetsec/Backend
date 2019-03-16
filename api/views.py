from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Student, Organisation, Scholarship, Application
import json
from json import JSONDecodeError
from django.forms.models import model_to_dict

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
    if len(existing)>0:
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
        return JsonResponse({'exists': False})
    else:
        organisation_dict = model_to_dict(existing[0])
        organisation_dict['exists'] = True
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
    if len(existing)>0:
        try:
            existing.update(**content)
        except Exception:
            print("Invalid update")
            return JsonResponse({'success': False})
    else:
        # try:
        new_org = Student(**content)
        # except Exception:
            # print("Invalid create")
            # return JsonResponse({'success': False})
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
        return JsonResponse({'exists': False})
    else:
        student_dict = model_to_dict(existing[0])
        student_dict['exists'] = True
        return JsonResponse(student_dict)


# @csrf_exempt
# def get_scholarship(request):
#     all_scholarships = Scholarship.objects.all()
#     scholarships = []
#     for scholarship in all_scholarships:
#         scholarships.append(model_to_dict(scholarship))
#     