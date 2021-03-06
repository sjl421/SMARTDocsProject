from django.urls import path
from main import views

urlpatterns = [
	path('deanery/students/', views.all_students),
	path('student/practice/<int:practice_id>/diary/', views.student_diary),
	path('student/practice/<int:practice_id>/ind_task/', views.student_ind_task),
	path('student/practice/<int:practice_id>/report_title/', views.student_title),
	path('deanery/practice/<int:practice_id>/students/list/', views.get_students),
	path('deanery/practices/', views.all_practices),
	path('deanery/practice/create/', views.create_practice),
	path('deanery/practice/delete/<int:practice_id>/', views.delete_practice),	
	path('deanery/practice/list/', views.get_practices),
	path('deanery/practice/get/<int:practice_id>/', views.get_practice_view),
	path('deanery/document/change_status/', views.change_document_status),
	path('user/login/', views.new_login),
	path('user/logout/', views.new_logout),
	path('user/main/', views.main_redirect),
]