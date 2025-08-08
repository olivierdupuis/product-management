"""
YAML handler utilities for managing initiatives.yaml file
"""
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from datetime import datetime


def get_initiatives_file_path() -> Path:
    """Get the path to the initiatives.yaml file"""
    return Path(__file__).parent.parent / "initiatives.yaml"


def load_initiatives() -> Dict[str, Any]:
    """
    Load initiatives data from YAML file
    
    Returns:
        Dict containing the full initiatives data structure
        
    Raises:
        FileNotFoundError: If initiatives.yaml doesn't exist
        yaml.YAMLError: If YAML is malformed
    """
    file_path = get_initiatives_file_path()
    
    if not file_path.exists():
        raise FileNotFoundError(f"initiatives.yaml not found at {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data or {}
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Failed to parse YAML: {e}")


def save_initiatives(data: Dict[str, Any]) -> None:
    """
    Save initiatives data to YAML file
    
    Args:
        data: The initiatives data structure to save
        
    Raises:
        yaml.YAMLError: If data cannot be serialized to YAML
    """
    file_path = get_initiatives_file_path()
    
    # Update metadata
    if 'metadata' not in data:
        data['metadata'] = {}
    data['metadata']['last_updated'] = datetime.now().strftime('%Y-%m-%d')
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            yaml.dump(data, f, default_flow_style=False, sort_keys=False, indent=2)
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Failed to save YAML: {e}")


def get_initiative(initiative_id: str) -> Optional[Dict[str, Any]]:
    """Get a specific initiative by ID"""
    data = load_initiatives()
    return data.get('initiatives', {}).get(initiative_id)


def get_project(project_id: str) -> Optional[Dict[str, Any]]:
    """Get a specific project by ID from nested structure"""
    data = load_initiatives()
    initiatives = data.get('initiatives', {})
    
    for initiative in initiatives.values():
        projects = initiative.get('projects', {})
        if project_id in projects:
            return projects[project_id]
    return None


def get_task(task_id: str) -> Optional[Dict[str, Any]]:
    """Get a specific task by ID from nested structure"""
    data = load_initiatives()
    initiatives = data.get('initiatives', {})
    
    for initiative in initiatives.values():
        projects = initiative.get('projects', {})
        for project in projects.values():
            tasks = project.get('tasks', {})
            if task_id in tasks:
                return tasks[task_id]
    return None


def get_projects_for_initiative(initiative_id: str) -> Dict[str, Any]:
    """Get all projects belonging to an initiative from nested structure"""
    data = load_initiatives()
    initiative = data.get('initiatives', {}).get(initiative_id)
    if initiative:
        return initiative.get('projects', {})
    return {}


def get_tasks_for_project(project_id: str) -> Dict[str, Any]:
    """Get all tasks belonging to a project from nested structure"""
    project = get_project(project_id)
    if project:
        return project.get('tasks', {})
    return {}


def validate_yaml_structure(data: Dict[str, Any]) -> list[str]:
    """
    Validate the structure of initiatives data
    
    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []
    
    # Check top-level structure
    required_keys = ['metadata', 'initiatives', 'projects', 'tasks']
    for key in required_keys:
        if key not in data:
            errors.append(f"Missing required top-level key: {key}")
    
    # Validate initiatives
    initiatives = data.get('initiatives', {})
    for init_id, initiative in initiatives.items():
        if 'id' not in initiative or initiative['id'] != init_id:
            errors.append(f"Initiative {init_id}: id field missing or mismatched")
        
        required_fields = ['name', 'status', 'created']
        for field in required_fields:
            if field not in initiative:
                errors.append(f"Initiative {init_id}: missing required field '{field}'")
    
    # Validate projects
    projects = data.get('projects', {})
    for proj_id, project in projects.items():
        if 'id' not in project or project['id'] != proj_id:
            errors.append(f"Project {proj_id}: id field missing or mismatched")
        
        if 'initiative_id' in project:
            if project['initiative_id'] not in initiatives:
                errors.append(f"Project {proj_id}: references non-existent initiative {project['initiative_id']}")
    
    # Validate tasks
    tasks = data.get('tasks', {})
    for task_id, task in tasks.items():
        if 'id' not in task or task['id'] != task_id:
            errors.append(f"Task {task_id}: id field missing or mismatched")
        
        if 'project_id' in task:
            if task['project_id'] not in projects:
                errors.append(f"Task {task_id}: references non-existent project {task['project_id']}")
    
    return errors