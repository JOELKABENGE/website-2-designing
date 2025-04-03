from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegistrationView, LoginView, MyTokenObtainPairView, MyTokenRefreshView,
    PasswordResetView, PasswordChangeView,
    DepartmentListCreateView, DepartmentDetailView,
    IssueListCreateView, IssueDetailView,
    CategoryViewSet, ActivityListView,
    ContactFormView
)

# Create a router for ViewSets
router = DefaultRouter()
router.register(r'categories', CategoryViewSet)

app_name = 'UNI'

urlpatterns = [
    # User registration and authentication
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    # JWT token authentication
    path(
        'api/token/', 
        MyTokenObtainPairView.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        MyTokenRefreshView.as_view(),
        name='token_refresh'
    ),

    # Password management
    path(
        'password-reset/',
        PasswordResetView.as_view(),
        name='password_reset'
    ),
    path(
        'password-change/',
        PasswordChangeView.as_view(),
        name='password_change'
    ),

    # Department endpoints
    path(
        'departments/',
        DepartmentListCreateView.as_view(),
        name='department_list_create'
    ),
    path(
        'departments/<int:pk>/',
        DepartmentDetailView.as_view(),
        name='department_detail'
    ),

    # Issue endpoints
    path('issues/', IssueListCreateView.as_view(), name='issue_list_create'),
    path('issues/<int:pk>/', IssueDetailView.as_view(), name='issue_detail'),

    # Contact form endpoint
    path('contact-form/', ContactFormView.as_view(), name='contact-form'),
    
    # Include router URLs for ViewSets
    path('', include(router.urls)),
    
    # Activity endpoints

    path('activities/', ActivityListView.as_view(), name='activity_list'),
    

]