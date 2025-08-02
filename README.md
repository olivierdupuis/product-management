# Product Management System

A personal project planning system for data product development that bridges PKM (Personal Knowledge Management) with Linear execution.

## Purpose

Transform project ideas from PKM context into crisp Linear tickets with comprehensive requirements:

- **User stories** - Clear narrative of functionality from user perspective
- **Acceptance criteria** - Specific conditions that must be met
- **Deliverables** - Concrete outputs and artifacts
- **Technical specifications** - Implementation details and constraints

## Project Types

- **RepublicOfData.io business projects** - Building a data products business
- **Consulting projects** - Data product consulting work  
- **Product projects** - Actual data products as RepublicOfData.io assets

## Workflow

1. Extract project ideas from PKM notes (`/Users/olivierdupuis/dev/PKM`)
2. Apply data product domain context and expertise
3. Generate structured Linear tickets with detailed requirements
4. Execute projects through Linear with clear scope and deliverables

## Quick Start

```bash
# Run the application
python main.py

# Run tests
make test
# or
python -m pytest

# Start development with Neovim integration
make nvim  # Start Neovim with socket
make claude # Initialize Claude Code session
```

## Requirements

- Python 3.13+
- uv for dependency management
- Linear account for project execution
- PKM repository for context and ideas