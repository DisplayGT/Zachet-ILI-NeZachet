from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required
from ..models.repo import KidsRepo
from ..models.tables import db, Kids

bp = Blueprint("kids", __name__, url_prefix="/kids")

@bp.get("/")
@login_required
def list_kids():
    repo = KidsRepo(db)
    kids = repo.all()
    return render_template("list_kids.html", kids=kids)

@bp.post("/")
def create_kids():
    repo = KidsRepo(db)
    kid = request.form.get("kid")
    birth = request.form.get("birth")
    groupp = request.form.get("groupp")
    adress = request.form.get("adress")
    state = request.form.get("state")
    repo.add(kid, birth, groupp, adress, state)
    return redirect(url_for("kids.list_kids"))

@bp.post("/<int:kid_id>/delete")
def delete_kids(kid_id):
    kid = Kids.query.get_or_404(kid_id)
    db.session.delete(kid)
    db.session.commit()
    return redirect(url_for("kids.list_kids"))

@bp.post("/<int:kid_id>/update")
def update_kids(kid_id):
    kid = Kids.query.get_or_404(kid_id)
    kid.kid = request.form.get("kid", kid.kid)
    kid.birth = request.form.get("birth", kid.birth)
    kid.groupp = request.form.get("groupp", kid.groupp)
    kid.adress = request.form.get("adress", kid.adress)
    kid.state = request.form.get("state", kid.state)
    db.session.commit()
    return redirect(url_for("kids.list_kids"))