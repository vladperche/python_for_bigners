# .setdefault()

computers = { "Google":"Chromebook", "Apple":"MacBook", "Microsoft":"Surface Pro" }

# if "Lenovo" not in computers:
#     computers["Lenovo"] = "Thinkpad"
# print(computers)

computers.setdefault("Lenovo","Thinkpad") # The value Thinkpad will be added, because the key "Lenovo" does not exists
print(computers)

computers.setdefault("Lenovo","Ideapad") # The value Ideapad will NOT be updated, because the key "Lenovo" already exists
print(computers)

