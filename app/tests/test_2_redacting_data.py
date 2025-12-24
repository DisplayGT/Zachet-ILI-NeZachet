def test_preps_update_ok(client):
    with client.application.app_context():
        from app.models.repo import PreparatsRepo
        from app.models.tables import db, Preparats
        repo = PreparatsRepo(db)
        repo.add("Пацерикс", "000", "000", "000", "000")
        prep = Preparats.query.filter_by(name="Пацерикс").first()
        prep_id = prep.id

    rv = client.post(f"/preparats/{prep_id}/update", data={
        "name": "Пацерикс-Обновленный",
        "serial": "111",
        "doze": "111",
        "count": "111",
        "registr": "111"
    }, follow_redirects=True)
    assert rv.status_code == 200
    assert "Пацерикс-Обновленный" in rv.get_data(as_text=True)


def test_groups_update_ok(client):
    with client.application.app_context():
        from app.models.repo import GroupsRepo
        from app.models.tables import db, Groups
        repo = GroupsRepo(db)
        repo.add("Тестовая группа", "000", "000")
        group = Groups.query.filter_by(group_name="Тестовая группа").first()
        group_id = group.id

    rv = client.post(f"/groups/{group_id}/update", data={
        "group_name": "Тестовая группа 2",
        "teacher": "111",
        "how_many": "111"
    }, follow_redirects=True)
    assert rv.status_code == 200
    assert "Тестовая группа 2" in rv.get_data(as_text=True)


def test_kids_update_ok(client):
    with client.application.app_context():
        from app.models.repo import KidsRepo
        from app.models.tables import db, Kids
        repo = KidsRepo(db)
        repo.add("Тестовый Тест Тестович", "000", "000", "000", "000")
        kid = Kids.query.filter_by(kid="Тестовый Тест Тестович").first()
        kid_id = kid.id

    rv = client.post(f"/kids/{kid_id}/update", data={
        "kid": "Тестовый Обновленный",
        "birth": "111",
        "groupp": "111",
        "adress": "111",
        "state": "111"
    }, follow_redirects=True)
    assert rv.status_code == 200
    assert "Тестовый Обновленный" in rv.get_data(as_text=True)


def test_privs_update_ok(client):
    with client.application.app_context():
        from app.models.repo import PrivivkiRepo
        from app.models.tables import db, Privivki
        repo = PrivivkiRepo(db)
        repo.add("Иванов Иван", "000", "000", "000", "000")
        priv = Privivki.query.filter_by(fullname="Иванов Иван").first()
        priv_id = priv.id

    rv = client.post(f"/privivki/{priv_id}/update", data={
        "fullname": "Иванов Иван Обновленный",
        "date": "111",
        "preparat": "111",
        "vacine": "111",
        "method": "111"
    }, follow_redirects=True)
    assert rv.status_code == 200
    assert "Иванов Иван Обновленный" in rv.get_data(as_text=True)