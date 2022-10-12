import pytest 
from .conftest import add_log

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

@pytest.mark.django_db
def test_log_detail_view(client, add_log):
    log = add_log('I like to code')
    url = reverse('log_detail', kwargs={'id': log.id })
    response = client.get(url)

    assert response.status_code == 200
