while 1:
    price = int(input("gheymat kol ra vared konid(toman)...;"))
    if price == 0 :
        break
    elif price < 0 :
        print ("gheymat dorost ra vared konid!...")
        continue
    percent = float(input("darsad ra vared konid"))
    if percent == 0 or percent > 100 or percent < 0:
        print ("lotfan darsad dorost ra vared konid")
        continue
    darsad_kol = (price * percent) /100,
    print (f"darsakol shoma mosavi ast ba {darsad_kol}toman")
    