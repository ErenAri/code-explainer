from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Küçük, CPU dostu model
model_id = "tiiuae/falcon-rw-1b"

print("Model yükleniyor...")
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer)

# Dil seçimi
language = input("Açıklama dili (tr/en): ").strip().lower()
if language not in ["tr", "en"]:
    print("Geçersiz seçim. 'tr' veya 'en' yazmalısınız.")
    exit()

# Kod alımı
print("\nAçıklanmasını istediğiniz Python kodunu girin (bitirmek için boş satır bırakın):\n")
user_code = ""
while True:
    line = input()
    if line.strip() == "":
        break
    user_code += line + "\n"

# Prompt oluşturma
if language == "tr":
    prompt = f"Aşağıdaki Python kodunu Türkçe olarak açıkla:\n{user_code}\nAçıklama:"
else:
    prompt = f"Explain the following Python code in English:\n{user_code}\nExplanation:"

# Model çıktısı
print("\nAçıklama oluşturuluyor...\n")
result = generator(prompt, max_new_tokens=150)[0]["generated_text"]
print(result)
