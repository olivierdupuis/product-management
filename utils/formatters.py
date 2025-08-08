"""
Output formatting utilities for generating reports
"""
from typing import Dict, Any, List
from datetime import datetime


def format_status_icon(status: str) -> str:
    """Convert status text to icon"""
    status_icons = {
        'active': '🟢',
        'planning': '🟡', 
        'on-hold': '⏸️',
        'completed': '✅',
        'cancelled': '❌',
        'blocked': '🚫',
        'todo': '📝',
        'in_progress': '🔄',
        'backlog': '📦',
        'staging': '🚀'
    }
    return status_icons.get(status.lower(), '❓')


def format_priority_icon(priority: str) -> str:
    """Convert priority to icon"""
    priority_icons = {
        'high': '🔴',
        'medium': '🟡', 
        'low': '🟢'
    }
    return priority_icons.get(priority.lower(), '⚪')


def format_date(date_str: str) -> str:
    """Format date string for display"""
    if not date_str:
        return "Not set"
    return date_str


def format_linear_status(linear_id: Any) -> str:
    """Format Linear integration status"""
    if linear_id:
        return f"✅ {linear_id}"
    return "❌"


def format_summary_counts(data: Dict[str, Any]) -> str:
    """Generate summary statistics from nested structure"""
    initiatives = data.get('initiatives', {})
    
    # Count by status
    init_counts = {}
    proj_counts = {}
    task_counts = {}
    
    for initiative in initiatives.values():
        status = initiative.get('status', 'unknown')
        init_counts[status] = init_counts.get(status, 0) + 1
        
        # Count projects within this initiative
        projects = initiative.get('projects', {})
        if isinstance(projects, dict):
            for project in projects.values():
                status = project.get('status', 'unknown')
                proj_counts[status] = proj_counts.get(status, 0) + 1
                
                # Count tasks within this project
                tasks = project.get('tasks', {})
                if isinstance(tasks, dict):
                    for task in tasks.values():
                        status = task.get('status', 'unknown')
                        task_counts[status] = task_counts.get(status, 0) + 1
    
    summary = "## Summary\n"
    
    # Initiatives
    init_parts = [f"{count} {status}" for status, count in init_counts.items()]
    summary += f"- 🏢 Initiatives: {', '.join(init_parts) if init_parts else '0'}\n"
    
    # Projects  
    proj_parts = [f"{count} {status}" for status, count in proj_counts.items()]
    summary += f"- 📋 Projects: {', '.join(proj_parts) if proj_parts else '0'}\n"
    
    # Tasks
    task_parts = [f"{count} {status}" for status, count in task_counts.items()]
    summary += f"- ✅ Tasks: {', '.join(task_parts) if task_parts else '0'}\n"
    
    return summary


