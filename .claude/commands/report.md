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

1. **Read the initiatives.yaml file** from the project root
2. **Parse the user's request** to determine the scope:
   - Extract any initiative-id, project-id, or task-id mentioned
   - Default to full report if no specific ID is provided
3. **Generate the appropriate report** based on scope:

### Full Report
- Show summary counts (total initiatives, projects, tasks)
- List all initiatives with their status
- For each initiative, show projects and their status
- Highlight any blocked or overdue items

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

- Use clear headers and sections
- Include status indicators (🟢 active, 🟡 on-hold, ✅ completed, ❌ blocked, etc.)
- Show creation and update dates
- Highlight missing or incomplete information
- Use tables for structured data when appropriate

## Error Handling

- If the initiatives.yaml file doesn't exist, inform the user and offer to create it
- If a requested ID doesn't exist, list available IDs of that type
- If the YAML is malformed, report the parsing error and suggest fixes

## Examples

### Full Report Output Format:
```
# Product Management Report - Full

## Summary
- 🏢 Initiatives: 2 active, 0 completed
- 📋 Projects: 4 active, 1 completed  
- ✅ Tasks: 12 todo, 8 in_progress, 15 completed

## Initiatives
### republic-platform (🟢 active)
- **RepublicOfData.io Platform Development**
- Projects: data-ingestion-api (🟡 planning), analytics-dashboard (🟢 active)
- Created: 2025-07-31 | Updated: 2025-07-31
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