from abc import ABC, abstractmethod

class StorageInterface(ABC):
    @abstractmethod
    def save(self, data: dict) -> None:
        """Saves data to the storage"""
        pass

    @abstractmethod
    def load(self, identifier: str) -> dict:
        """Loads data from the storage by identifier"""
        pass

    @abstractmethod
    def delete(self, identifier: str) -> None:
        """Deletes data from the storage by identifier"""
        pass


class LocalStorage(StorageInterface):
    def __init__(self, storage_file: str):
        self.storage_file = storage_file
        self._data = self._load_storage()

    def _load_storage(self) -> dict:
        try:
            with open(self.storage_file, 'r') as f:
                import json
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def save(self, data: dict) -> None:
        self._data.update(data)
        with open(self.storage_file, 'w') as f:
            import json
            json.dump(self._data, f)

    def load(self, identifier: str) -> dict:
        return self._data.get(identifier, {})

    def delete(self, identifier: str) -> None:
        if identifier in self._data:
            del self._data[identifier]
        self.save({})