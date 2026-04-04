class StorageInterface:
    def save_analysis(self, data):
        pass  # Implement saving of analysis data

    def load_analysis(self, id):
        pass  # Implement loading of analysis data by id

    def load_index(self):
        pass  # Implement loading the index of analyses

    def delete_analysis(self, id):
        pass  # Implement deleting analysis data by id


class LocalStorage(StorageInterface):
    def __init__(self, storage_path):
        self.storage_path = storage_path

    def save_analysis(self, data):
        with open(f'{self.storage_path}/analysis.json', 'a') as file:
            json.dump(data, file)  # Save analysis to a file

    def load_analysis(self, id):
        with open(f'{self.storage_path}/analysis.json', 'r') as file:
            data = json.load(file)
            return data.get(id)  # Load specific analysis by id

    def load_index(self):
        index = []
        # Logic to generate on-disk index
        return index

    def delete_analysis(self, id):
        # Logic to delete analysis by id
        pass