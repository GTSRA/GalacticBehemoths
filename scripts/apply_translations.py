import json
import os
import shutil

def load_original_texts(base_dir):
    original_texts = {}
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if not file.endswith('.json'):
                continue
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                for filename, keys in data.items():
                    if filename not in original_texts:
                        original_texts[filename] = {}
                    for key, content in keys.items():
                        # Handle complex format: { original: "...", ... }
                        if isinstance(content, dict) and 'original' in content:
                            original_texts[filename][key] = content['original']
                        # Handle potential other formats or if original is just the value (unlikely)
            except Exception as e:
                print(f"Error reading originals from {filepath}: {e}")
    return original_texts

def main():
    translated_content_path = '/Users/Foo/repo/gtsra/translated_content.json'
    missing_chunks_dir = '/Users/Foo/repo/gtsra/missing_content_chunks'
    
    print(f"Loading translations from {translated_content_path}...")
    with open(translated_content_path, 'r', encoding='utf-8') as f:
        translations = json.load(f)
    
    print(f"Loading original texts from {missing_chunks_dir}...")
    original_texts = load_original_texts(missing_chunks_dir)
    
    english_dir = '/Users/Foo/repo/gtsra/localisation/english'
    
    applied_count = 0
    
    for filename, keys in translations.items():
        filepath = os.path.join(english_dir, filename)
        
        # Determine if file exists
        if not os.path.exists(filepath):
            print(f"Creating new file: {filepath}")
            with open(filepath, 'w', encoding='utf-8-sig') as f:
                f.write("l_english:\n")
        
        # Read existing content
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            content = f.read()
            lines = content.splitlines()

        # Simple check for existing keys to avoid duplicates
        # A improved way is to parse the file or check " key:" pattern.
        # But grep style check is okay for now.
        existing_keys = set()
        for line in lines:
            line = line.strip()
            if ':' in line:
                k = line.split(':')[0].strip()
                existing_keys.add(k)
        
        to_append = []
        for key, text in keys.items():
            if key in existing_keys:
                continue
            
            original = original_texts.get(filename, {}).get(key, "")
            # Clean original text for comment display
            # Replace newlines with space or \n literal.
            original_display = original.replace('\n', ' ').replace('\r', '') if original else ""
            
            if original_display:
                to_append.append(f' # Original: {original_display}')
            
            # Escape quotes in translation
            text_escaped = text.replace('"', '\\"').replace('\n', '\\n')
            to_append.append(f' {key}:0 "{text_escaped}"')
            applied_count += 1
        
        if to_append:
            with open(filepath, 'a', encoding='utf-8-sig') as f:
                if content and not content.endswith('\n'):
                    f.write('\n')
                f.write('\n'.join(to_append) + '\n')
            # print(f"Appended {len(to_append)} lines to {filename}")

    print(f"Applied {applied_count} translated keys across {len(translations)} files.")

if __name__ == "__main__":
    main()
