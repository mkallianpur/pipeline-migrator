# 🛠️ Pipeline Migrator

A Python-based CLI tool that converts **Azure DevOps YAML pipelines** into equivalent **GitHub Actions workflows**.

---

## 🚀 Features

- 🌀 Converts `stages`, `jobs`, and `steps` from Azure DevOps to GitHub Actions
- ✅ Supports:
  - `script` steps → `run` in GitHub Actions
  - `task` steps → placeholder shell commands
- 🧪 Includes automated unit tests and GitHub Actions CI
- 📦 Lightweight and extensible

---

## 📁 Project Structure


pipeline-migrator/
├── pipeline_migrator/ # Core logic
│ ├── init.py
│ └── migrate.py
├── examples/
│ └── sample_azure_pipeline.yml # Sample input
├── tests/
│ └── test_migrate.py # Unit tests
├── pipeline_migrator.py # CLI runner
├── requirements.txt
├── .github/workflows/python-tests.yml
└── README.md
