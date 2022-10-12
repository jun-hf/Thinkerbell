from urllib import response
import pytest 

from django.urls import reverse

@pytest.mark.django_db
def test_home_view(client):
    url = reverse('home')
    response = client.get(url)

    assert response.status_code == 200

@pytest.mark.django_db
def test_log_view(client):
    url = reverse('log')
    response = client.get(url)

    assert response.status_code == 200
