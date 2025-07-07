import pytest
from pipeline_migrator import migrate

def test_convert_to_github_actions():
    azure_yaml = {
        "name": "Test Pipeline",
        "stages": [
            {
                "stage": "Build",
                "jobs": [
                    {
                        "job": "BuildJob",
                        "steps": [
                            {"script": "echo Hello", "displayName": "Hello World"}
                        ]
                    }
                ]
            }
        ]
    }
    github_yaml = migrate.convert_to_github_actions(azure_yaml)
    assert "jobs" in github_yaml
    assert "Build" in github_yaml["jobs"]
    assert github_yaml["jobs"]["Build"]["steps"][0]["run"] == "echo Hello"
