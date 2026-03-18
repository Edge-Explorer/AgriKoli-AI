import json
import os
import random

def generate_perfect_large_dataset():
    # 1. Base Hand-Crafted High-Quality Samples (Bilingual Instructions)
    hand_crafted = [
        {"instruction": "कुटुंबाची चौकशी कर. / Ask about the family.", "input": "", "output": "काय चाललंय रे? घरचे सर्व कसे हायेत? आयू-बापुस मजेत हायेत ना?"},
        {"instruction": "आज जेवणात काय आहे? / What is for food today?", "input": "", "output": "आज जेवानाला काय रांधलंय ग? मासली हाय की सुकं हाय?"},
        {"instruction": "पाहुण्यांचे स्वागत कर. / Welcome the guests.", "input": "", "output": "या रे, बसा. पानी-बिनी घ्या आधी. खूप दिसानी आलात तुम्ही आमचे कडे."},
        {"instruction": "त्याला बाजारात जायला सांग. / Tell him to go to the market.", "input": "", "output": "अरे, तेवढं बाजारात जाऊन ये रे. घरांत थोडे सामान संपलंय, ते घेऊन ये लवकर."},
        {"instruction": "शेतीच्या कामाबद्दल विचार. / Ask about the farm work.", "input": "", "output": "काय रे, शेताचं काम कसं चाललंय? आगरं-बिगरं नीटं नीटं केलीत ना?"},
        {"instruction": "पाऊस पडल्यावरची स्थिती सांग. / Describe the situation after rain.", "input": "", "output": "अरे लय पाऊस झालाय, शेतांत पाणीच पाणी साचलंय. आता चिखल झालाय, कामं अडकलीत सगळी."},
        {"instruction": "पीक कापणीबद्दल बोल. / Talk about crop harvesting.", "input": "", "output": "भात कापणीला आलीय. आता पोरांना घेऊन शेतावर जावं लागल. लय अदावत (अडचण) होईल जर पाऊस आला तर."},
        {"instruction": "होडी समुद्रात न्यायला सांग. / Tell to take the boat to sea.", "input": "", "output": "होडीला दर्यात ढकल रे लवकर. भरतीची वेळ झालीय, मासले चांगले मिळतील आज."},
        {"instruction": "जाळ्यात जास्त मासे आल्यावर काय म्हणशील? / What to say when the net is full of fish?", "input": "", "output": "अय्या! आज तर लय मासले गावलेत (मिळालेत). वाघटी, सुरमई सगळं जाळ्यांत हाय. बरं झालं रे!"},
        {"instruction": "कोळी गाण्याबद्दल बोल. / Talk about Koli songs.", "input": "", "output": "एकदा कोळी गीत लावून दे रे. गाण्यावर नाचायला लय मजा येते आपल्या कोळीवाड्यात."},
        {"instruction": "रस्ता विचार. / Ask for directions.", "input": "ठाण्याला जाण्याचा रस्ता / Way to Thane", "output": "अरे बाबा, ठाण्याला जायला ह्योच रस्ता सरळ पकड. पुढे गेल्यावर मोठा नाका लागल, तिथून डावीकडे वळ."},
        {"instruction": "आरोग्याची विचारपूस कर. / Ask about health.", "input": "", "output": "काय झालं रे? चेहरा असा उतरलाय का? काय टायमट (आजारपण) हाय का? डॉक्टरकडे जाऊन ये रे."},
        {"instruction": "काम वेळेवर पूर्ण करण्याच्या सूचना दे. / Instructions to complete work on time.", "input": "", "output": "हे बघ, काम टायमावर झालं पायजेल. उशीर करू नकोस, नायतर लय अदावत होईल."},
        {"instruction": "सणाबद्दल माहिती विचार. / Ask about the festival.", "input": "नारळी पौर्णिमा / Narali Pournima", "output": "आपल्या नारली पुनवेची तयारी कशी चाललीय? सोन्याचा नारल दर्याला द्यायची वेळ झालीय रे!"},
        {"instruction": "लग्नाच्या आमंत्रणासाठी काय म्हणाल? / What to say for a wedding invitation?", "input": "", "output": "आमच्या पोराचं लगीन हाय, विसरू नका हं? अख्ख्या परिवाराला घेऊन वराताला ये रे!"},
        {"instruction": "एखाद्याला सावध करताना काय म्हणशील? / What to say when warning someone?", "input": "", "output": "जपून जा रे, पाऊस लय हाय आणि रस्ता खराब झालाय. अदावत येईल वाटेत."},
        {"instruction": "शुभ सकाळ म्हण. / Say Good Morning.", "input": "", "output": "राम राम! काय म्हणतोय? उठला की नय अजून?"},
        {"instruction": "खूप भूक लागली आहे असे सांग. / Say you are very hungry.", "input": "", "output": "पोटांत कावळे ओरडतायत रे, लवकर जेवायला वाढ ग!"},
        {"instruction": "वेळ किती झाली ते विचार. / Ask what time it is.", "input": "", "output": "काय टाइम झालाय रे? घराला जायची वेळ झाली आता."},
        {"instruction": "एखाद्याच्या यशाचे कौतुक कर. / Praise someone's success.", "input": "", "output": "लय भारी रे! तू तर नाव काढलंस आपलं. असाच पुढे जात राह."},
    ]

    # 2. Base vocabulary (Keep original)
    vocab = {
        "mother": ["आई", "आऊ", "गय"],
        "father": ["बाबा", "बापुस", "दादा"],
        "difficulty": ["अडचण", "अदावत", "त्रास"],
        "fish": ["मासा", "मासली", "मासले"],
        "sea": ["समुद्र", "दर्य", "दर्या"],
        "food": ["जेवण", "खाण-बिणं", "रांधलेलं"],
        "work": ["काम", "काम-धंदा", "चाकरी"],
        "house": ["घर", "खोली", "वाडा"],
        "time": ["वेळ", "टायम", "घडी"],
        "friend": ["मित्र", "पोरगा", "दोस्त"],
        "come": ["ये", "ये रे", "ये ग"],
        "go": ["जा", "जा रे", "जा ग"],
        "eat": ["खा", "जेव", "तावा मार"],
        "look": ["बघ", "बघ रे", "बघ ग", "जोय"],
        "how_are_you": ["कसा आहेस?", "काय म्हणतंय?", "बरा हायस ना?"],
    }

    templates = [
        {
            "instruction_mr": "कुटुंबाची चौकशी कर.",
            "instruction_en": "Ask about the family.",
            "outputs": [
                "काय म्हणतंय {friend}? {mother} आणि {father} मजेत हायेत ना?",
                "{father} कसं हाय? लय दिसानी गावलास रे!",
                "{mother} ने काय रांधलंय आज? पोटांत कावळे ओरडतायत."
            ]
        },
        {
            "instruction_mr": "कामाबद्दल विचार.",
            "instruction_en": "Ask about work.",
            "outputs": [
                "काय {friend}, {work} कसं चाललंय? लय {difficulty} हाय की काय?",
                "आज {work} ला जायचं नाय का? {time} झालाय बघ.",
                "{work} नीटं नीटं कर रे, नायतर नंतर लय {difficulty} होईल."
            ]
        },
        {
            "instruction_mr": "मासेमारीबद्दल बोल.",
            "instruction_en": "Talk about fishing.",
            "outputs": [
                "आज {sea} ला जायला उशीर झाला रे, {time} निघून गेली भरतीची.",
                "जाळ्यांत लय {fish} गावलेत आज! {mother} कडे देऊन ये लवकर.",
                "{sea} शांत हाय आज, होडी नीटं चालव रे."
            ]
        },
        {
            "instruction_mr": "जेवणाबद्दल विचार.",
            "instruction_en": "Ask about food.",
            "outputs": [
                "आज {food} मध्ये काय हाय? {fish} हाय की सुकं?",
                "लवकर {food} वाढ ग, लय भूक लागली हाय.",
                "ये रे {friend}, सोबत {eat} आपण आज."
            ]
        },
        {
            "instruction_mr": "हवामानाबद्दल सांग.",
            "instruction_en": "Describe the weather.",
            "outputs": [
                "दर्यात लय लाटा उसळल्यात, आज {sea} ला जाणं धोक्याचं हाय रे.",
                "वारा लय सुटलाय, घराची तावदानं नीट लावून घे रे.",
                "पाऊस लय पडतोय, शेतात पाणीच पाणी साचलंय आता."
            ]
        },
        {
            "instruction_mr": "बाजारात मासे विकण्याबद्दल बोल.",
            "instruction_en": "Talk about selling fish in the market.",
            "outputs": [
                "आज बाजारात मासले चांगले विकले गेले, खिसा गरम झालाय बघ!",
                "{mother} बाजाराला गेली का? मासले घेऊन ये लवकर.",
                "पाडव्याचा बाजार हाय, गर्दी लय असेल आज बाजारात."
            ]
        },
        {
            "instruction_mr": "आरोग्य आणि औषधाबद्दल बोल.",
            "instruction_en": "Talk about health and medicine.",
            "outputs": [
                "काय झालं रे {friend}? चेहरा असा पडलाय का? काय टायमट (आजारपण) हाय का?",
                "डॉक्टरकडे जाऊन ये रे, अंगात ताप चढलाय तुझ्या.",
                "जरा विश्रांती घे रे, कामाची लय धावपळ झालीय तुझी."
            ]
        }
    ]

    final_dataset = hand_crafted.copy()
    
    # 3. Augmentation logic to reach 1000+ entries (Alternating Languages)
    for i in range(1000):
        template = random.choice(templates)
        output_template = random.choice(template["outputs"])
        
        # Alternate between Marathi, English, and Bilingual instructions
        if i % 3 == 0:
            instruction = template["instruction_mr"]
        elif i % 3 == 1:
            instruction = template["instruction_en"]
        else:
            instruction = f"{template['instruction_mr']} / {template['instruction_en']}"
            
        final_output = output_template.format(
            mother=random.choice(vocab["mother"]),
            father=random.choice(vocab["father"]),
            friend=random.choice(vocab["friend"]),
            difficulty=random.choice(vocab["difficulty"]),
            fish=random.choice(vocab["fish"]),
            sea=random.choice(vocab["sea"]),
            food=random.choice(vocab["food"]),
            work=random.choice(vocab["work"]),
            time=random.choice(vocab["time"]),
            eat=random.choice(vocab["eat"]),
        )
        
        final_dataset.append({
            "instruction": instruction,
            "input": f"Context {i+1}" if i % 15 == 0 else "", 
            "output": final_output
        })

    os.makedirs('data', exist_ok=True)
    output_path = 'data/agrikoli_training_dataset.json'
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(final_dataset, f, ensure_ascii=False, indent=4)
    
    return output_path

if __name__ == "__main__":
    path = generate_perfect_large_dataset()
    print(f"Final training dataset generated at: {path}")
    print(f"Total entries: {len(json.load(open(path, encoding='utf-8')))}")
