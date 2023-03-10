from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin
from .models import User, DriverProfile
from .forms import UserImageCompressForm
from common.mixins import PhotoTagAdminMixin


@admin.register(User)
class UserAdmin2(UserAdmin, PhotoTagAdminMixin):
    # model = User
    list_display = (
        "photo_tag",
        "login",
        "is_active",
        "is_deleted",
    )
    list_display_links = ("login",)
    list_filter = (
        "is_active",
        "is_deleted",
    )
    list_editable = ("is_active", "is_deleted")
    readonly_fields = (
        "created_at",
        "updated_at",
        "last_login",
        "password",
    )
    search_fields = ("full_name",)
    list_per_page = 25
    form = UserImageCompressForm
    ordering = ["-created_at"]
    PhotoTagAdminMixin.photo_tag.short_description = "Фото"
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "login",
                    "email",
                    "phone",
                    "first_name",
                    "last_name",
                    "middle_name",
                    "code",
                    "photo",
                    "is_active",
                    "is_deleted",
                    "is_driver",
                    "is_client",
                    "created_at",
                    "updated_at",
                    "last_login",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "login",
                    "password1",
                    "password2",
                    "is_staff",
                ),
            },
        ),
    )

    # def has_delete_permission(self, request, obj=None):
    #     return False

    def has_module_permission(self, request):
        if request.user.is_superuser:
            return True
        return False


admin.site.unregister(Group)
admin.site.register(DriverProfile)
