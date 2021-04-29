from django.contrib import admin


from .models import User, Student






class UserAdmin(admin.ModelAdmin):
    model = User
    list_display = ['username', 'is_patient', 'phone']


class StudentAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'program', 'grades', 'courses')
    list_filter = ('program', 'courses', 'grades')
    change_list_template = 'change_list_graph.html'


admin.site.register(Student, StudentAdmin)
admin.site.register(User, UserAdmin)
