import pytest 

from journal.models import Log, Entry

@pytest.fixture(scope='function')
def add_log():
    def _add_movie(content):
        log = Log.objects.create(content=content)
        return log
    return _add_movie