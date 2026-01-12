import json
import os
import math

def main():
    with open('missing_translations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Prepare output directory
    output_dir = 'missing_content_chunks'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Configuration
    # Target size roughly 20-30 files per chunk or by character count?
    # Let's simple split by number of files (top level keys)
    keys = list(data.keys())
    total_files = len(keys)
    # Estimate total size
    
    # We want chunks that fit into context easily. 
    # 5 files per chunk seems safe given 37 files.
    chunk_size = 5 
    
    num_chunks = math.ceil(total_files / chunk_size)
    
    for i in range(num_chunks):
        chunk_keys = keys[i*chunk_size : (i+1)*chunk_size]
        chunk_data = {k: data[k] for k in chunk_keys}
        
        output_filename = os.path.join(output_dir, f'chunk_{i}.json')
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(chunk_data, f, indent=4, ensure_ascii=False)
            
    print(f"Split {total_files} files into {num_chunks} chunks in '{output_dir}'.")

if __name__ == "__main__":
    main()
