import yaml

def load_azure_pipeline(path):
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def convert_to_github_actions(azure_pipeline):
    github_workflow = {
        'name': azure_pipeline.get('name', 'Migrated Azure Pipeline'),
        'on': {'push': {'branches': ['main']}},
        'jobs': {}
    }

    for idx, stage in enumerate(azure_pipeline.get('stages', [])):
        job_name = stage.get('stage', f'job_{idx}')
        github_workflow['jobs'][job_name] = {
            'runs-on': 'ubuntu-latest',
            'steps': []
        }

        for job in stage.get('jobs', []):
            for step in job.get('steps', []):
                if 'script' in step:
                    github_workflow['jobs'][job_name]['steps'].append({
                        'name': step.get('displayName', 'Run Script'),
                        'run': step['script']
                    })
                elif 'task' in step:
                    github_workflow['jobs'][job_name]['steps'].append({
                        'name': step.get('displayName', step['task']),
                        'run': f"echo Placeholder for task {step['task']}"
                    })

    return github_workflow

def save_github_workflow(github_workflow, output_path):
    with open(output_path, 'w') as f:
        yaml.dump(github_workflow, f, sort_keys=False)
