import sys
import unittest
import os
from operator import itemgetter


class TestArtifacts(unittest.TestCase):
    def test_contains_app_artifacts(self):
        app_artifact_paths = [
            "api/app/config/config.yml",
            "api/app/models/logistic_regression.pkl",
            "api/app/utils/io_utils.py",
            "api/app/utils/model_utils.py",
            "api/app/Dockerfile",
            "api/app/main.py",
            "api/app/requirements.txt"
        ]

        existing_paths = [not os.path.exists(path) for path in app_artifact_paths]
        ids = [i for i, x in enumerate(existing_paths) if x]
        if len(ids) > 0:
            result = f"Faltam os arquivos: {itemgetter(*ids)(app_artifact_paths)}"
        else:
            result = "Possui todos os artefatos"
        self.assertEqual(len(ids), 0, result)
    
    def test_contains_frontend_artifacts(self):
        frontend_artifact_paths = [
            "api/frontend/config/config.yml",
            "api/frontend/utils/io_utils.py",
            "api/frontend/Dockerfile",
            "api/frontend/frontend.py",
            "api/frontend/requirements.txt"
        ]

        existing_paths = [not os.path.exists(path) for path in frontend_artifact_paths]
        ids = [i for i, x in enumerate(existing_paths) if x]
        if len(ids) > 0:
            result = f"Faltam os arquivos: {itemgetter(*ids)(frontend_artifact_paths)}"
        else:
            result = "Possui todos os artefatos"
        self.assertEqual(len(ids), 0, result)

if __name__ == '__main__':
    unittest.main()