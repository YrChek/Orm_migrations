from django.contrib import admin

from .models import Student, Teacher


class TeacherStudentInline(admin.TabularInline):
    model = Student.teachers.through
    extra = 0


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    inlines = [TeacherStudentInline, ]
    exclude = ('teachers', )


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    inlines = [TeacherStudentInline, ]
