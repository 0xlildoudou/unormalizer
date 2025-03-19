# unormalizer
Tool for unormalize strings

## Explain
In programming, normalization often refers to the process of transforming data into a standardized format. This can be applied to various types of data, including text, numerical data, and database structures.

Normalization is important to avoid issues related to the multiple representations of certain characters, such as accents or ligatures.

But it is sometimes possible to bypass filters thanks to character normalization.

Indeed, if a sanitization filter is present before normalization, it's possible to bypass it by sending non-normalized characters that will pass the filters. 

### Text Normalization Formats

There are several normalization forms, but the most common ones are:

- NFC (Normalization Form C) : Canonical Composition, where characters are composed as much as possible.
- NFD (Normalization Form D) : Canonical Decomposition, where characters are decomposed into their base elements.
- NFKC (Normalization Form KC) : Compatibility Composition, which decomposes characters into their compatible forms before recomposing them.
- NFKD (Normalization Form KD) : Compatibility Decomposition, which decomposes characters into their compatible forms without recomposing them.


## Usage
```
unormalizer --- by 0xlildoudou
usage: unormalizer.py [-h] [-s S] [-f F] [--verbose]

options:
  -h, --help  show this help message and exit
  -s S        String to unormalize
  -f F        Normalisation format
  --verbose   Verbose mode
```

## Exemple

SSTI unormalize exemple:
```
python3 unormalizer.py -s "{{''.class.mro()[1].subclasses()}}" -f NFKC
```
```
{{''.class.mro()[1].subclasses()}}
︷︷＇＇․ᶜˡªſſ․ᵐʳº⁽⁾﹇¹﹈․ſᵘᵇᶜˡªſſᵉſ⁽⁾︸︸
﹛﹛﹛﹛﹒ⅽₗᵃˢˢ﹒ₘᵣᵒ₍₎［₁］﹒ˢᵤⓑⅽₗᵃˢˢₑˢ₍₎﹜﹜
｛｛｛｛．ⓒℓₐₛₛ．ⅿⓡₒ︵︶｛①｛．ₛⓤｂⓒℓₐₛₛℯₛ︵︶｝｝
ｃⅼⓐⓢⓢⓜｒℴ﹙﹚１ⓢｕ𝐛ｃⅼⓐⓢⓢⅇⓢ﹙﹚
𝐜ⓛａｓｓｍ𝐫ⓞ（）𝟏ｓ𝐮𝑏𝐜ⓛａｓｓⓔｓ（）
𝑐ｌ𝐚𝐬𝐬𝐦𝑟ｏ𝟙𝐬𝑢𝒃𝑐ｌ𝐚𝐬𝐬ｅ𝐬
𝒄𝐥𝑎𝑠𝑠𝑚𝒓𝐨𝟣𝑠𝒖𝒷𝒄𝐥𝑎𝑠𝑠𝐞𝑠
𝒸𝑙𝒂𝒔𝒔𝒎𝓇𝑜𝟭𝒔𝓊𝓫𝒸𝑙𝒂𝒔𝒔𝑒𝒔
𝓬𝒍𝒶𝓈𝓈𝓂𝓻𝒐𝟷𝓈𝓾𝔟𝓬𝒍𝒶𝓈𝓈𝒆𝓈
𝔠𝓁𝓪𝓼𝓼𝓶𝔯𝓸🯱𝓼𝔲𝕓𝔠𝓁𝓪𝓼𝓼𝓮𝓼
𝕔𝓵𝔞𝔰𝔰𝔪𝕣𝔬𝔰𝕦𝖇𝕔𝓵𝔞𝔰𝔰𝔢𝔰
𝖈𝔩𝕒𝕤𝕤𝕞𝖗𝕠𝕤𝖚𝖻𝖈𝔩𝕒𝕤𝕤𝕖𝕤
𝖼𝕝𝖆𝖘𝖘𝖒𝗋𝖔𝖘𝗎𝗯𝖼𝕝𝖆𝖘𝖘𝖊𝖘
𝗰𝖑𝖺𝗌𝗌𝗆𝗿𝗈𝗌𝘂𝘣𝗰𝖑𝖺𝗌𝗌𝖾𝗌
𝘤𝗅𝗮𝘀𝘀𝗺𝘳𝗼𝘀𝘶𝙗𝘤𝗅𝗮𝘀𝘀𝗲𝘀
𝙘𝗹𝘢𝘴𝘴𝘮𝙧𝘰𝘴𝙪𝚋𝙘𝗹𝘢𝘴𝘴𝘦𝘴
𝚌𝘭𝙖𝙨𝙨𝙢𝚛𝙤𝙨𝚞𝚌𝘭𝙖𝙨𝙨𝙚𝙨
𝙡𝚊𝚜𝚜𝚖𝚘𝚜𝙡𝚊𝚜𝚜𝚎𝚜
𝚕𝚕
```