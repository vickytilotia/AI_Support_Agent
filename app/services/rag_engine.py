import os
import json
import fitz # PyMuPDF
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import uuid


DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')
FAQ_PATH = os.path.join(DATA_DIR, 'faqs.json')
PDF_DIR = os.path.join(DATA_DIR, 'kb_pdfs')


DB_PATH = os.getenv('CHROMA_DB_PATH', os.path.join(DATA_DIR, 'chroma_db'))


class RAGEngine:
    def __init__(self):
        self.embedder = SentenceTransformer('all-MiniLM-L6-v2')
        self.client = chromadb.Client(Settings( persist_directory=DB_PATH))
        self.collection = self.client.get_or_create_collection(name="knowledge_base")
    
    def load_faqs(self):
        """Load FAQs and add to vector DB."""
        with open(FAQ_PATH, 'r') as f:
            faqs = json.load(f)
        
        for faq in faqs:
            text = f"Q: {faq['question']}\nA: {faq['answer']}"
            embedding = self.embedder.encode(text).tolist()
            self.collection.add(ids=[str(uuid.uuid4())], documents=[text], embeddings=[embedding])
        print(f"✅ Loaded {len(faqs)} FAQs into ChromaDB")
    
    def load_pdfs(self):
        """Extract text from PDFs and add to vector DB."""
        for filename in os.listdir(PDF_DIR):
            if filename.endswith(".pdf"):
                pdf_path = os.path.join(PDF_DIR, filename)
                doc = fitz.open(pdf_path)
                text = ""
                for page in doc:
                    text += page.get_text()
                
                chunks = self.split_text(text)
                for chunk in chunks:
                    emb = self.embedder.encode(chunk).tolist()
                    self.collection.add(ids=[str(uuid.uuid4())], documents=[chunk], embeddings=[emb])
                print(f"✅ Processed {filename}, added {len(chunks)} chunks")

    def split_text(self, text, max_length=300):
        """Split text into smaller chunks for better embedding."""
        sentences = text.split('. ')
        chunks, current = [], ""
        for sentence in sentences:
            if len(current) + len(sentence) < max_length:
                current += sentence + '. '
            else:
                chunks.append(current.strip())
                current = sentence + '. '   
        if current:
            chunks.append(current.strip())
        return chunks

    def query(self,user_query, top_k=3):
        """Query the vector DB and return top_k relevant documents."""
        query_emb = self.embedder.encode(user_query).tolist()
        results = self.collection.query(query_embeddings=[query_emb], n_results=top_k)
        return results["documents"][0]
    

if __name__ == "__main__":
    engine = RAGEngine()
    engine.load_faqs()
    engine.load_pdfs()
    print("RAG Engine setup complete.")
