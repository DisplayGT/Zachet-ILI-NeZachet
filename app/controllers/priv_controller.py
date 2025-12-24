from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required
from ..models.repo import PrivivkiRepo
from ..models.tables import db, Privivki

bp = Blueprint("privivki", __name__, url_prefix="/privivki")

@bp.get("/")
@login_required
def list_priv():
    repo = PrivivkiRepo(db)
    privivki = repo.all()
    return render_template("list_privivki.html", privivki=privivki)

@bp.post("/")
def create_priv():
    repo = PrivivkiRepo(db)
    fullname = request.form.get("fullname")
    date = request.form.get("date")
    preparat = request.form.get("preparat")
    vacine = request.form.get("vacine")
    method = request.form.get("method")
    repo.add(fullname, date, preparat, vacine, method)
    return redirect(url_for("privivki.list_priv"))

@bp.post("/<int:priv_id>/delete")
def delete_priv(priv_id):
    priv = Privivki.query.get_or_404(priv_id)
    db.session.delete(priv)
    db.session.commit()
    return redirect(url_for("privivki.list_priv"))

@bp.post("/<int:priv_id>/update")
def update_priv(priv_id):
    priv = Privivki.query.get_or_404(priv_id)
    priv.fullname = request.form.get("fullname", priv.fullname)
    priv.date = request.form.get("date", priv.date)
    priv.preparat = request.form.get("preparat", priv.preparat)
    priv.vacine = request.form.get("vacine", priv.vacine)
    priv.method = request.form.get("method", priv.method)
    db.session.commit()
    return redirect(url_for("privivki.list_priv"))