import pytest

from journal.models import Log

@pytest.mark.django_db
def test_log_model():
    log = Log(content="I am very happy today" )
    log.save() 

    assert log.content == "I am very happy today"
    assert str(log) == log.content
    assert log.date_added