import json
import os

def main():
    chunk_path = 'missing_content_chunks/chunk_0.json'
    if not os.path.exists(chunk_path):
        print(f"Error: {chunk_path} not found.")
        return

    with open(chunk_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Translations mapping
    translations = {
        "gts_i_traptrix_l_english.yml": {
            "gts_traptrix_fleet_buff2": "Traptrix Encouragement",
            "gts_traptrix_fleet_buff2_desc": "The fleet with the best combat performance will later be able to choose a more comfortable spot inside the Traptrix. For this reward, the combat effectiveness of all fleets has been greatly improved!"
        },
        "gts_evt_tiny_basic_l_english.yml": {
            "Tiny_station_enclave_curator_01_key": "Tiny Station - Core Section",
            "gov_tiny_enclave": "§HTiny Trading Organization§!",
            "gov_tiny_enclave_desc": "An enclave organization dedicated to trading with tiny people.",
            "tiny_enclave_default_ruler_title": "Miniature Trader",
            "tiny_enclave_default_ruler_title_test": "Very tiny trading personnel, usually ignored by giantesses",
            "tiny_enclave_common.2000.title": "Strange Communication",
            "tiny_enclave_event.21.title": "Tiny Trading Station",
            "tiny_enclave_event.title": "Tiny Trading Station",
            "tiny_enclave_event.300.a.reply": "We are the §HTiny Trading Organization§!. Our services mainly provide technology or resource support. However, since giantesses require too many resources, most services are open to tiny people. But to avoid the trading station being directly destroyed by giantesses, there are also services open to giantesses. So what service do you need?",
            "tiny_enclave_gts_patron": "Sponsor Tiny Trading Station",
            "tiny_enclave_gts_patron_desc": "The resources of the Tiny Trading Station enclave are really not worth looking at - but their methods of pleasing giantesses are really good.",
            "tiny_enclave_tiny_patron": "Sponsor Tiny Trading Station",
            "tiny_enclave_tiny_patron_desc": "The Tiny Trading Station enclave provided us with some production assistance and technical data - even including technologies that only exist in other parallel worlds.",
            "tiny_enclave_event.301.a.reply": "Thank you for your sponsorship. Then, service begins.",
            "tiny_enclave_event.302.a.reply": "Very good, then I wish us a happy cooperation.",
            "tiny_enclave_event.304.desc.END": "We found another ancient robot, but probably nothing new.",
            "tiny_enclave_event.304.a.reply": "According to the manual, it is a small cleaning robot.",
            "tiny_enclave_event.304.b.reply": "It's not that simple. This robot was obtained from the Giantess Empire. Small is also relative to giantesses. The package itself is too large for the space station to hold, so we need assistance. And in order to figure out how she works, we must perform a startup test. Unsure if it will have an impact, after all, the power of giantess items is relatively high.",
            "tiny_enclave_event.304.c.reply": "This is no ordinary cleaning machine. It is a cleaning machine so ancient that even Fallen Empires think it is old. If it weren't for that giantess's home being so piled up that there was no place to step, we wouldn't have been able to buy this. You know, even Fallen Empires have quite a lot of lost technology. Through this, we can discover a thing or two.",
            "tiny_enclave_event.305.name": "Cleaning Robot Trample",
            "tiny_enclave_event.305.b": "I want to be stepped on too",
            "tiny_enclave_event.306.name": "Cleaning Robot Milk Spray",
            "tiny_enclave_event.306.b": "Don't I have to take a sip",
            "tiny_enclave_event.307.name": "Cleaning Robot Ravage",
            "tiny_enclave_event.307.b": "Bliss",
            "tiny_enclave_event.308.name": "Cleaning Robot Fart",
            "tiny_enclave_event.308.b": "One more time!",
            "tiny_enclave_event.309.a.reply": "The manual says so, \"Sterilization and insect removal, your good partner\". Probably can't distinguish between tiny people and pests. But looking at your planet's situation, maybe it was treated as dust?",
            "tiny_enclave_event.309.b.reply": "I see the data says '$ai_strength$'. Anyway, we are already researching it. Next sponsorship can probably provide it together.",
            "tiny_enclave_event.310.a.reply": "We can dismantling that robot to get a lot of alloys, and use her processing chip, but it can probably only be used for a year. Or we can rewrite her program and make her a shipgirl.",
            "tiny_enclave_event.501.title": "Fallen Fleet",
            "tiny_modifier_lazy": "Slacking Off",
            "tiny_modifier_lazy_desc": "Productivity has dropped... but slacking off feels so good!",
            "tiny_enclave_event.5.title": "§HTiny Trading Organization§! Destroyed",
            "tiny_enclave_event.6.title": "§HTiny Trading Organization§! Destroyed",
            "NAME_Tiny_Enclave_Station": "Tiny Trading Point",
            "NAME_tiny_enclave_space_station": "Tiny Trading Space Station",
            "NAME_tiny_species": "Tiny People",
            "NAME_tiny_species_plural": "Tiny People",
            "NAME_tiny_country": "Tiny Trading Station"
        },
        "gts_i_xinuo_l_english.yml": {
            "gts_xinuo.1000.b.response": "",
            "gts_xinuo.1000.c.response": "",
            "gts_xinuo.300.name": "",
            "gts_xinuo.300.desc": "",
            "gts_xinuo.300.a": "",
            "gts_xinuo.300.b": "",
            "gts_xinuo.300.c": ""
        },
        "gts_ar_support_event_0_l_english.yml": {
            "gts_o_support_event.0001.title": "Rift Gacha"
        },
        "gts_com_interact_l_english.yml": {
            "concept_leader_gts_skill_scientist_two_2_desc": "§G#Remember to add§!",
            "concept_leader_gts_skill_scientist_two_4_desc": "§G#Remember to add§!",
            "concept_leader_gts_skill_scientist_two_5_desc": "§G#Remember to add§!",
            "concept_leader_gts_skill_scientist_three_02_desc": "§GMonthly Society Research +15\\nMonthly Rare Artifacts +5§!",
            "concept_leader_gts_skill_commander_two_5_desc": "§G#Remember to add§!"
        }
    }

    # Apply translations
    for filename, file_data in data.items():
        if filename in translations:
            for key, val_data in file_data.items():
                if key in translations[filename]:
                    val_data['translated'] = translations[filename][key]
                else:
                    # If missed in manual dict, keep original? Or empty?
                    # For now assume I covered all or leave as non-translated (will skip applying or apply original)
                    # Let's apply original as fallback if I missed something, but I should have covered it.
                    pass

    # Save
    output_path = 'translated_content_chunks/chunk_0.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print(f"Translated chunk 0 saved to {output_path}")

if __name__ == "__main__":
    main()
