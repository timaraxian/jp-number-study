def units_to_jp(units):
    switcher = {
        "1": "いち",
        "2": "に",
        "3": "さん",
        "4": "よん",
        "5": "ご",
        "6": "ろく",
        "7": "なな",
        "8": "はち",
        "9": "きゅう",
    }
    return switcher.get(units, "")

def jyuu_to_jp(jyuu):
    switcher = {
        "1": "じゅう",
        "2": "にじゅう",
        "3": "さんじゅう",
        "4": "よんじゅう",
        "5": "ごじゅう",
        "6": "ろくじゅう",
        "7": "ななじゅう",
        "8": "はちじゅう",
        "9": "きゅうじゅう",
    }
    return switcher.get(jyuu, "")

def hyaku_to_jp(hyaku):
    switcher = {
        "1": "ひゃく",
        "2": "にひゃく",
        "3": "さんびゃく",
        "4": "よんひゃく",
        "5": "ごひゃく",
        "6": "ろっぴゃく",
        "7": "ななひゃく",
        "8": "はっぴゃく",
        "9": "きゅうひゃく",
    }
    return switcher.get(hyaku, "")

def sen_to_jp(sen):
    switcher = {
        "1": "せん",
        "2": "にせん",
        "3": "さんぜん",
        "4": "よんせん",
        "5": "ごせん",
        "6": "ろくせん",
        "7": "ななせん",
        "8": "はっせん",
        "9": "きゅうせん",
    }
    return switcher.get(sen, "")

def man_to_jp(man):
    if len(str(man)) == 1:
        return units_to_jp(man) + "まん"
    if len(str(man)) == 2:
        return jyuu_to_jp(str(man)[0]) + units_to_jp(str(man)[1]) + "まん"
    if len(str(man)) == 3:
        return hyaku_to_jp(str(man)[0]) + jyuu_to_jp(str(man)[1]) + units_to_jp(str(man)[2]) + "まん"
    
    return ""

def num_to_jp(num):
    num_array = list(reversed([int(x) for x in str(num)]))
    
    units = ''.join([str(x) for x in num_array[:1]])
    jyuu = ''.join([str(x) for x in num_array[1:2]])
    hyaku = ''.join([str(x) for x in num_array[2:3]])
    sen = ''.join([str(x) for x in num_array[3:4]])
    man = ''.join([str(x) for x in reversed(num_array[4:7])])
    oku = ''.join([str(x) for x in reversed(num_array[7:10])])
    
    return man_to_jp(man) + " " + sen_to_jp(sen) + " " + hyaku_to_jp(hyaku) + " " + jyuu_to_jp(jyuu) + " " + units_to_jp(units)
