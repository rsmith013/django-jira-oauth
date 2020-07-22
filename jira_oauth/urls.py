from django.urls import path
import jira_oauth.views

app_name = 'jira_oauth'
urlpatterns = [
    path('authorize/', jira_oauth.views.authorize, name='jira_oauth_authorize'),
    path('access_token/', jira_oauth.views.access_token, name='jira_oauth_access_token'),
]
