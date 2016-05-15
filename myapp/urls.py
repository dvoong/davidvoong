from django.conf.urls import url
from myapp import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^home$', views.home),
    url(r'welcome', views.welcome),
    url(r'^breathe$', views.breathe),
    url(r'^submit-name$', views.submit_name),
    url(r'^submit-age$', views.submit_age),
    url(r'^intro$', views.intro),
    url(r'^intro2$', views.intro2),
    url(r'^intro3$', views.intro3),
    url(r'^getting-started$', views.getting_started),
    url(r'^your-symptoms$', views.your_symptoms),
    url(r'^how-to-use-this-app$', views.how_to_use),
    url(r'^after-an-episode$', views.how_to_after_an_episode),
    url(r'^post-episode$', views.post_episode),
    url(r'^monitoring-your-progress$', views.monitoring_your_progress),
    url(r'^what-is-cbt$', views.what_is_cbt),
    url(r'^what-is-fnd$', views.what_is_fnd),
    url(r'^fin$', views.fin),
    url(r'^relaxing-sounds$', views.relaxing_sounds),
    url(r'^finger-exercises$', views.finger_exercises),
    url(r'^inspiration$', views.inspiration),
    url(r'^post-episode-details-submitted$', views.post_episode_details_submitted),
    url(r'^day-log$', views.day_log)
]
