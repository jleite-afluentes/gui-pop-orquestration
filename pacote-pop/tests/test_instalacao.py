import os
from pathlib import Path
import subprocess
import tempfile
import unittest

PACKAGE = Path(__file__).resolve().parents[1]
INSTALLER = PACKAGE / 'instalar.sh'

class TestInstalacao(unittest.TestCase):
    def test_instala_e_preserva_existente(self):
        with tempfile.TemporaryDirectory(prefix='gui install ') as temp:
            root = Path(temp)
            existing = root / 'skills' / 'pd-methods'
            existing.mkdir(parents=True)
            marker = existing / 'SKILL.md'
            marker.write_text('versão já existente', encoding='utf-8')
            env = dict(os.environ, CODEX_HOME=str(root))
            result = subprocess.run(['sh', str(INSTALLER)], env=env, capture_output=True, text=True)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(marker.read_text(encoding='utf-8'), 'versão já existente')
            self.assertIn('versão não verificada', result.stdout)
            expected = {p.name for p in (PACKAGE / 'skills').iterdir() if p.is_dir()}
            installed = {p.name for p in (root / 'skills').iterdir() if p.is_dir()}
            self.assertEqual(expected, installed)
            self.assertTrue(all((root / 'skills' / name / 'SKILL.md').is_file() for name in expected))
            repeat = subprocess.run(['sh', str(INSTALLER)], env=env, capture_output=True, text=True)
            self.assertEqual(repeat.returncode, 0, repeat.stderr)
            self.assertEqual(marker.read_text(encoding='utf-8'), 'versão já existente')

if __name__ == '__main__':
    unittest.main()
