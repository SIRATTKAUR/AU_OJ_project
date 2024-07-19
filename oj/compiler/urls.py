from django.urls import path
from .views import run_code_inline, submit_code_with_verdict

app_name = 'compiler'

urlpatterns = [
    path('run_code/<int:problem_id>/', run_code_inline, name='run_code_inline'),
    path('submit_code_with_verdict/<int:problem_id>/', submit_code_with_verdict, name='submit_code_with_verdict'),

]
