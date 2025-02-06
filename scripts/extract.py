import fitz
import json
from langchain.text_splitter import RecursiveCharacterTextSplitter

# Step 1: Extract Text from PDF
def extract_text_pymupdf(pdf_path):
    doc = fitz.open(pdf_path)
    pages = []
    for i, page in enumerate(doc):
        pages.append({"page": i + 1, "text": page.get_text("text")})
    return pages

# Step 2: Split Text into Chunks with Metadata
def split_text(pages, chunk_size=500, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    chunks = []
    for page in pages:
        split_chunks = text_splitter.split_text(page["text"])
        for i, chunk in enumerate(split_chunks):
            chunks.append({
                "chunk_id": f"{page['page']}_{i}",  # Unique ID (page_chunk_number)
                "page": page["page"],
                "text": chunk
            })
    return chunks

# Step 3: Save Processed Chunks
def save_data(chunks, txt_path="data/processed_text.txt", json_path="data/processed_data.json"):
    # Save as text file
    with open(txt_path, "w", encoding="utf-8") as f:
        for chunk in chunks:
            f.write(f"Chunk {chunk['chunk_id']} (Page {chunk['page']}):\n{chunk['text']}\n\n")

    # Save as JSON file
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    pdf_path = "data/test.pdf"
    
    # Extract and process
    raw_text_pages = extract_text_pymupdf(pdf_path)
    text_chunks = split_text(raw_text_pages)

    # Store the data
    save_data(text_chunks)

    print(f"Processing complete. Extracted {len(text_chunks)} chunks.")
