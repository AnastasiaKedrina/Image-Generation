import re
import json

def phone_format(phone):
    phone = phone.removeprefix("+")
    phone = phone.removeprefix("1")     # remove leading +1 or 1
    phone = re.sub("[ ()-]", '', phone) # remove space, (), -
    # assert(len(phone) == 11)
    if len(phone)==11:
        phone = f"{phone[:1]}({phone[1:4]}){phone[4:7]}-{phone[7:9]}-{phone[9:]}"
    return phone

def add_line_break(text, length):
    s = []
    c = 0 
    for i in text.split(' '):
        c += len(i)+1
        if c>length:
            s.append('\n')   
        s.append(i)
    return ' '.join(s)

def get_GPT_headings():
    with open('parsed_data.json', encoding="utf8") as json_file:
        parsed_data = json.load(json_file)
    with open('gpt_output.json', encoding="utf8") as json_file:
        gpt_output = json.load(json_file)
    return parsed_data, gpt_output
