html_text = """
<h1>Technology</h1>
<p>Technology is evolving rapidly.</p>

<h2>Artificial Intelligence</h2>
<p>AI powers modern applications.</p>

<h1>Health</h1>
<p>Health is wealth.</p>

<h2>Nutrition</h2>
<p>Balanced diet is important.</p>
"""


from langchain_text_splitters import HTMLHeaderTextSplitter

headers = [
    ("h1", "H1"),
    ("h2", "H2"),
]

splitter = HTMLHeaderTextSplitter(headers)

chunks = splitter.split_text(html_text)

for i, chunk in enumerate(chunks):
    print(f"\n--- Chunk {i+1} ---")
    print(chunk.page_content)
    print("Metadata:", chunk.metadata)
