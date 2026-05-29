from django.contrib import admin

from .models import Comment, Post


admin.site.site_header = "게시판 관리자"
admin.site.site_title = "게시판 관리자"
admin.site.index_title = "사용자, 게시글 및 댓글 관리"


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    readonly_fields = ("created_at", "updated_at")


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "comment_count", "created_at", "updated_at")
    list_filter = ("owner", "created_at", "updated_at")
    search_fields = ("title", "content", "owner__username")
    autocomplete_fields = ("owner",)
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "created_at"
    inlines = (CommentInline,)

    @admin.display(description="댓글 수")
    def comment_count(self, obj):
        return obj.comments.count()


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "owner", "created_at", "updated_at")
    list_filter = ("owner", "created_at", "updated_at")
    search_fields = ("content", "post__title", "owner__username")
    autocomplete_fields = ("post", "owner")
    readonly_fields = ("created_at", "updated_at")
    date_hierarchy = "created_at"
