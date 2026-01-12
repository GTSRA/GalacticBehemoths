import json
import os

def main():
    translated_content = {}
    base_dir = '/Users/Foo/repo/gtsra/translated_content_chunks'

    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if not file.endswith('.json'):
                continue
            if file == 'translated_content.json':
                continue
            
            filepath = os.path.join(root, file)
            print(f"Processing {filepath}")
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    
                for filename, keys in data.items():
                    if filename not in translated_content:
                        translated_content[filename] = {}
                    
                    for key, content in keys.items():
                        translation = ""
                        if isinstance(content, str):
                            translation = content
                        elif isinstance(content, dict) and 'translated' in content:
                            translation = content['translated']
                        
                        if translation:
                            translated_content[filename][key] = translation
            except Exception as e:
                print(f"Error processing {filepath}: {e}")

    output_file = '/Users/Foo/repo/gtsra/translated_content.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(translated_content, f, indent=4, ensure_ascii=False)
    print(f"Merged translations saved to {output_file}")

if __name__ == "__main__":
    main()
