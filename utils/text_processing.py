import nltk
nltk.download('punkt',quet=True)
from nltk.tokenize import sent_tokenize

def split_text_into_chunks(text: str, method: str = 'sentence', chunk_size: int = 3, overlap: int = 1):
    """
    we split text into chunks
    by default it should tokenize text into sentence 
    and then groups them
    we should return a List[str] which is a list of text chunks.
    """

    if method == 'sentence':
        sentences = sent_tokenize(text)
        chunks = []
        start_idx = 0
        while start_idx < len(sentences):
            end_idx = start_idx + chunk_size
            chunk = ' '.join(sentences[start_idx:end_idx])
            chunks.append(chunk)
            start_idx += chunk_size - overlap
        return chunks
    else:
        # if method is not sentence we just split by newline
        return [p.strip() for p in text.split("\n") if p.strip()]