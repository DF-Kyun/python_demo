import re
re_mail = re.compile(r'^(\<?[a-zA-Z0-9\s_.]+>)|([a-zA-Z0-9_.]+)(\@[a-z0-9]+)(.\w{3})')
x = input('input E-mail :')
if re_mail.match(x) == None:
    print('E-mail is wrong..')
elif '<' in x and  '>' in x:
    m = re_mail.match(x)
    print('E-mail name is ',m.group(1))
else:
    print('E-mail ok....')
