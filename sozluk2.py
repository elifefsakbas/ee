import time
meme_dict = {
            "LOL": "komik bir şeye verilen cevap",
            "CRINGE": "garip ya da utandırıcı bir şey",
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek"
            }
            
for i in range(5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")

    time.sleep(1)
    if word in meme_dict.keys():
        print("Bu kelimenin anlamı:", meme_dict[word])
        
    else:
        print("Henüz bu kelimeye sahip değiliz... Ama üzerinde çalışıyoruz!")
        
    time.sleep(1)
