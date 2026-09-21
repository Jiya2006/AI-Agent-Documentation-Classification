from classifier import classify_document


test_text = """
JOHN DOE

Bachelor of Technology in Computer Science and Engineering

Technical Skills:
Python, Java, C++, Machine Learning, SQL

Education:
B.Tech Computer Science and Engineering
XYZ University

Projects:
AI Based Document Classification System
Machine Learning Diabetes Prediction

Experience:
Software Development Intern
"""


print("\n========== AI CLASSIFICATION ==========\n")

result = classify_document(test_text)

print(result)

print("\n=======================================\n")