import json
import os
import math

def main():
    chunk_path = 'missing_content_chunks/chunk_1.json'
    if not os.path.exists(chunk_path):
        print(f"Error: {chunk_path} not found.")
        return

    with open(chunk_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Flatten the data to list of (filename, key, value) tuples to split easier?
    # Or just split by top level files if possible?
    # gts_aom_l_english.yml is huge, so we might need to split WITHIN the file.
    
    # We will create a list of items to translate:
    # { "chunk_1_0.json": { "filename": { "key": ... } } }
    
    items = []
    for filename, file_data in data.items():
        for key, val_data in file_data.items():
            items.append((filename, key, val_data))
            
    # Target items per chunk. 2800 lines, maybe 300 lines per chunk? 
    # Each item is ~5-10 lines. So maybe 50 items per chunk.
    items_per_chunk = 50
    total_items = len(items)
    num_chunks = math.ceil(total_items / items_per_chunk)
    
    print(f"Total items: {total_items}, splitting into {num_chunks} chunks.")
    
    output_dir = 'missing_content_chunks/chunk_1_sub'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    for i in range(num_chunks):
        chunk_items = items[i*items_per_chunk : (i+1)*items_per_chunk]
        
        # Reconstruct dict structure
        chunk_data = {}
        for filename, key, val_data in chunk_items:
            if filename not in chunk_data:
                chunk_data[filename] = {}
            chunk_data[filename][key] = val_data
            
        output_filename = os.path.join(output_dir, f'chunk_1_{i}.json')
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(chunk_data, f, indent=4, ensure_ascii=False)
            
    print(f"Created {num_chunks} sub-chunks in {output_dir}")

if __name__ == "__main__":
    main()
