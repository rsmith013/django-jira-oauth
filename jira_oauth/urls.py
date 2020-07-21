from django.urls import path
import jira_oauth.views

urlpatterns = [
    path('authorize/', jira_oauth.views.authorize, name='jira-oauth-authorize'),
    path('access_token/', jira_oauth.views.access_token, name='jira-oauth-access-token'),
]
