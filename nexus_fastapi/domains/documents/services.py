from .models import Document
from .schemas import Document as DocumentsSchema
from sqlalchemy.orm import Session
from ...database import get_db

class DocumentsService:
    @staticmethod
    def create_documents(documents_data: DocumentsSchema):
        db: Session = get_db()
        documents = Document(**documents_data.dict())
        db.add(documents)
        db.commit()
        db.refresh(documents)
        return documents

    @staticmethod
    def get_documents(documents_id: int):
        db: Session = get_db()
        return db.query(Document).filter(Document.id == documents_id).first()

    @staticmethod
    def list_documents():
        db: Session = get_db()
        return db.query(Document).all()

    @staticmethod
    def update_documents(documents_id: int, documents_data: DocumentsSchema):
        db: Session = get_db()
        documents = db.query(Document).filter(Document.id == documents_id).first()
        if not documents:
            return None
        for key, value in documents_data.dict().items():
            setattr(documents, key, value)
        db.commit()
        db.refresh(documents)
        return documents

    @staticmethod
    def delete_documents(documents_id: int):
        db: Session = get_db()
        documents = db.query(Document).filter(Document.id == documents_id).first()
        if documents:
            db.delete(documents)
            db.commit()