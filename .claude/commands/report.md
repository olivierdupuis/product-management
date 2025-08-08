# Report Command

This command generates reports on initiatives, projects, and tasks from the `initiatives.yaml` file.

## Usage

The user can request reports with different scopes:

- **Full report**: "Run the report command" or "Show me all initiatives, projects, and tasks"
- **Initiative-specific**: "Run the report command for initiative [initiative-id]" or "Show me initiative [initiative-id]"
- **Project-specific**: "Run the report command for project [project-id]" or "Show me project [project-id]"
- **Task-specific**: "Run the report command for task [task-id]" or "Show me task [task-id]"

## Instructions for Claude

When this command is invoked:

1. **Generate the report** using Python utilities:
   ```bash
   python -c "
   from utils.yaml_handler import load_initiatives
   from utils.formatters import format_full_report
   data = load_initiatives()
   report = format_full_report(data)
   with open('initiatives.md', 'w') as f:
       f.write(report)
   print('Report generated: initiatives.md')
   "
   ```
2. **Parse the user's request** to determine the scope:
   - Extract any initiative-id, project-id, or task-id mentioned
   - Default to full report if no specific ID is provided
3. **Generate the appropriate report** based on scope:

### Full Report
- Show legend with all status icons
- Show summary counts (total initiatives, projects, tasks by status)
- **## Active Initiatives** section with nested tree structure
- **## Planned Initiatives** section with nested tree structure
- Exclude completed and backlog initiatives from main report
- Tree format: Initiative → Projects → Tasks with proper nesting

### Initiative Report
- Show initiative details (name, description, status, dates)
- List all projects under this initiative with status
- Show task counts per project
- Include Linear integration status if available

### Project Report
- Show project details (name, description, status, dates)
- Show parent initiative context
- List all tasks with status, priority, and progress
- Include Linear project/issue sync status

### Task Report
- Show complete task details including:
  - Name, description, status, priority
  - Parent project and initiative context
  - User story, acceptance criteria, deliverables
  - Technical specifications
  - Time estimates vs actual
  - Linear issue integration status

## Output Formatting

- **Legend section** with all status icons (📦 Backlog, 🚀 Staging, 📝 Todo, 🔄 In Progress, etc.)
- **No status icons on initiative headers** - clean initiative names only
- **Status icons on projects and tasks** for clear progress visibility
- **Nested tree format** - Projects indented under initiatives, tasks under projects
- **No priority information** - focus on status and task names only
- Show creation and update dates for initiatives
- **Exclude completed initiatives** from main report output

## Error Handling

- If the initiatives.yaml file doesn't exist, inform the user and offer to create it
- If a requested ID doesn't exist, list available IDs of that type
- If the YAML is malformed, report the parsing error and suggest fixes

## Examples

### Full Report Output Format:
```
# Product Management Report - Full

## Legend
**Status Icons:**
- 🟢 Active | 🟡 Planning | 📝 Todo | 🔄 In Progress | 📦 Backlog | 🚀 Staging | ✅ Completed

## Summary
- 🏢 Initiatives: 5 active, 2 planning, 2 backlog
- 📋 Projects: 6 active, 5 planning
- ✅ Tasks: 13 backlog, 3 todo, 1 in_progress, 1 staging, 4 completed

## Active Initiatives

### Barkbox engagement
- Client engagement and analytics work for Barkbox
- Target: 2025-10-31
- **Projects:** None

### Foundational Ecosystem  
- Complete foundations for Wire, Pulse, and Automations products
- Target: 2025-09-30
- **Projects (5):**
  - 🟢 **Wire Framework Core** (3 tasks)
    - 📦 Wire CLI
    - 📦 First set of agents
    - ✅ Wire 0.1 Vision
  - 🟢 **Automations Platform** (5 tasks)
    - 🔄 Productionize Forge
    - ✅ Fathom calls to Obsidian workflow

## Planned Initiatives

### Rittman Analytics - 2025Q4 Engagement
- Q4 2025 engagement work for Rittman Analytics  
- Target: 2025-12-31
- **Projects:** None
```

### Project Report Output Format:
```
# Project Report: data-ingestion-api

**Data Ingestion API** (🟡 planning)
- Initiative: republic-platform - RepublicOfData.io Platform Development  
- Description: RESTful API for data ingestion workflows
- Linear Project: Not synced
- Created: 2025-07-31 | Updated: 2025-07-31

## Tasks (3 total)
| Task | Status | Priority | Linear |
|------|--------|----------|--------|
| design-api-schema | 📝 todo | high | ❌ |
| implement-endpoints | 📝 todo | medium | ❌ |
```

## Dependencies

This command relies on:
- `initiatives.yaml` file in project root
- Python YAML parsing (use claude/utils functions when available)
- Access to Linear MCP for sync status checks when relevant