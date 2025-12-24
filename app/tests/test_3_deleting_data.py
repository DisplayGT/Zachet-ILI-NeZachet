def test_preps_delete_ok(client):
    with client.application.app_context():
        from app.models.repo import PreparatsRepo
        from app.models.tables import db, Preparats
        repo = PreparatsRepo(db)
        repo.add("Пацерикс", "000", "000", "000", "000")
        prep = Preparats.query.filter_by(name="Пацерикс").first()
        prep_id = prep.id

    rv = client.post(f"/preparats/{prep_id}/delete", follow_redirects=True)
    assert rv.status_code == 200

    with client.application.app_context():
        prep = Preparats.query.filter_by(id=prep_id).first()
        assert prep is None


def test_groups_delete_ok(client):
    with client.application.app_context():
        from app.models.repo import GroupsRepo
        from app.models.tables import db, Groups
        repo = GroupsRepo(db)
        repo.add("Тестовая группа", "000", "000")
        group = Groups.query.filter_by(group_name="Тестовая группа").first()
        group_id = group.id

    rv = client.post(f"/groups/{group_id}/delete", follow_redirects=True)
    assert rv.status_code == 200

    with client.application.app_context():
        group = Groups.query.filter_by(id=group_id).first()
        assert group is None


def test_kids_delete_ok(client):
    with client.application.app_context():
        from app.models.repo import KidsRepo
        from app.models.tables import db, Kids
        repo = KidsRepo(db)
        repo.add("Тестовый Тест Тестович", "000", "000", "000", "000")
        kid = Kids.query.filter_by(kid="Тестовый Тест Тестович").first()
        kid_id = kid.id

    rv = client.post(f"/kids/{kid_id}/delete", follow_redirects=True)
    assert rv.status_code == 200

    with client.application.app_context():
        kid = Kids.query.filter_by(id=kid_id).first()
        assert kid is None


def test_privs_delete_ok(client):
    with client.application.app_context():
        from app.models.repo import PrivivkiRepo
        from app.models.tables import db, Privivki
        repo = PrivivkiRepo(db)
        repo.add("Иванов Иван", "000", "000", "000", "000")
        priv = Privivki.query.filter_by(fullname="Иванов Иван").first()
        priv_id = priv.id

    rv = client.post(f"/privivki/{priv_id}/delete", follow_redirects=True)
    assert rv.status_code == 200

    with client.application.app_context():
        priv = Privivki.query.filter_by(id=priv_id).first()
        assert priv is None