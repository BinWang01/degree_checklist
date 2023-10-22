from django import forms
from data.models import College, Department, Degree, Area, Course, Area_Course

class CollegeForm(forms.ModelForm):
    class Meta:
        model = College
        fields = "__all__"

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = "__all__"

class DegreeForm(forms.ModelForm):
    class Meta:
        model = Degree
        fields = "__all__"


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = "__all__"

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = "__all__"

class AreaCourseForm(forms.ModelForm):
    class Meta:
        model = Area_Course
        fields = "__all__"