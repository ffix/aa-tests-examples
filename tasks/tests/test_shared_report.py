import pytest


@pytest.fixture
def report(tmp_path):
    path = tmp_path / "report.txt"
    path.write_text("SOS", encoding="utf-8")
    return path


def test_report_name(report):
    assert report.name == "report.txt"


def test_report_text(report):
    assert report.read_text(encoding="utf-8") == "SOS"
