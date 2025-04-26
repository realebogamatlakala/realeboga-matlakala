# Repository Layer and Factory Design

## 🧩 Repository Pattern

We implemented a **generic `Repository<T, ID>` interface** to define standard CRUD operations:
- `save(entity)`
- `find_by_id(id)`
- `find_all()`
- `delete(id)`

Each domain entity (Employee, TimeEntry, Schedule) has its own specific repository interface.

## 🛠 In-Memory Implementation

We created **in-memory repositories** that use Python dictionaries for storage:
- `InMemoryEmployeeRepository`
- `InMemoryTimeEntryRepository`
- `InMemoryScheduleRepository`

This allows fast testing and removes the need for a database initially.

## 🔧 Factory Pattern for Storage Abstraction

A **RepositoryFactory** was created to abstract how repositories are obtained.
Example:

```python
repo = RepositoryFactory.get_employee_repository()
