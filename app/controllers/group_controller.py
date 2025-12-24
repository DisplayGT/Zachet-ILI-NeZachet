from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_required
from ..models.repo import GroupsRepo
from ..models.tables import db, Groups

bp = Blueprint("groups", __name__, url_prefix="/groups")

@bp.get("/")
@login_required
def list_group():
    repo = GroupsRepo(db)
    groups = repo.all()
    return render_template("list_groups.html", groups=groups)

@bp.post("/")
def create_group():
    repo = GroupsRepo(db)
    group_name = request.form.get("group_name")
    teacher = request.form.get("teacher")
    how_many = request.form.get("how_many")
    repo.add(group_name, teacher, how_many)
    return redirect(url_for("groups.list_group"))

@bp.post("/<int:group_id>/delete")
def delete_group(group_id):
    group = Groups.query.get_or_404(group_id)
    db.session.delete(group)
    db.session.commit()
    return redirect(url_for("groups.list_group"))

@bp.post("/<int:group_id>/update")
def update_group(group_id):
    group = Groups.query.get_or_404(group_id)
    group.group_name = request.form.get("group_name", group.group_name)
    group.teacher = request.form.get("teacher", group.teacher)
    group.how_many = request.form.get("how_many", group.how_many)
    db.session.commit()
    return redirect(url_for("groups.list_group"))