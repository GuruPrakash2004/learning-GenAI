qs = "how to study Gen AI";

def createPrompt(question):
    prompt = f"Answer the following question: {question}"
    return prompt;

result = createPrompt(qs);
print(result);