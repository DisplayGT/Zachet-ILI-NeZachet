from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required
from ..models.repo import PreparatsRepo
from ..models.tables import db, Preparats

bp = Blueprint("preparats", __name__, url_prefix="/preparats")

@bp.get("/")
@login_required
def list_prep():
    repo = PreparatsRepo(db)
    preparats = repo.all()
    return render_template("list_preparats.html", preparats=preparats)

@bp.post("/")
def create_prep():
    repo = PreparatsRepo(db)
    name = request.form.get("name")
    serial = request.form.get("serial")
    doze = request.form.get("doze")
    count = request.form.get("count")
    registr = request.form.get("registr")
    repo.add(name, serial, doze, count, registr)
    return redirect(url_for("preparats.list_prep"))

@bp.post("/<int:prep_id>/delete")
def delete_prep(prep_id):
    prep = Preparats.query.get_or_404(prep_id)
    db.session.delete(prep)
    db.session.commit()
    return redirect(url_for("preparats.list_prep"))

@bp.post("/<int:prep_id>/update")
def update_prep(prep_id):
    prep = Preparats.query.get_or_404(prep_id)
    prep.name = request.form.get("name", prep.name)
    prep.serial = request.form.get("serial", prep.serial)
    prep.doze = request.form.get("doze", prep.doze)
    prep.count = request.form.get("count", prep.count)
    prep.registr = request.form.get("registr", prep.registr)
    db.session.commit()
    return redirect(url_for("preparats.list_prep"))