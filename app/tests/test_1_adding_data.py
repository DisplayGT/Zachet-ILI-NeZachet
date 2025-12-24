def test_index_ok(client):
    rv = client.get("/")
    assert rv.status_code == 200
    assert "Учет прививок в детском саду" in rv.get_data(as_text=True)


def test_preps_ok(client):
    with client.application.app_context():
        from app.models.repo import PreparatsRepo
        from app.models.tables import db
        repo = PreparatsRepo(db)
        repo.add("Пацерикс", "000", "000", "000", "000")

    rv = client.get("/preparats/")
    assert rv.status_code == 200
    assert "Пацерикс" in rv.get_data(as_text=True)


def test_groups_ok(client):
    with client.application.app_context():
        from app.models.repo import GroupsRepo
        from app.models.tables import db
        repo = GroupsRepo(db)
        repo.add("Тестовая группа", "000", "000")

    rv = client.get("/groups/")
    assert rv.status_code == 200
    assert "Тестовая группа" in rv.get_data(as_text=True)


def test_kids_ok(client):
    with client.application.app_context():
        from app.models.repo import KidsRepo
        from app.models.tables import db
        repo = KidsRepo(db)
        repo.add("Тестовый Тест Тестович", "000", "000", "000", "000")

    rv = client.get("/kids/")
    assert rv.status_code == 200
    assert "Тестовый Тест Тестович" in rv.get_data(as_text=True)


def test_privs_ok(client):
    with client.application.app_context():
        from app.models.repo import PrivivkiRepo
        from app.models.tables import db
        repo = PrivivkiRepo(db)
        repo.add("Тестов", "000", "000", "000", "000")

    rv = client.get("/privivki/")
    assert rv.status_code == 200
    assert "Тестов" in rv.get_data(as_text=True)