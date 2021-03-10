from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import AbstractUserCreationForm, AbstractUserChangeForm
from .models import User # UserProfile

# class UserProfileInline(admin.StackedInline):
#     model = UserProfile
#     can_delete = False
#     verbose_name_plural = 'Profile'
#     fk_name = 'user'

class AbstractUserAdmin(admin.ModelAdmin):
    add_form = AbstractUserCreationForm
    form = AbstractUserChangeForm
    model = User
    list_display = ['username', 'email', 'role']


    # inlines = (UserProfileInline, )

    # def get_inline_instances(self, request, obj=None):
    #     if not obj:
    #         return list()
    #     return super(AbstractUserAdmin, self).get_inline_instances(request, obj)


admin.site.register(User, AbstractUserAdmin)
# admin.site.register(UserProfile)
