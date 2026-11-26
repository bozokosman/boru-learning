name = "  Osman Bozok  "

print(name)
print(name.strip())
print(name.upper())
print(name.lower())

print(name[0:5])
print(name[::-1])

text = "Python,Java,C++,Go"

languages = text.split(",")

print(languages)

new_text = " | ".join(languages)

print(new_text)

search = "Python"

if search in text:
    print(f"{search} bulundu.")
else:
    print(f"{search} bulunamadı.")

first_name = "Osman"
age = 32
city = "Podgorica"

print(f"Benim adım {first_name}. {age} yaşındayım ve {city} şehrinde yaşıyorum.")

sentence = "Python programlama dilini öğreniyorum."

for character in sentence:
    print(character)