def format_full_report(data: Dict[str, Any]) -> str:
    """Generate a full report of all initiatives, projects, and tasks using nested structure"""
    output = ["# Product Management Report - Full\n"]
    
    # Legend
    output.append("## Legend")
    output.append("")
    output.append("**Status Icons:**")
    output.append("- 🟢 Active | 🟡 Planning | ⏸️ On-Hold | ✅ Completed | ❌ Cancelled | 🚫 Blocked | 📝 Todo | 🔄 In Progress | 📦 Backlog | 🚀 Staging")
    output.append("")
    
    # Summary
    output.append(format_summary_counts(data))
    output.append("")
    
    initiatives = data.get('initiatives', {})
    
    if not initiatives:
        output.append("No initiatives found. Use the system to create your first initiative.")
        return "\n".join(output)
    
    # Group initiatives by status
    active_initiatives = {k: v for k, v in initiatives.items() if v.get('status') == 'active'}
    planning_initiatives = {k: v for k, v in initiatives.items() if v.get('status') == 'planning'}
    
    # Active Initiatives Section
    if active_initiatives:
        output.append("## Active Initiatives")
        output.append("")
        
        for init_id, initiative in active_initiatives.items():
            status_icon = format_status_icon(initiative.get('status', ''))
            name = initiative.get('name', 'Unnamed Initiative')
            description = initiative.get('description', '')
            target_date = format_date(initiative.get('target_date', ''))
            
            output.append(f"### {name}")
            if description:
                output.append(f"- {description}")
            output.append(f"- Target: {target_date}")
            
            # Get projects within this initiative
            projects = initiative.get('projects', {})
            if isinstance(projects, dict) and projects:
                output.append(f"- **Projects ({len(projects)}):**")
                for proj_id, project in projects.items():
                    proj_status_icon = format_status_icon(project.get('status', ''))
                    proj_name = project.get('name', 'Unnamed Project')
                    
                    # Count tasks in this project
                    tasks = project.get('tasks', {})
                    task_count = len(tasks) if isinstance(tasks, dict) else 0
                    
                    output.append(f"  - {proj_status_icon} **{proj_name}** ({task_count} tasks)")
                    
                    # Show tasks if any
                    if isinstance(tasks, dict) and tasks:
                        for task_id, task in tasks.items():
                            task_status_icon = format_status_icon(task.get('status', ''))
                            task_name = task.get('name', 'Unnamed Task')
                            output.append(f"    - {task_status_icon} {task_name}")
            else:
                output.append("- **Projects:** None")
            
            created = format_date(initiative.get('created', ''))
            updated = format_date(initiative.get('updated', ''))
            output.append(f"- Created: {created} | Updated: {updated}")
            output.append("")
    
    # Planning Initiatives Section
    if planning_initiatives:
        output.append("## Planned Initiatives")
        output.append("")
        
        for init_id, initiative in planning_initiatives.items():
            status_icon = format_status_icon(initiative.get('status', ''))
            name = initiative.get('name', 'Unnamed Initiative')
            description = initiative.get('description', '')
            target_date = format_date(initiative.get('target_date', ''))
            
            output.append(f"### {name}")
            if description:
                output.append(f"- {description}")
            output.append(f"- Target: {target_date}")
            
            # Get projects within this initiative
            projects = initiative.get('projects', {})
            if isinstance(projects, dict) and projects:
                output.append(f"- **Projects ({len(projects)}):**")
                for proj_id, project in projects.items():
                    proj_status_icon = format_status_icon(project.get('status', ''))
                    proj_name = project.get('name', 'Unnamed Project')
                    
                    # Count tasks in this project
                    tasks = project.get('tasks', {})
                    task_count = len(tasks) if isinstance(tasks, dict) else 0
                    
                    output.append(f"  - {proj_status_icon} **{proj_name}** ({task_count} tasks)")
                    
                    # Show tasks if any
                    if isinstance(tasks, dict) and tasks:
                        for task_id, task in tasks.items():
                            task_status_icon = format_status_icon(task.get('status', ''))
                            task_name = task.get('name', 'Unnamed Task')
                            output.append(f"    - {task_status_icon} {task_name}")
            else:
                output.append("- **Projects:** None")
            
            created = format_date(initiative.get('created', ''))
            updated = format_date(initiative.get('updated', ''))
            output.append(f"- Created: {created} | Updated: {updated}")
            output.append("")
    
    return "\n".join(output)


def format_initiative_report(initiative_id: str, data: Dict[str, Any]) -> str:
    """Generate a report for a specific initiative using nested structure"""
    initiative = data.get('initiatives', {}).get(initiative_id)
    if not initiative:
        return f"❌ Initiative '{initiative_id}' not found.\n\nAvailable initiatives: {', '.join(data.get('initiatives', {}).keys())}"
    
    output = [f"# Initiative Report: {initiative_id}\n"]
    
    status_icon = format_status_icon(initiative.get('status', ''))
    name = initiative.get('name', 'Unnamed Initiative')
    description = initiative.get('description', '')
    target_date = format_date(initiative.get('target_date', ''))
    
    output.append(f"**{name}** ({status_icon} {initiative.get('status', 'unknown')})")
    if description:
        output.append(f"- {description}")
    output.append(f"- Target: {target_date}")
    
    created = format_date(initiative.get('created', ''))
    updated = format_date(initiative.get('updated', ''))
    output.append(f"- Created: {created} | Updated: {updated}")
    output.append("")
    
    # Get projects from nested structure
    projects = initiative.get('projects', {})
    
    if projects:
        output.append(f"## Projects ({len(projects)} total)")
        output.append("| Project ID | Name | Status | Tasks | Linear |")
        output.append("|------------|------|--------|--------|--------|")
        
        for proj_id, project in projects.items():
            name = project.get('name', 'Unnamed')
            status_icon = format_status_icon(project.get('status', ''))
            status = project.get('status', 'unknown')
            
            # Count tasks in nested structure
            tasks = project.get('tasks', {})
            task_count = len(tasks)
            
            linear_status = format_linear_status(project.get('linear_project_id'))
            
            output.append(f"| {proj_id} | {name} | {status_icon} {status} | {task_count} | {linear_status} |")
    else:
        output.append("## Projects\nNo projects found for this initiative.")
    
    return "\n".join(output)


