from .tables import Preparats, Groups, Kids, Privivki, db


class PreparatsRepo:
    def __init__(self, db_instance=None):
        self.db = db_instance or db

    def all(self):
        return Preparats.query.all()

    def add(self, name, serial, doze, count, registr):
        new_prep = Preparats(name=name, serial=serial, doze=doze, count=count, registr=registr)
        self.db.session.add(new_prep)
        self.db.session.commit()
        return new_prep


class GroupsRepo:
    def __init__(self, db_instance=None):
        self.db = db_instance or db

    def all(self):
        return Groups.query.all()

    def add(self, group_name, teacher, how_many):
        new_group = Groups(group_name=group_name, teacher=teacher, how_many=how_many)
        self.db.session.add(new_group)
        self.db.session.commit()
        return new_group


class KidsRepo:
    def __init__(self, db_instance=None):
        self.db = db_instance or db

    def all(self):
        return Kids.query.all()

    def add(self, kid, birth, groupp, adress, state):
        new_kid = Kids(kid=kid, birth=birth, groupp=groupp, adress=adress, state=state)
        self.db.session.add(new_kid)
        self.db.session.commit()
        return new_kid


class PrivivkiRepo:
    def __init__(self, db_instance=None):
        self.db = db_instance or db

    def all(self):
        return Privivki.query.all()

    def add(self, fullname, date, preparat, vacine, method):
        new_priv = Privivki(fullname=fullname, date=date, preparat=preparat, vacine=vacine, method=method)
        self.db.session.add(new_priv)
        self.db.session.commit()
        return new_priv