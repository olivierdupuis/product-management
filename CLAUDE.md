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

The system uses Python 3.13+ and follows a minimal setup approach with uv for dependency management.

## Development Commands

### Basic Operations
- `python main.py` - Run the main application
- `make test` or `python -m pytest` - Run all tests
- `python -m pytest [specific_test_file]` - Run specific test file
- `python -m pytest -k [test_name]` - Run specific test by name

### Development Environment
- `make nvim` - Start Neovim with socket listening on /tmp/nvim_product_management
- `make claude` - Initialize Claude Code session with Neovim integration

### Testing
- Tests are run using pytest
- Use `ARGS` variable with make: `make test ARGS="-v -k test_name"`

## Project Structure

This is currently a minimal Python project with:
- Single entry point in `main.py`
- uv-based dependency management via `pyproject.toml`
- Makefile for common development tasks
- Pytest for testing framework

**Workflow**: Extract project ideas from PKM notes → Apply data product context → Generate structured Linear tickets with comprehensive requirements.

## Linear Integration Notes

- **Initiatives**: Linear initiatives are the root organizational unit for all work, but Linear's MCP server does not support initiatives access
- **Project Hierarchy**: Initiatives contain projects, which contain tickets/issues
- **Workaround**: Initiative context must be maintained separately in this system and PKM notes

## Development Notes

- Project uses uv for Python package management
- Requires Python 3.13 or higher
- Neovim integration is preconfigured with socket-based communication
- No external dependencies currently defined in pyproject.toml

## Memory Context

- PKM (Personal Knowledge Management) repository is located at `/Users/olivierdupuis/dev/PKM` and should be used for rich context about ongoing work