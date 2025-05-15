from services.auth import login

def test_login_valid(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "admin" if not hasattr(_, "called") else "admin123")
    assert login() is True
