# pipeline_migrator.py
import argparse
from pipeline_migrator import load_azure_pipeline, convert_to_github_actions, save_github_workflow

def main():
    parser = argparse.ArgumentParser(
        description="Convert Azure DevOps YAML pipelines into GitHub Actions workflows"
    )
    parser.add_argument('--input', required=True, help='Path to Azure DevOps pipeline YAML')
    parser.add_argument('--output', required=True, help='Path to save GitHub Actions workflow YAML')

    args = parser.parse_args()

    azure_pipeline = load_azure_pipeline(args.input)
    github_workflow = convert_to_github_actions(azure_pipeline)
    save_github_workflow(github_workflow, args.output)

    print(f"✅ GitHub Actions workflow saved to: {args.output}")

if __name__ == "__main__":
    main()
