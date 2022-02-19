
with open("/24day_Mail Merge/Mail Merge Project Start/Input/Letters/starting_letter.txt") as letters:
    content = letters.read()

with open("/24day_Mail Merge/Mail Merge Project Start/Input/Names/invited_names.txt") as names:
    name = names.readlines()
    #각 줄의 이름을 불러온다

for people in name:
    change_name = content.replace("[name]", people.strip())
    with open(f"/24day_Mail Merge/Mail Merge Project Start/Output/{people}.text", "w") as new_file:
        new_file.write(change_name)






