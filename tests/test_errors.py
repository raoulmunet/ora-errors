from ora_errors import lookup,normalize_code,search

def test_normalize():
    assert normalize_code("1722")=="ORA-01722"
    assert normalize_code("ORA 12541")=="ORA-12541"

def test_lookup():
    assert "conversion" in lookup("ORA-01722")["meaning"].lower()

def test_search():
    assert any(c=="ORA-12541" for c,_ in search("listener"))
