from typing import TypeVar, Generic, List, Optional

# Define generic types
T = TypeVar('T')  # Entity type (like Employee, TimeEntry, etc.)
ID = TypeVar('ID')  # ID type (usually str or int)

class Repository(Generic[T, ID]):
    def save(self, entity: T) -> None:
        """Save a new entity or update an existing one."""
        raise NotImplementedError

    def find_by_id(self, id: ID) -> Optional[T]:
        """Find an entity by its ID."""
        raise NotImplementedError

    def find_all(self) -> List[T]:
        """Retrieve all entities."""
        raise NotImplementedError

    def delete(self, id: ID) -> None:
        """Delete an entity by its ID."""
        raise NotImplementedError
