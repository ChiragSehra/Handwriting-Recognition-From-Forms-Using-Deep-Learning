from django.shortcuts import render
import json
from pprint import pprint
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from helpers import main
from .models import FrontForm, BackForm, RotationAngles


# Create your views here.

@api_view(["POST"])
def form_links(request):
    try:
        user_id = request.data["userEntryFormId"]
        form_side = request.data["documentType"]
        s3_link = request.data["fileURL"]

        if form_side == "1":
            empty_object = {'user_id': user_id, 'document_type': form_side, 'form_url': s3_link, 'status': 'In_Process'}
            obj = FrontForm.objects.create(**empty_object)
            # print(obj.pk)
            front_information, skewness_information = main.main(s3_link, form_side, user_id)
            print("front_information: {}".format(front_information))
            front_form_object = FrontForm(pk=obj.pk, user_id=user_id, document_type=form_side, form_url=s3_link,
                                          status="Success", **front_information)
            front_form_object.save()
            # FrontForm.objects.create(**front_information)
            RotationAngles.objects.create(**skewness_information)
            return Response(status=status.HTTP_200_OK, data={"data": front_information, "success": True})
        if form_side == "2":
            empty_object = {'user_id': user_id, 'document_type': form_side, 'form_url': s3_link,
                            'status': 'In_Process'}
            obj = BackForm.objects.create(**empty_object)
            print("Primary Key of this object: {}".format(obj.pk))
            back_information, skewness_information = main.main(s3_link, form_side, user_id)
            back_form_object = BackForm(pk=obj.pk, user_id=user_id, document_type=form_side,
                                        form_url=s3_link, status="Success", **back_information)
            back_form_object.save()
            # BackForm.objects.create(**back_information)
            print("skewness information : {}".format(skewness_information))
            RotationAngles.objects.create(**skewness_information)
            return Response(status=status.HTTP_200_OK, data={"data": back_information, "success": True})
    except Exception as e:
        # check if user_id already exists
        # if already exists in the table, then set status = Failed
        print("[IN FAILED]: Primary key of object is : {}".format(obj.pk))
        if form_side == "1":
            front_form_object = FrontForm(pk=obj.pk, user_id=user_id, document_type=form_side,
                                          form_url=s3_link, status="Failed")
            front_form_object.save()

            rotation_angle_object = RotationAngles(pk=obj.pk, user_id=user_id, document_type=form_side, rotation_angle=99, errors=str(e))

            rotation_angle_object.save()

        if form_side == "2":
            back_form_object = BackForm(pk=obj.pk, user_id=user_id, document_type=form_side,
                                        form_url=s3_link, status="Failed")
            back_form_object.save()

        return Response(status=status.HTTP_400_BAD_REQUEST, data={"message": str(e), "success": False})
