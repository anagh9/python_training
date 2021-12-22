# Model Admin

"""
The ModelAdmin class is the representation of a model in the admin interface. We do All operation in admin.py of application

Syntax :-
Class ModelAdminClassName(admin.ModelAdmin):
    list_display = ('fieldname1','fieldnamw2',....)

-- Register Above Created Class In admin.py
admin.site.register(ModelClassName,ModelAdminClassName)


-- Register Model By Decorator
@admin.register(ModelClassName1,ModelClassName2,...,site=custom_admin_site)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('id','studid','stuname','stumail','stupass')

"""

# Note - If we pass single value in tuple we have to end it by comme like  (name,)
