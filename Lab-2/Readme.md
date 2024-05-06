# Lab - 2 : Attacking Classic Crypto Systems

## Task - 1 : Decrypting Caesar Cipher

The given cipher is : `"odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo"`

The following bruteforce python code is used to decrypt it.

```python
def decrypt_caesar_cipher(cipher_text):
    for shift in range(26):
        plain_text = ""
        for char in cipher_text:
            if char.isalpha():
                shifted = ord(char) - shift
                if char.islower():
                    if shifted < ord('a'):
                        shifted += 26
                elif char.isupper():
                    if shifted < ord('A'):
                        shifted += 26
                plain_text += chr(shifted)
            else:
                plain_text += char
        print('Shift #%s: %s' % (shift, plain_text))

message = 'odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo'

decrypt_caesar_cipher(message)
```

### Output :

```
Shift #0: odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo
Shift #1: ncqnandvrbcqnknbcbvjaclxwcajlcyujcoxavxdccqnan
.....
Shift #10: ethereumisthebestsmartcontractplatformoutthere
.....
Shift #25: pespcpfxtdespmpdedxlcenzyeclneawleqzcxzfeespcp
```

From all possible 26 shifts, shift 10 is the probable plain text. For shift 26, deciphered text is

`ethereum is the best smart contract platform out there`

## Task - 2 : Substitution Cipher

Two cipher text and a frequency distribution of english characters are given. Need to decipher them.

Here, most frequent character in the cipher text will be replaced with the most frequent english character from the distribution table.

```
- Sort frequency distribution in descending order.
- Find frequency distribution of letters in cipher text and sort in descending order.
- Map the letters according to frequency distribution to decrypt the text.
```

### Substitution Cipher Breaker :
```py
def substitution_cipher(cipher_text, english_freq):

    sorted_english_freq = dict(sorted(english_freq.items(), key=lambda x : x[1], reverse = True))

    char_freq = {}
    total = 0
    # frequency count
    for char in cipher_text:
        if char.isalpha():
            char = char.lower()
            total += 1
            char_freq[char] = char_freq.get(char, 0) + 1

    char_percentage = {}
    # frequency distribution of cipher text
    for char, freq in char_freq.items():
        char_percentage[char] = (freq / total) * 100

    sorted_char_percentage = dict(sorted(char_percentage.items(), key=lambda x : x[1], reverse = True))

    order = "abcdefghijklmnopqrstuvwxyz"
    key = order
    # mapping
    for char in order:
        if char in sorted_char_percentage:
            index = list(sorted_char_percentage.keys()).index(char)
            char_key = list(sorted_english_freq.keys())[index]
            key = key.replace(char, char_key)
    
    decipher_text = ""
    for char in cipher_text:
        if char.isalpha():
            if char.islower():
                decipher_text += key[ord(char) - ord('a')]
            else:
                decipher_text += key[ord(char) - ord('A')].upper()
        else:
            decipher_text += char

    print("Key : ", key)
    print("Deciphered Text :", decipher_text)


english_freq = {
'a': 8.05, 'b': 1.67, 'c': 2.23, 'd': 5.10, 'e': 12.22, 'f': 2.14, 'g': 2.30, 'h': 6.62, 'i': 6.28, 'j': 0.19, 'k': 0.95, 'l': 4.08, 'm': 2.33, 
'n': 6.95, 'o': 7.63, 'p': 1.66, 'q': 0.06, 'r': 5.29, 's': 6.02, 't': 9.67, 'u': 2.92, 'v': 0.82, 'w': 2.60, 'x': 0.11, 'y': 2.04, 'z': 0.06
}

cipher1 = "af p xpkcaqvnpk pfg, af ipqe qpri, gauuikifc tpw, ceiri udvk tiki afgarxifrphni cd eao-wvmd popkwn, hiqpvri du ear jvaql vfgikrcpfgafm du cei xkafqaxnir du xrwqedearcdkw pfg du ear aopmafpcasi xkdhafmr afcd fit pkipr. ac tpr qdoudkcafm cd lfdt cepc au pfwceafm epxxifig cd ringdf eaorinu hiudki cei opceiopcaqr du cei uaing qdvng hi qdoxnicinw tdklig dvc-pfg edt rndtnw ac xkdqiigig, pfg edt odvfcpafdvr cei dhrcpqnir--ceiki tdvng pc niprc kiopaf dfi mddg oafg cepc tdvng qdfcafvi cei kiripkqe"


substitution_cipher(cipher1, english_freq)
```

