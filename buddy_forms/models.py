from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.


class BackForm(models.Model):
    user_id = models.CharField(max_length=10, null=False, unique=True)
    document_type = models.CharField(max_length=10, default='2', null=False)
    form_url = models.CharField(max_length=500, default=None)
    status = models.CharField(max_length=100, default=None, null=True)
    # back form fields
    class_10_board = models.CharField(default=None, max_length=100, null=True)
    class_10_passing_year = models.CharField(default=None, max_length=100, null=True)
    class_10_total_marks = models.CharField(default=None, max_length=100, null=True)
    class_10_marks_obtained = models.CharField(default=None, max_length=100, null=True)
    class_12_board = models.CharField(default=None, max_length=100, null=True)
    class_12_passing_year = models.CharField(default=None, max_length=100, null=True)
    class_12_total_marks = models.CharField(default=None, max_length=100, null=True)
    class_12_marks_obtained = models.CharField(default=None, max_length=100, null=True)
    class_12_stream = models.CharField(default=None, max_length=100, null=True)
    graduation_stream = models.CharField(default=None, max_length=100, null=True)
    graduation_course_duration = models.CharField(default=None, max_length=100, null=True)
    graduation_total_marks = models.CharField(default=None, max_length=100, null=True)
    graduation_marks_obtained = models.CharField(default=None, max_length=100, null=True)
    graduation_passing_year = models.CharField(default=None, max_length=100, null=True)
    post_graduation_stream = models.CharField(default=None, max_length=100, null=True)
    post_graduation_course_duration = models.CharField(default=None, max_length=100, null=True)
    post_graduation_total_marks = models.CharField(default=None, max_length=100, null=True)
    post_graduation_marks_obtained = models.CharField(default=None, max_length=100, null=True)
    post_graduation_passing_year = models.CharField(default=None, max_length=100, null=True)
    bank_name = models.CharField(default=None, max_length=100, null=True)
    ifsc_code = models.CharField(default=None, max_length=100, null=True)
    account_number = models.CharField(default=None, max_length=100, null=True)
    account_holder_name = models.CharField(default=None, max_length=100, null=True)
    relation_with_account_holder = models.CharField(default=None, max_length=100, null=True)
    no_bank_account = models.CharField(default=None, max_length=100, null=True)

    # back form accuracy fields
    class_10_board_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    class_10_passing_year_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    class_10_total_marks_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    class_10_marks_obtained_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    class_12_board_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    class_12_passing_year_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    class_12_total_marks_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    class_12_marks_obtained_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    class_12_stream_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    graduation_stream_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    graduation_course_duration_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    graduation_total_marks_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    graduation_marks_obtained_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    graduation_passing_year_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    post_graduation_stream_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    post_graduation_course_duration_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    post_graduation_total_marks_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    post_graduation_marks_obtained_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    post_graduation_passing_year_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    bank_name_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    ifsc_code_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    account_number_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    account_holder_name_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    relation_with_account_holder_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    no_bank_account_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)


class FrontForm(models.Model):
    user_id = models.CharField(max_length=10, null=False, unique=True)
    form_url = models.CharField(max_length=500, default=None)
    document_type = models.CharField(max_length=10, null=False)
    status = models.CharField(max_length=100, default=None, null=True)
    # front form fields
    created_date = models.DateTimeField(default=timezone.now)
    first_name = models.CharField(default=None, max_length=100, null=True)
    last_name = models.CharField(default=None, max_length=100, null=True)
    date_of_birth = models.CharField(default=None, max_length=100, null=True)
    aadhar_number = models.CharField(default=None, max_length=100, null=True)
    present_address = models.CharField(default=None, max_length=100, null=True)
    student_mobile_number = models.CharField(default=None, max_length=100, null=True)
    email = models.CharField(default=None, max_length=100, null=True)
    gender = models.CharField(default=None, max_length=100, null=True)
    number_of_brothers_sisters = models.CharField(default=None, max_length=100, null=True)
    religion = models.CharField(default=None, max_length=100, null=True)
    category = models.CharField(default=None, max_length=100, null=True)
    special_cases = models.CharField(default=None, max_length=100, null=True)
    disability = models.CharField(default=None, max_length=100, null=True)
    percentage_of_disability = models.CharField(default=None, max_length=100, null=True)
    talent_areas = models.CharField(default=None, max_length=100, null=True)
    awards = models.CharField(default=None, max_length=100, null=True)
    father_first_name = models.CharField(default=None, max_length=100, null=True)
    father_last_name = models.CharField(default=None, max_length=100, null=True)
    father_occupation = models.CharField(default=None, max_length=100, null=True)
    father_mobile_number = models.CharField(default=None, max_length=100, null=True)
    father_annual_income = models.CharField(default=None, max_length=100, null=True)
    father_email_id = models.CharField(default=None, max_length=100, null=True)
    mother_first_name = models.CharField(default=None, max_length=100, null=True)
    mother_last_name = models.CharField(default=None, max_length=100, null=True)
    mother_occupation = models.CharField(default=None, max_length=100, null=True)
    mother_annual_income = models.CharField(default=None, max_length=100, null=True)
    mother_email_id = models.CharField(default=None, max_length=100, null=True)
    mother_mobile_number = models.CharField(default=None, max_length=100, null=True)
    present_class = models.CharField(default=None, max_length=100, null=True)
    present_class_stream = models.CharField(default=None, max_length=100, null=True)
    mode_of_course = models.CharField(default=None, max_length=100, null=True)
    type_of_student = models.CharField(default=None, max_length=100, null=True)
    annual_fee = models.CharField(default=None, max_length=100, null=True)
    previous_class_passing_year = models.CharField(default=None, max_length=100, null=True)
    marks_obtained = models.CharField(default=None, max_length=100, null=True)
    total_marks = models.CharField(default=None, max_length=100, null=True)

    # front form accuracy fields
    first_name_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    last_name_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    date_of_birth_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    aadhar_number_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    present_address_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    student_mobile_number_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    email_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    gender_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    number_of_brothers_sisters_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    religion_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    category_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    special_cases_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    disability_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    percentage_of_disability_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    talent_areas_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    awards_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    father_first_name_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    father_last_name_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    father_occupation_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    father_mobile_number_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    father_annual_income_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    father_email_id_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    mother_first_name_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    mother_last_name_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    mother_occupation_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    mother_annual_income_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    mother_email_id_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    mother_mobile_number_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    present_class_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    present_class_stream_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    mode_of_course_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    type_of_student_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    annual_fee_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    previous_class_passing_year_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    marks_obtained_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)
    total_marks_CONFIDENCE = models.CharField(default=None, max_length=100, null=True)


class RotationAngles(models.Model):
    user_id = models.CharField(null=False, max_length=10, unique=True)
    rotation_angle = models.FloatField(null=True, default=None)
    document_type = models.CharField(max_length=10, null=True)
    errors = models.TextField(null=True ,default=None)
