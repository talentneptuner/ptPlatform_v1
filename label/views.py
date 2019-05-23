import json
import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import View
from .models import CatagoryS, CatagoryF, labelRecord
from users.models import UserProfile
from info.models import Image,Text
from label.models import labelitem
# Create your views here.

class GetCatagory(View):

    def get(self,request):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        all_cat_f = CatagoryF.objects.all()
        items = []
        for cat_f in all_cat_f:
            cat_s_list = []
            all_cat_s = CatagoryS.objects.filter(catagory_f=cat_f)
            for cat_s in all_cat_s:
                cat_s_list.append(dict(id = cat_s.id, name=cat_s.name))
            items.append(dict(id=cat_f.id, name=cat_f.name, sub_cat=cat_s_list))
        return HttpResponse(json.dumps(items, ensure_ascii=False), content_type='application/json')

class GetAllUnlabeled(View):


    def get(self,request):
        if not request.user.is_authenticated:
            return render(request, 'login.html')
        user = request.user
        all_ids = [str(i[0]) for i in user.get_data_for_label()]
        return HttpResponse(json.dumps(all_ids, ensure_ascii=False), content_type='application/json')

class NextItem(View):

    def get(self, request):
        label_id = request.GET.get('label_id')
        record = labelRecord.objects.get(id=label_id)
        image = '{}.jpg'.format(str(Image.objects.get(id=record.image_id).img_name))
        text = Text.objects.get(id=record.text_id).text
        result = dict(id=label_id, image = image, text=text)
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json')

class LabelItem(View):

    def post(self,request):
        try:
            id = request.POST.get('id')
            labels = request.POST.getlist('label[]')
            objects_list = request.POST.get('objects_list')
            for label in labels:
                record = labelitem()
                record.recorder = request.user
                record.image = '/Image/'+Image.objects.get(id=labelRecord.objects.get(id=id).image_id).img_name+'.jpg'
                record.text = Text.objects.get(id=labelRecord.objects.get(id=id).text_id).text
                record.mid = Text.objects.get(id=labelRecord.objects.get(id=id).text_id).mid
                record.cat_id = CatagoryS.objects.get(id=label)
                if record.cat_id.name == '对象相关':
                    record.objects_list = objects_list
                record.save()
            label_record = labelRecord.objects.get(id=id)
            label_record.has_done = True
            label_record.save()
            return HttpResponse('{"status":"success"}', content_type='application/json')
        except:
            return HttpResponse('{"status":"fail"}', content_type='application/json')

class Status(View):

    def get(self,request):
        label_nums = request.user.get_labeled_data_count()
        unlabel_nums = request.user.get_unlabeled_data_count()
        result = dict(label_nums=label_nums, unlabel_nums=unlabel_nums)
        return HttpResponse(json.dumps(result, ensure_ascii=False), content_type='application/json')



