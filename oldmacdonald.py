def old_macdonald(name):
    first_letter = name[0]
    inbet= name[1:3]
    fourth=name[3]
    rest=name[4:]
    return first_letter.upper()+inbet+fourth.upper()+rest
print(old_macdonald('macdonald'))