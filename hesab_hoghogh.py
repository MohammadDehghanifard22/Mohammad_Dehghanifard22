def hoghogh():
 while 1:     
     # "take: days you work "
       
    day_work = int(input("chand roz kar kardi ?"))
    if day_work <=0 or day_work >31 :
        print("lotfan tedad roz ha ra dorost vard konid !")
        continue
    
     # "take: Price in one day "
      
    day_price = int(input("rozane cheghadr poll migirid ? (Toman)"))
    if day_price <=0:
        print("lotfan dast mozd rozane  ra dorost vard konid !")
        continue
    
     # "take: paye sanavat "
     
    paye_sanavat = int(input("paye sanavat shoma cheghadr ast ? (Toman)"))
    if paye_sanavat < 0:
        print("lotfan paye sanavat ra dorost vard konid !")
        continue
    
    #" Hesab hoghogh paye "
    
    hoghogh_paye = (paye_sanavat + day_price) * day_work
    print (f"hoghogh paye shoma mosavi ast ba '{hoghogh_paye}' Toman")
    
    # "take: (daghighe) ezafe kari "
    
    ezafe_kari1 = int(input("chand daghighe ezafe kari kardin ? (دقیقه)"))
    if ezafe_kari1 < 0:
        print("lotfan dorost vared konid")
        continue
    
    #" Hesab ezafe kari "
    
    ezafe_kari =(ezafe_kari1 / 60)
    ezafe_kari_1h = (day_price / 7.33)*1.4
    
    price_ezafe_kari = (ezafe_kari * ezafe_kari_1h)
    print(f"pole ezafe kari shoma mosavi ast ba '..{price_ezafe_kari}..'(Toman) ")
   
     # "take: tedad farzand "

    tedad_farzand = int(input("chand farzand darid ? "))
    if tedad_farzand < 0:
        print("شما نمیتوانید این تعداد فرزند داشته یاشید")
        continue
    
     #" Hagh olad "

    hagh_olad = ((day_price * 3) * tedad_farzand)
    print (f"hagh olad shoma mosavi ast ba '..{hagh_olad}..'(Toman)")
    
     #" Hesab kol hoghogh "
    
    kol_hoghogh_shoma = (price_ezafe_kari + hoghogh_paye + hagh_olad)
    print(f"kol hoghogh  shoma mosavi ast ba '..{kol_hoghogh_shoma}..' (Toman) ")

    # hesab hagh maskan
    hagh_maskan_1403 = (900000)
    hagh_maskan = ((hagh_maskan_1403 /30)*day_work)
    print (f"hagh maskan shoma mosavi ast ba '.. {hagh_maskan}..' (Toman)")

    #hesab tatil kari 
     # "take: (daghighe) 
    tedad_saat_kar_M= int(input("chand daghighe ezafe kari kardin da tatilat ? (دقیقه)"))
    if tedad_saat_kar_M < 0:
        print("lotfan dorost vared konid")
        continue
    #tabdil be saat
    tedad_saat_kar_H =(tedad_saat_kar_M  / 60)
     #hesab
    hagh_tatili = ((day_price/7.33)*140 /100 * tedad_saat_kar_H) 
    
    print(f"kar shoma dar roz hay tatil mosavi ast ba'..{hagh_tatili}..' (Toman)")
   
    #jome kari((day_price * 40)/100)
    jome_kari = ((day_price * 40)/100)
    print(f"jome kari shoma mosavi ast ba'..{jome_kari}..' (Toman)")
    
    
    #hesab hagh khar bar(hagh moshakhas shode/30*tedad_roze)
    hagh_moshakhas_shode_1403 =(1400000) 
    hagh_kharbar = ((hagh_moshakhas_shode_1403 /30) *day_work)
    print(f"hagh kharcar shoma mosaavi ast ba'..{hagh_kharbar}..'(Toman)")
    
    #hagh bime
    hagh_bime_1403 = (6626329)
    hagh_bime = (hagh_bime_1403 *7)/100
    print(f"hagh bime shoma mosavi ast ba'..{hagh_bime}..' (Toman)")
   
    #maliyat
    
    
    #hohghogh kol
    kol_hoghogh_shoma = (price_ezafe_kari + hoghogh_paye + hagh_olad + hagh_kharbar + hagh_tatili + jome_kari - hagh_bime + hagh_maskan)
    print(f"kol hoghogh  shoma mosavi ast ba '..{kol_hoghogh_shoma}..' (Toman) ")
        
hoghogh()