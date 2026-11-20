"""Negative and baseline tests for public-vs-internal document isolation."""
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("check_public", ROOT / "scripts/validate_pages.py")
check = importlib.util.module_from_spec(spec)
spec.loader.exec_module(check)


class PublicPagesTests(unittest.TestCase):
    def fixture(self, tmp):
        dest = Path(tmp) / "repo"
        dest.mkdir()
        for name in ("pages", "config"):
            shutil.copytree(ROOT / name, dest / name)
        shutil.copy2(ROOT / "mkdocs.yml", dest / "mkdocs.yml")
        return dest

    def test_baseline(self):
        self.assertEqual([], check.check_pages(ROOT))

    def test_unapproved_page(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            (root / "pages/internal.md").write_text("x")
            self.assertIn("PAGES UNAPPROVED FILE: internal.md", check.check_pages(root))

    def test_agent_instruction(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            (root / "pages/index.md").write_text("Dla agenta: popraw repo")
            self.assertIn("PAGES AGENT OR EDITORIAL CONTENT: index.md", check.check_pages(root))

    def test_editor_note(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            (root / "pages/index.md").write_text("Uwagi redakcyjne: aktualizuj źródła")
            self.assertIn("PAGES AGENT OR EDITORIAL CONTENT: index.md", check.check_pages(root))

    def test_symlink(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            (root / "pages/internal.md").symlink_to(root / "mkdocs.yml")
            self.assertIn("PAGES SYMLINK: internal.md", check.check_pages(root))

    def test_docs_dir_not_public(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            config = root / "mkdocs.yml"
            config.write_text(config.read_text().replace("docs_dir: pages", "docs_dir: docs"))
            self.assertIn("PAGES CONFIG: docs_dir must equal pages exactly",
                          check.check_pages(root))

    def test_reject_private_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            p = root / "config/pages-policy.json"
            obj = json.loads(p.read_text())
            obj["public_files"].append("../docs/development/agent-workflow.md")
            p.write_text(json.dumps(obj))
            self.assertIn("PAGES POLICY: invalid public_files", check.check_pages(root))

    def test_generated_agent_page(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = self.fixture(tmp)
            site = root / "site"
            (site / "development").mkdir(parents=True)
            (site / "development/index.html").write_text("Procedura autonomicznych agentów")
            self.assertTrue(any("PAGES BUILD" in x for x in check.check_pages(root, Path("site"))))


if __name__ == "__main__":
    unittest.main()
