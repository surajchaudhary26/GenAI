markdown_text = """
# Artificial Intelligence

AI is transforming industries and daily life.

## Machine Learning

Machine learning allows systems to learn from data.

## Deep Learning

Deep learning uses neural networks to model complex patterns.

# Sports

Sports bring people together.

## Cricket

Cricket is widely followed in India.
"""


from langchain_text_splitters import MarkdownHeaderTextSplitter

headers = [
    ("#", "H1"),
    ("##", "H2"),
]

splitter = MarkdownHeaderTextSplitter(headers)

chunks = splitter.split_text(markdown_text)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk.page_content)
    print("Metadata:", chunk.metadata)