def format_project_report(project_id: str, data: Dict[str, Any]) -> str:
    """Generate a report for a specific project"""
    project = data.get('projects', {}).get(project_id)
    if not project:
        return f"❌ Project '{project_id}' not found.\n\nAvailable projects: {', '.join(data.get('projects', {}).keys())}"
    
    output = [f"# Project Report: {project_id}\n"]
    
    # Project details
    status_icon = format_status_icon(project.get('status', ''))
    name = project.get('name', 'Unnamed Project')
    description = project.get('description', '')
    
    output.append(f"**{name}** ({status_icon} {project.get('status', 'unknown')})")
    
    # Initiative context
    init_id = project.get('initiative_id')
    if init_id:
        initiative = data.get('initiatives', {}).get(init_id, {})
        init_name = initiative.get('name', 'Unknown Initiative')
        output.append(f"- Initiative: {init_id} - {init_name}")
    
    if description:
        output.append(f"- Description: {description}")
    
    linear_status = format_linear_status(project.get('linear_project_id'))
    output.append(f"- Linear Project: {linear_status}")
    
    created = format_date(project.get('created', ''))
    updated = format_date(project.get('updated', ''))
    output.append(f"- Created: {created} | Updated: {updated}")
    output.append("")
    
    # Tasks
    tasks = data.get('tasks', {})
    proj_tasks = {tid: t for tid, t in tasks.items() if t.get('project_id') == project_id}
    
    if proj_tasks:
        output.append(f"## Tasks ({len(proj_tasks)} total)")
        output.append("| Task ID | Name | Status | Priority | Linear |")
        output.append("|---------|------|--------|----------|--------|")
        
        for task_id, task in proj_tasks.items():
            name = task.get('name', 'Unnamed')
            status_icon = format_status_icon(task.get('status', ''))
            status = task.get('status', 'unknown')
            priority_icon = format_priority_icon(task.get('priority', ''))
            priority = task.get('priority', 'none')
            linear_status = format_linear_status(task.get('linear_issue_id'))
            
            output.append(f"| {task_id} | {name} | {status_icon} {status} | {priority_icon} {priority} | {linear_status} |")
    else:
        output.append("## Tasks\nNo tasks found for this project.")
    
    return "\n".join(output)


def format_task_report(task_id: str, data: Dict[str, Any]) -> str:
    """Generate a detailed report for a specific task"""
    task = data.get('tasks', {}).get(task_id)
    if not task:
        return f"❌ Task '{task_id}' not found.\n\nAvailable tasks: {', '.join(data.get('tasks', {}).keys())}"
    
    output = [f"# Task Report: {task_id}\n"]
    
    # Task details
    status_icon = format_status_icon(task.get('status', ''))
    priority_icon = format_priority_icon(task.get('priority', ''))
    name = task.get('name', 'Unnamed Task')
    description = task.get('description', '')
    
    output.append(f"**{name}** ({status_icon} {task.get('status', 'unknown')})")
    output.append(f"- Priority: {priority_icon} {task.get('priority', 'not set')}")
    
    # Context
    proj_id = task.get('project_id')
    if proj_id:
        project = data.get('projects', {}).get(proj_id, {})
        proj_name = project.get('name', 'Unknown Project')
        
        init_id = project.get('initiative_id')
        if init_id:
            initiative = data.get('initiatives', {}).get(init_id, {})
            init_name = initiative.get('name', 'Unknown Initiative')
            output.append(f"- Context: {init_id} → {proj_id} → {task_id}")
            output.append(f"- Initiative: {init_name}")
            output.append(f"- Project: {proj_name}")
        else:
            output.append(f"- Project: {proj_name}")
    
    if description:
        output.append(f"- Description: {description}")
    
    linear_status = format_linear_status(task.get('linear_issue_id'))
    output.append(f"- Linear Issue: {linear_status}")
    
    created = format_date(task.get('created', ''))
    updated = format_date(task.get('updated', ''))
    output.append(f"- Created: {created} | Updated: {updated}")
    
    # Estimates
    estimated = task.get('estimated_hours')
    actual = task.get('actual_hours')
    if estimated or actual:
        output.append(f"- Time: {estimated or 'Not estimated'} est. / {actual or 'Not tracked'} actual hours")
    
    output.append("")
    
    # User story
    user_story = task.get('user_story', '')
    if user_story:
        output.append("## User Story")
        output.append(user_story)
        output.append("")
    
    # Acceptance criteria
    criteria = task.get('acceptance_criteria', [])
    if criteria:
        output.append("## Acceptance Criteria")
        for i, criterion in enumerate(criteria, 1):
            output.append(f"{i}. {criterion}")
        output.append("")
    
    # Deliverables
    deliverables = task.get('deliverables', [])
    if deliverables:
        output.append("## Deliverables")
        for deliverable in deliverables:
            output.append(f"- {deliverable}")
        output.append("")
    
    # Technical specs
    tech_specs = task.get('technical_specs', [])
    if tech_specs:
        output.append("## Technical Specifications")
        for spec in tech_specs:
            output.append(f"- {spec}")
        output.append("")
    
    return "\n".join(output)