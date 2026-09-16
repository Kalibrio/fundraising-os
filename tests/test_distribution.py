"""Distribution checks: metadata, complete copies, and preserving existing work."""

import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class DistributionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.project = Path(self.temp.name) / "raise with spaces"

    def test_all_skills_have_portable_metadata(self):
        skills = list((ROOT / "skills").glob("*/SKILL.md"))
        self.assertEqual(len(skills), 13)
        for path in skills:
            with self.subTest(skill=path.parent.name):
                _, frontmatter, body = path.read_text(encoding="utf-8").split("---", 2)
                data = yaml.safe_load(frontmatter)
                self.assertEqual(data["name"], path.parent.name)
                self.assertIsInstance(data["description"], str)
                self.assertTrue(data["description"].strip())
                self.assertLessEqual(len(data["description"]), 1024)
                self.assertTrue(body.strip())

    def test_manifests_share_the_same_version_and_skill_source(self):
        claude = json.loads((ROOT / ".claude-plugin/plugin.json").read_text(encoding="utf-8"))
        codex = json.loads((ROOT / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
        for key in ("name", "version", "skills"):
            self.assertEqual(claude[key], codex[key])
        self.assertEqual((ROOT / codex["skills"]).resolve(), ROOT / "skills")
        marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text(encoding="utf-8"))
        entry = marketplace["plugins"][0]
        self.assertEqual(entry["name"], claude["name"])
        self.assertEqual((ROOT / entry["source"]).resolve(), ROOT)

    def test_both_apps_get_complete_skills_and_shared_artifacts_survive(self):
        self.project.mkdir()
        artifact = self.project / "raise-context.md"
        artifact.write_text("Existing private company context")
        installer.install(self.project, "both")
        for app in (".agents", ".claude"):
            self.assertEqual(installer.files(ROOT / "skills"), installer.files(self.project / app / "skills"))
        self.assertEqual(artifact.read_text(encoding="utf-8"), "Existing private company context")

    def test_repeated_install_is_idempotent(self):
        installer.install(self.project, "codex")
        before = installer.files(self.project)
        installer.install(self.project, "codex")
        self.assertEqual(installer.files(self.project), before)
        self.assertFalse((self.project / ".fundraising-os-backups").exists())

    def test_conflict_aborts_both_apps_before_any_copy(self):
        dest = self.project / ".claude/skills/raise-context"
        dest.mkdir(parents=True)
        (dest / "SKILL.md").write_text("My custom skill")
        with self.assertRaisesRegex(ValueError, "Existing skill differs"):
            installer.install(self.project, "both")
        self.assertFalse((self.project / ".agents").exists())
        self.assertEqual((dest / "SKILL.md").read_text(encoding="utf-8"), "My custom skill")

    def test_replacement_backs_up_customizations_and_preserves_unrelated_skills(self):
        installer.install(self.project, "codex")
        dest = self.project / ".agents/skills/raise-context"
        (dest / "SKILL.md").write_text("Custom context skill")
        (dest / "my-reference.md").write_text("Custom reference")
        other = self.project / ".agents/skills/my-unrelated-skill"
        other.mkdir()
        (other / "SKILL.md").write_text("Unrelated skill")
        installer.install(self.project, "codex", replace=True)
        self.assertEqual(installer.files(dest), installer.files(ROOT / "skills/raise-context"))
        backup = next((self.project / ".fundraising-os-backups").glob("*/codex/raise-context"))
        self.assertEqual((backup / "SKILL.md").read_text(encoding="utf-8"), "Custom context skill")
        self.assertEqual((backup / "my-reference.md").read_text(encoding="utf-8"), "Custom reference")
        self.assertEqual((other / "SKILL.md").read_text(encoding="utf-8"), "Unrelated skill")

    def test_symlink_destination_is_not_followed(self):
        external = Path(self.temp.name) / "external"
        external.mkdir()
        (self.project / ".agents/skills").mkdir(parents=True)
        (self.project / ".agents/skills/closing").symlink_to(external, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "symlink"):
            installer.install(self.project, "codex", replace=True)
        self.assertEqual(list(external.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
