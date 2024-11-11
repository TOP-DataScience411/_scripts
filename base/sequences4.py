par = 'Return True if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.'

words = par.split()


# >>> words
# ['Return', 'True', 'if', 'the', 'string', 'is', 'a', 'titlecased', 'string', 'and', 'there', 'is', 'at', 'least', 'one', 'character,', 'for', 'example', 'uppercase', 'characters', 'may', 'only', 'follow', 'uncased', 'characters', 'and', 'lowercase', 'characters', 'only', 'cased', 'ones.', 'Return', 'False', 'otherwise.']
# >>>
# >>> par.split('and')
# ['Return True if the string is a titlecased string ', ' there is at least one character, for example uppercase characters may only follow uncased characters ', ' lowercase characters only cased ones. Return False otherwise.']


# >>> ' '.join(words)
# 'Return True if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. Return False otherwise.'
# >>>
# >>> '__'.join(words)
# 'Return__True__if__the__string__is__a__titlecased__string__and__there__is__at__least__one__character,__for__example__uppercase__characters__may__only__follow__uncased__characters__and__lowercase__characters__only__cased__ones.__Return__False__otherwise.'
# >>>
# >>> ''.join(words)
# 'ReturnTrueifthestringisatitlecasedstringandthereisatleastonecharacter,forexampleuppercasecharactersmayonlyfollowuncasedcharactersandlowercasecharactersonlycasedones.ReturnFalseotherwise.'


# >>> words[-1]
# 'otherwise.'
# >>>
# >>> words[-1].isalpha()
# False
# >>>
# >>> words[-1][:-1]
# 'otherwise'
# >>>
# >>> words[-1][:-1].isalpha()
# True


puncts = '.,!?'

# >>> words[-1]
# 'otherwise.'
# >>>
# >>> words[-1].strip(puncts)
# 'otherwise'


# >>> par.upper()
# 'RETURN TRUE IF THE STRING IS A TITLECASED STRING AND THERE IS AT LEAST ONE CHARACTER, FOR EXAMPLE UPPERCASE CHARACTERS MAY ONLY FOLLOW UNCASED CHARACTERS AND LOWERCASE CHARACTERS ONLY CASED ONES. RETURN FALSE OTHERWISE.'
# >>>
# >>> par.lower()
# 'return true if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones. return false otherwise.'
# >>>
# >>> par.title()
# 'Return True If The String Is A Titlecased String And There Is At Least One Character, For Example Uppercase Characters May Only Follow Uncased Characters And Lowercase Characters Only Cased Ones. Return False Otherwise.'

