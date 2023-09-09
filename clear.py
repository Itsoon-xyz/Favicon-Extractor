text = open('text.txt').read()

lines = text.split('\n')

cleaned_lines = []
for line in lines:
    parts = line.split('|')
    if len(parts) >= 3:
        name = parts[1]
        link = parts[2]
        cleaned_lines.append(f'"{name}": "https://{link}",')

cleaned_text = '\n'.join(cleaned_lines)

print(cleaned_text)