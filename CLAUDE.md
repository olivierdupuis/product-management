# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a personal project planning system for data product development. It bridges PKM (Personal Knowledge Management) notes with Linear execution by refining project/ticket ideas into detailed requirements.

**Core Purpose**: Transform project ideas from PKM context into crisp Linear tickets with:
- User stories
- Acceptance criteria
- Deliverables
- Technical specifications

**Project Types**:
- **RepublicOfData.io business projects**: Building a data products business
- **Consulting projects**: Data product consulting work
- **Product projects**: Actual data products as RepublicOfData.io assets

The system uses Python 3.13+ with uv for dependency management and YAML-based data storage.

## Development Commands

### Basic Operations
- `python -c "from utils.yaml_handler import YAMLHandler; print(YAMLHandler.load('initiatives.yaml'))"` - Load and display YAML data
- `python -c "from utils.formatters import format_summary; format_summary()"` - Generate formatted reports
- `make test` or `python -m pytest` - Run all tests (when implemented)

### Development Environment
- `make nvim` - Start Neovim with socket listening on /tmp/nvim_product_management
- `make claude` - Initialize Claude Code session with Neovim integration

### Testing
- Tests configured for pytest but not yet implemented
- Use `ARGS` variable with make: `make test ARGS="-v -k test_name"`

## Project Structure

**Current Architecture:**
```
├── initiatives.yaml       # Central data store (initiatives/projects/tasks)
├── initiatives.md          # Human-readable formatted reports
├── utils/                  # Python utilities package
│   ├── formatters.py       # Report generation and formatting
│   └── yaml_handler.py     # YAML data management and validation
├── pyproject.toml          # Python 3.13+ project with PyYAML dependency
└── Makefile                # Development environment commands
```

**Data Model**: YAML-based hierarchy with initiatives containing projects containing tasks, each with Linear integration fields (IDs, statuses, assignees).

**Workflow**: Extract project ideas from PKM notes → Apply data product context → Generate structured Linear tickets with comprehensive requirements.

## Current State

### ✅ Implemented Features
- YAML-based data management for initiatives/projects/tasks hierarchy
- Rich formatting utilities with status icons, priority indicators, and comprehensive reports
- Data validation and structural integrity checks
- Linear integration field tracking
- 8+ active consulting initiatives tracked

### ❌ Missing Features
- Test suite (pytest configured but no tests)
- CLI interface or main entry point
- Automated Linear synchronization
- Command-line report generation tools

### 📊 Active Data
- **Active Initiatives**: 8 consulting engagements (Barkbox, Consensus, Rittman Analytics, ListEdTech, etc.)
- **Status Distribution**: Mix of planning, active development, and review phases
- **Integration Ready**: All entries structured for Linear ticket creation

## Dependencies

- **PyYAML**: YAML file parsing and generation
- **Python 3.13+**: Core language requirement
- **uv**: Package management and virtual environment

## Linear Integration Notes

- **Initiatives**: Linear initiatives are the root organizational unit for all work, but Linear's MCP server does not support initiatives access
- **Project Hierarchy**: Initiatives contain projects, which contain tickets/issues
- **Workaround**: Initiative context must be maintained separately in this system and PKM notes
- **Field Mapping**: YAML structure includes linearId, assignee, and status fields for seamless ticket creation

## Memory Context

- PKM (Personal Knowledge Management) repository is located at `/Users/olivierdupuis/dev/PKM` and should be used for rich context about ongoing work
- Active consulting focus on data product strategy, analytics engineering, and AI/ML implementations