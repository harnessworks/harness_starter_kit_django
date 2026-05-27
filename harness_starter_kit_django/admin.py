from django.contrib import admin

from .models import Post


admin.site.site_header = "게시판 관리자"
admin.site.site_title = "게시판 관리자"
admin.site.index_title = "사용자 및 게시글 관리"


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_at", "updated_at")
    list_filter = ("owner", "created_at", "updated_at")
    search_fields = ("title", "content", "owner__username")
    autocomplete_fields = ("owner",)
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "created_at"