### Output : 

```
Key :  lbagjodoeyikblcomijgmyyfyz

Deciphered Text : lo o foialmyloi ood, lo eomj moie, dlmmeieoa goy, ajeie mgyi geie lodlifeoioole ag jlc-yybg ocoiyl, oemoyie gm jli yylmk yodeiiaoodlob gm aje filomlflei gm fiymjgjliagiy ood gm jli lcoblooalje figolobi loag oeg oieoi. la goi mgcmgialob ag kogg ajoa lm ooyajlob joffeoed ag ieldgo jlcielm oemgie aje coajecoalmi gm aje mleld mgyld oe mgcfleaely ggiked gya-ood jgg ilggly la figmeeded, ood jgg cgyoaologyi aje goiaomlei--ajeie ggyld oa leoia iecolo goe bggd clod ajoa ggyld mgoaloye aje ieieoimj
```

Second cipher text : 

```
"aceah toz puvg vcdl omj puvg yudqecov, omj loj auum klu thmjuv hs klu zlcvu shv zcbkg guovz, upuv zcmdu lcz vuwovroaeu jczoyyuovomdu omj qmubyudkuj vukqvm. klu vcdluz lu loj avhqnlk aodr svhw lcz kvopuez loj mht audhwu o ehdoe eunumj, omj ck toz yhyqeoveg auecupuj, tlokupuv klu hej sher wcnlk zog, klok klu lcee ok aon umj toz sqee hs kqmmuez zkqssuj tckl kvuozqvu. omj cs klok toz mhk umhqnl shv sowu, kluvu toz oezh lcz yvhehmnuj pcnhqv kh wovpue ok. kcwu thvu hm, aqk ck zuuwuj kh lopu eckkeu ussudk hm wv. aonncmz. ok mcmukg lu toz wqdl klu zowu oz ok scskg. ok mcmukg-mcmu klug aunom kh doee lcw tuee-yvuzuvpuj; aqk qmdlomnuj thqej lopu auum muovuv klu wovr. kluvu tuvu zhwu klok zlhhr klucv luojz omj klhqnlk klcz toz khh wqdl hs o nhhj klcmn; ck zuuwuj qmsocv klokomghmu zlhqej yhzzuzz (oyyovumkeg) yuvyukqoe ghqkl oz tuee oz (vuyqkujeg) cmubloqzkcaeu tuoekl. ck tcee lopu kh au yocj shv, klug zocj. ck czm'k mokqvoe, omj kvhqaeu tcee dhwu hs ck! aqk zh sov kvhqaeu loj mhk dhwu; omj oz wv. aonncmz toz numuvhqz tckl lcz whmug, whzk yuhyeu tuvu tceecmn kh shvncpu lcw lcz hjjckcuz omj lcz nhhj shvkqmu. lu vuwocmuj hm pczckcmn kuvwz tckl lcz vueokcpuz (ubduyk, hs dhqvzu, klu zodrpceeu- aonncmzuz), omj lu loj womg juphkuj ojwcvuvz owhmn klu lhaackz hs yhhv omj qmcwyhvkomk sowcecuz. aqk lu loj mh dehzu svcumjz, qmkce zhwu hs lcz ghqmnuv dhqzcmz aunom kh nvht qy. klu uejuzk hs kluzu, omj aceah'z sophqvcku, toz ghqmn svhjh aonncmz. tlum aceah toz mcmukg-mcmu lu ojhykuj svhjh oz lcz lucv, omj avhqnlk lcw kh ecpu ok aon umj; omj klu lhyuz hs klu zodrpceeu- aonncmzuz tuvu scmoeeg jozluj. aceah omj svhjh loyyumuj kh lopu klu zowu acvkljog, zuykuwauv 22mj. ghq loj aukkuv dhwu omj ecpu luvu, svhjh wg eoj, zocj aceah hmu jog; omj klum tu dom dueuavoku hqv acvkljog-yovkcuz dhwshvkoaeg khnukluv. ok klok kcwu svhjh toz zkcee cm lcz ktuumz, oz klu lhaackz doeeuj klu cvvuzyhmzcaeu ktumkcuz auktuum dlcejlhhj omj dhwcmn hs onu ok klcvkg-klvuu"
```

