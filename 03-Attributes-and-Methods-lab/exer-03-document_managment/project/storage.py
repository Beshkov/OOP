from project.category import  Category
from project.topic import Topic
from project.document import Document

class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_topic(self, topic_id, new_topic, new_storage_folder):
        for topic in self.topics:
            if topic.id == topic_id:
                topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id, new_file_name):
        document = [doc for doc in self.documents if doc.id == document_id][0]
        document.edit(new_file_name)

    def edit_category(self, category_id, new_name):
        category = [category for category in self.categories if category.id == category_id][0]
        category.edit(new_name)


    def delete_category(self, category_id):
        self.categories.remove(*[cat for cat in self.categories if cat.id == category_id])
        # del [cat for cat in self.categories if cat.id == category_id][0]

    def delete_topic(self, topic_id):
        self.topics.remove(*[topic for topic in self.topics if topic.id == topic_id])

    def delete_document(self, document_id):
        self.documents.remove(*[document for document in self.documents if document.id == document_id])

    def get_document(self, document_id):
        for document in self.documents:
            if document.id == document_id:
                return str(document)


    def __repr__(self):
        return "\n".join([self.get_document(doc.id) for doc in self.documents])

