
---

# 📄 2. `CHANGELOG.md` (Progress Log)


```markdown
# Changelog

## [Assignment 11] - Persistence Layer

### Added
- Created generic `Repository` interface.
- Implemented `EmployeeRepository`, `TimeEntryRepository`, and `ScheduleRepository`.
- Built in-memory repositories for each entity.
- Developed `RepositoryFactory` to abstract storage backend.
- Created stub for `DatabaseEmployeeRepository` (future database support).
- Wrote unit tests for in-memory repositories (Employee, TimeEntry, Schedule).

### Improvements
- Ensured Repository layer can easily switch storage types.
- Designed code for future database or filesystem integration.

### Testing
- All repositories tested with Python `unittest`.
- Coverage includes save, find, delete operations.