Output : 

```
Key :  edcphfbaidfhmcakgrmfergxpi

Deciphered Text : echea fai kerb rcph amd kerb pepghcar, amd had eeem fhe famder am fhe ihcre mar icdfb beari, eker icmpe hci regarraehe dciappearampe amd gmedpepfed refgrm. fhe rcphei he had eragchf eapr mrag hci frakehi had maf eepage a hapah hecemd, amd cf fai papgharhb eehceked, fhafeker fhe ahd mahr gcchf iab, fhaf fhe hchh af eac emd fai mghh am fgmmehi ifgmmed fcfh freaigre. amd cm fhaf fai maf emagch mar mage, fhere fai ahia hci prahamced kccagr fa garkeh af. fcge fare am, egf cf ieeged fa hake hcffhe emmepf am gr. eacccmi. af mcmefb he fai ggph fhe iage ai af mcmfb. af mcmefb-mcme fheb eecam fa pahh hcg fehh-preierked; egf gmphamced faghd hake eeem mearer fhe garr. fhere fere iage fhaf ihaar fhecr headi amd fhagchf fhci fai faa ggph am a caad fhcmc; cf ieeged gmmacr fhafambame ihaghd paiieii (apparemfhb) perpefgah bagfh ai fehh ai (repgfedhb) cmedhagifcehe feahfh. cf fchh hake fa ee pacd mar, fheb iacd. cf cim'f mafgrah, amd fragehe fchh page am cf! egf ia mar fragehe had maf page; amd ai gr. eacccmi fai cemeragi fcfh hci gameb, gaif peaphe fere fchhcmc fa marccke hcg hci addcfcei amd hci caad marfgme. he regacmed am kcicfcmc fergi fcfh hci rehafckei (edpepf, am pagrie, fhe iaprkchhe- eacccmiei), amd he had gamb dekafed adgcreri agamc fhe haeecfi am paar amd gmcgparfamf magchcei. egf he had ma phaie mrcemdi, gmfch iage am hci bagmcer pagicmi eecam fa craf gp. fhe ehdeif am fheie, amd echea'i makagrcfe, fai bagmc mrada eacccmi. fhem echea fai mcmefb-mcme he adapfed mrada ai hci hecr, amd eragchf hcg fa hcke af eac emd; amd fhe hapei am fhe iaprkchhe- eacccmiei fere mcmahhb daihed. echea amd mrada happemed fa hake fhe iage ecrfhdab, iepfegeer 22md. bag had eeffer page amd hcke here, mrada gb had, iacd echea ame dab; amd fhem fe pam peheerafe agr ecrfhdab-parfcei pagmarfaehb facefher. af fhaf fcge mrada fai ifchh cm hci ffeemi, ai fhe haeecfi pahhed fhe crreipamicehe ffemfcei eeffeem phchdhaad amd pagcmc am ace af fhcrfb-fhree
```

### Observation:

In second cipher text, some words can be recognized such as `had`, `he`, `here`, `bag` etc.

So, second cipher is more likely to be broken.

But the given cipher could not be broken. One reason maybe the need of more complex algorithm to break the cipher and more data apart from frequency distribution.
