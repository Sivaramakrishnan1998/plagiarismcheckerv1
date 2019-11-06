
from django.contrib import admin
from .models import Data,Document,Apidocument,Credits,Profile,Institution,Subuser
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Data)
admin.site.register(Document)
admin.site.register(Apidocument)
admin.site.register(Credits)
admin.site.register(Profile)

admin.site.register(Subuser)



class InstitutionAdmin(admin.ModelAdmin):
	list_display = [field.name for field in Institution._meta.get_fields()]
	model = Institution
admin.site.register(Institution,InstitutionAdmin)
class ProfileAdmin(admin.ModelAdmin):
	list_display = ("username",)
	model = Profile
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		if request.user.is_superuser:
			return get_queryset
		return User.objects.filter(created_by=request.user) or qs.none()



	def save_model(self, request, obj, form, change):
		if change:
			obj.modified_by = request.user
		else:
			obj.created_by = request.user
		obj.save()