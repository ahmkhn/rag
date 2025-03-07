# utils/text_processing.py
import spacy

# Load SpaCy model
nlp = spacy.load("en_core_web_sm")

def split_text_into_chunks(text: str, method: str = 'sentence', chunk_size: int = 3, overlap: int = 1):
    """
    Split text into chunks using SpaCy for sentence segmentation.
    """
    if method == 'sentence':
        doc = nlp(text)
        sentences = [sent.text for sent in doc.sents]  # Extract sentences
        chunks = []
        start_idx = 0
        while start_idx < len(sentences):
            end_idx = start_idx + chunk_size
            chunk = ' '.join(sentences[start_idx:end_idx])
            chunks.append(chunk)
            start_idx += chunk_size - overlap
        return chunks
    else:
        return [p.strip() for p in text.split("\n") if p.strip()]
