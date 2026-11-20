"""Limits are Unicode characters; long questionnaire content has an explicit exception."""
import importlib.util
import json
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("doc_policy", ROOT / "scripts/validate_documentation.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class DocumentationTests(unittest.TestCase):
    def test_current_documents_within_limits(self):
        self.assertEqual([], module.check_documentation(ROOT))

    def test_questionnaire_limit_is_explicit(self):
        policy = json.loads((ROOT / "config/documentation-policy.json").read_text())
        self.assertEqual(10000, policy["exact_limits"]["pages/questionnaire-pl.md"])
        self.assertEqual(6000, policy["glob_limits"]["pages/**/*.md"])

    def test_too_long_new_page_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "site", "__pycache__"))
            (root / "pages/other.md").write_text("x" * 6001)
            self.assertTrue(any("DOC LENGTH EXCEEDED: pages/other.md" in x
                                for x in module.check_documentation(root)))

    def test_invalid_policy_path_is_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "repo"
            shutil.copytree(ROOT, root, ignore=shutil.ignore_patterns(".git", "site", "__pycache__"))
            cfg = root / "config/documentation-policy.json"
            value = json.loads(cfg.read_text())
            value["exact_limits"]["../escape.md"] = 500
            cfg.write_text(json.dumps(value))
            self.assertTrue(any("invalid limit or path" in x
                                for x in module.check_documentation(root)))


if __name__ == "__main__":
    unittest.main()
