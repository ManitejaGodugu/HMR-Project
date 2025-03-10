from django.contrib import admin
from django.contrib import messages
from .models import Department

class DepartmentAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('dept_name', 'description', 'status', 'created_at', 'updated_at')

    # Add a search bar to search by department name or description
    search_fields = ('dept_name', 'description')

    # Add filters for status and creation date
    list_filter = ('status', 'created_at')

    # Fields that can be edited directly in the list view
    list_editable = ('status',)

    # Order departments by creation date (newest first)
    ordering = ('-created_at',)

    # Custom action to mark selected departments as inactive
    def make_inactive(self, request, queryset):
        updated_count = queryset.update(status='inactive')
        self.message_user(request, f"{updated_count} departments marked as inactive.", messages.SUCCESS)

    make_inactive.short_description = "Mark selected departments as inactive"

    # Add the custom action to the admin interface
    actions = [make_inactive]

# Register the Department model with the custom admin class
admin.site.register(Department, DepartmentAdmin)