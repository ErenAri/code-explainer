from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Kod odaklı küçük model
model_id = "Salesforce/codegen-350M-multi"

print("Model yükleniyor...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Kod alımı
print("\nDönüştürmek istediğiniz Python kodunu girin (bitirmek için boş satır bırakın):\n")
user_code = ""
while True:
    line = input()
    if line.strip() == "":
        break
    user_code += line + "\n"

# Prompt
prompt = f"""# Convert Python code to JavaScript

# Python code:
{user_code}

# JavaScript code:"""


# Üretim
print("\nJavaScript kodu üretiliyor...\n")
result = generator(prompt, max_new_tokens=200)[0]["generated_text"]
print(result)
