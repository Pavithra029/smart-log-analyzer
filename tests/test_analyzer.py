from app.analyzer import analyze_log

def test_analyze_log():
    sample_log = "INFO Start\nERROR Something failed\nWARNING Low memory\nERROR Failed again"
    result = analyze_log(sample_log)
    assert result["total_errors"] == 2
    assert result["total_warnings"] == 1
