import pytest

from journal.models import Log, Entry

@pytest.mark.django_db
def test_log_model():
    log = Log(content="I am very happy today" )
    log.save() 

    assert log.content == "I am very happy today"
    assert str(log) == log.content
    assert log.date_added

@pytest.mark.django_db
def test_entry_model():
    log = Log(content="I like to code")
    log.save() 

    entry = Entry(topic=log, content="I like to code in python")
    entry.save() 

    assert entry.topic == log
    assert entry.content == "I like to code in python"
    assert entry.date_added
    assert str(entry) == "I like to code in python"
    