import json
import os

def main():
    translated_content_path = '/Users/Foo/repo/gtsra/translated_content.json'
    
    with open(translated_content_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Add gts_o_god_keeper_l_english.yml
    if 'gts_o_god_keeper_l_english.yml' not in data:
        data['gts_o_god_keeper_l_english.yml'] = {}
    
    data['gts_o_god_keeper_l_english.yml']['gts_god_keeper.99.f.response'] = "The maiden wearing the crown kneels on one knee, the rolling sun roars behind her, the thrown prominence seems to be cheering for her - of course, it may just be affected by the girl's too terrifying emotions.\\n\\n§POf course, Father... Majesty.§!"
    data['gts_o_god_keeper_l_english.yml']['gts_god_keeper.118.tile'] = "Forced Palace"

    # Add empty keys to silence verification (optional but good practice)
    files_with_empties = [
        "gts_i_xinuo_l_english.yml",
        "gts_aom_l_english.yml",
        "gts_ap_planet_l_english.yml",
        "gts_bruh_l_english.yml",
        "gts_civ_tiny115_l_english.yml",
        "gts_com_l_english.yml"
    ]
    
    missing_json_path = '/Users/Foo/repo/gtsra/missing_translations.json'
    with open(missing_json_path, 'r', encoding='utf-8') as f:
        missing_data = json.load(f)
        
    for filename in files_with_empties:
        if filename in missing_data:
            if filename not in data:
                data[filename] = {}
            for key, val_dict in missing_data[filename].items():
                if val_dict['original'] == "":
                    data[filename][key] = ""

    with open(translated_content_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print("Updated translated_content.json with remaining translations.")

if __name__ == "__main__":
    main()
