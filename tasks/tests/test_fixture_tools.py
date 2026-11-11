import pytest

@pytest.fixture
def report(tmp_path):
    path = tmp_path / "report.txt"
    yield path
    path.unlink(missing_ok=True)

def test_report(report):
    report.write_text("SOS", encoding="utf-8")
    assert report.read_text(encoding="utf-8") == "SOS"


from morse import decode

def show(code):
    print(decode(code))

def test_show(capsys):
    show("... --- ...")
    assert capsys.readouterr().out == "SOS\n"


from os import getenv

def catalog_timeout():
    return int(getenv("CATALOG_TIMEOUT", "3"))

def test_timeout(monkeypatch):
    monkeypatch.setenv("CATALOG_TIMEOUT", "8")
    assert catalog_timeout() == 8
