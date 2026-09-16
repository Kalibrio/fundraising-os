#!/usr/bin/env python3
"""Install project-local Fundraising OS skills using only the Python standard library."""

import argparse
from datetime import datetime, timezone
from pathlib import Path
import shutil
import tempfile

SOURCE = Path(__file__).resolve().parents[1] / "skills"
APP_DIRS = {"codex": ".agents", "claude": ".claude"}


def files(folder):
    return {p.relative_to(folder): p.read_bytes() for p in folder.rglob("*") if p.is_file()}


def install(project, app, replace=False):
    project = Path(project).expanduser().resolve()
    skills = sorted(p.parent for p in SOURCE.glob("*/SKILL.md"))
    if len(skills) != 13:
        raise ValueError(f"Expected 13 source skills; found {len(skills)}. Download the complete repository.")
    if not (SOURCE / "raise-context/references/raise-context-template.md").is_file():
        raise ValueError("The raise-context template is missing. Download the complete repository.")
    apps = APP_DIRS if app == "both" else [app]
    changes = []
    # Check every destination before copying, including when installing into both apps.
    for target_app in apps:
        root = project / APP_DIRS[target_app] / "skills"
        if root.is_symlink() or not root.resolve().is_relative_to(project):
            raise ValueError(f"Skill directory must be inside the project: {root}")
        for skill in skills:
            dest = root / skill.name
            if dest.is_symlink() or (dest.exists() and not dest.is_dir()):
                raise ValueError(f"Refusing to replace a symlink or file: {dest}")
            if dest.exists():
                if any(p.is_symlink() for p in dest.rglob("*")):
                    raise ValueError(f"Refusing to replace a skill containing symlinks: {dest}")
                if files(dest) == files(skill):
                    continue
                if not replace:
                    raise ValueError(f"Existing skill differs: {dest}. Use --replace to back it up and install this version.")
            changes.append((target_app, skill, dest))

    project.mkdir(parents=True, exist_ok=True)
    backup = None
    for target_app, skill, dest in changes:
        dest.parent.mkdir(parents=True, exist_ok=True)
        # Stage a complete skill before changing an existing installation.
        with tempfile.TemporaryDirectory(prefix=".fundraising-install-", dir=dest.parent) as temp:
            staged = Path(temp) / skill.name
            shutil.copytree(skill, staged)
            old = None
            if dest.exists():
                if backup is None:
                    backup_root = project / ".fundraising-os-backups"
                    if backup_root.is_symlink():
                        raise ValueError(f"Backup directory must not be a symlink: {backup_root}")
                    backup_root.mkdir(exist_ok=True)
                    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ-")
                    backup = Path(tempfile.mkdtemp(prefix=stamp, dir=backup_root))
                old = backup / target_app / skill.name
                old.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(dest), str(old))
            try:
                staged.rename(dest)
            except Exception:
                if old is not None and not dest.exists():
                    shutil.move(str(old), str(dest))
                raise
    print(f"Ready: 13 skills for {app} in {project} ({len(changes)} folders installed/updated).")
    if backup:
        print(f"Previous versions saved in {backup}")
    print("Open this project in a new session. Codex: $raise-decision. Standalone Claude skills: /raise-decision.")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--app", required=True, choices=[*APP_DIRS, "both"])
    parser.add_argument("--project", required=True, help="Folder containing your raise files")
    parser.add_argument("--replace", action="store_true", help="Back up conflicting skill folders before updating")
    args = parser.parse_args()
    try:
        install(args.project, args.app, args.replace)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Installation failed: {error}\n")


if __name__ == "__main__":
    main()
