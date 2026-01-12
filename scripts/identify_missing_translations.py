import os
import re
import json

# Configuration
LOCALISATION_DIR = "localisation"
CHINESE_DIR = os.path.join(LOCALISATION_DIR, "simp_chinese")
ENGLISH_DIR = os.path.join(LOCALISATION_DIR, "english")

# Regex to parse Paradox YAML lines
# Matches:  key:0 "value"  or  key: "value"
# Capture groups: 1=key, 2=value
KEY_VALUE_PATTERN = re.compile(r'^\s*([a-zA-Z0-9_\.\-]+)\s*:\d*\s*"(.*)"')

def parse_yaml_file(filepath):
    """
    Parses a Paradox YAML file and returns a dictionary of keys and their values/metadata.
    Returns: {key: {'val': text, 'original_line': line_content}}
    """
    data = {}
    if not os.path.exists(filepath):
        return data

    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except UnicodeDecodeError:
         # Fallback for weird encodings, though usually utf-8 or utf-8-sig
        with open(filepath, 'r', encoding='utf-8-sig') as f:
            lines = f.readlines()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return data
        
    for line in lines:
        # Strip comments manually if needed, but regex usually assumes start of line for key
        # Paradox files usually have comments on separate lines or after valid data, 
        # but the standard format is strictly one key per line.
        
        # Remove comments at end of line if any (basic heuristic)
        # Be careful not to remove # inside quotes. 
        # Paradox parser is simple: if line starts with #, it's a comment.
        stripped_line = line.strip()
        if not stripped_line or stripped_line.startswith('#'):
            continue
            
        match = KEY_VALUE_PATTERN.match(line)
        if match:
            key = match.group(1)
            value = match.group(2)
            data[key] = {
                'value': value,
                'original_line': line.strip()
            }
    return data

def main():
    missing_translations = {}
    
    # Ensure English directory exists
    if not os.path.exists(ENGLISH_DIR):
        os.makedirs(ENGLISH_DIR)

    # Walk through Chinese directory
    for root, dirs, files in os.walk(CHINESE_DIR):
        for filename in files:
            if not filename.endswith('.yml') and not filename.endswith('.yaml'):
                continue
            
            chinese_filepath = os.path.join(root, filename)
            
            # Determine relative path to maintain structure if needed, 
            # though usually strictly flat or mirrored structure in Paradox games.
            # Here we assume flat structure inside 'simp_chinese' mapping to 'english'
            # filename conversion: gts_aom_l_simp_chinese.yml -> gts_aom_l_english.yml
            
            if 'l_simp_chinese' in filename:
                english_filename = filename.replace('l_simp_chinese', 'l_english')
            else:
                # If naming doesn't follow standard convention, just skip or warn? 
                # Let's simple skip or try direct mapping if logical
                print(f"Skipping non-standard filename: {filename}")
                continue
                
            english_filepath = os.path.join(ENGLISH_DIR, english_filename)
            
            chinese_data = parse_yaml_file(chinese_filepath)
            english_data = parse_yaml_file(english_filepath)
            
            file_missing_keys = {}
            
            for key, data in chinese_data.items():
                if key not in english_data:
                    file_missing_keys[key] = {
                        "original": data['value'],
                        "original_line": data['original_line']
                    }
            
            if file_missing_keys:
                missing_translations[english_filename] = file_missing_keys

    # Output results
    with open('missing_translations.json', 'w', encoding='utf-8') as f:
        json.dump(missing_translations, f, indent=4, ensure_ascii=False)
        
    print(f"Comparison complete. Found missing keys in {len(missing_translations)} files.")
    print("Results saved to missing_translations.json")

if __name__ == "__main__":
    main()
