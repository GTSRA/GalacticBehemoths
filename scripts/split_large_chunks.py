import json
import os
import math

def split_chunk(filename, items_per_chunk=50):
    filepath = os.path.join('missing_content_chunks', filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Flatten the structure to a list of (file, key, value) tuples
    items = []
    for yum_file, content in data.items():
        for key, value in content.items():
            items.append((yum_file, key, value))

    total_items = len(items)
    num_chunks = math.ceil(total_items / items_per_chunk)
    
    basename = os.path.splitext(filename)[0]
    output_dir = os.path.join('missing_content_chunks', f'{basename}_sub')
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Splitting {filename} ({total_items} items) into {num_chunks} files in {output_dir}...")

    for i in range(num_chunks):
        chunk_items = items[i*items_per_chunk : (i+1)*items_per_chunk]
        
        # Reconstruct the nested structure
        chunk_data = {}
        for yum_file, key, value in chunk_items:
            if yum_file not in chunk_data:
                chunk_data[yum_file] = {}
            chunk_data[yum_file][key] = value
            
        output_filename = os.path.join(output_dir, f'{basename}_{i}.json')
        with open(output_filename, 'w', encoding='utf-8') as f:
            json.dump(chunk_data, f, indent=4, ensure_ascii=False)
        print(f"Created {output_filename}")

def main():
    split_chunk('chunk_3.json')
    split_chunk('chunk_6.json')

if __name__ == "__main__":
    main()
