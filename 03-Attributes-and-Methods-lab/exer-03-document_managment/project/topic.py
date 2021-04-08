class Topic:
    def __init__(self, id, topic, storage_folder):
        self.id = id
        self.topic = topic
        self.storage_folder = storage_folder

    def edit(self, new_topic, new_storage):
        self.topic = new_topic
        self.storage_folder = new_storage

    def __repr__(self):
        return f"Topic {self.id}: {self.topic} in {self.storage_folder}"
