from document_processor import extract_text


file_path = "test_document.txt"

text = extract_text(file_path)

print("========== EXTRACTED TEXT ==========")
print(text)
print("====================================")