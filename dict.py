alpha =[{"name":"Apollo","rules": "music,medicine, archery, sun","child": "Will Solace"},
         {"name":"Athena","rules": "wisdom, war","child": "Annabeth Grace"},
         {"name":"Posiodon", "rules":"Seas", "child":"Percy Jackson"},
         {"name":"Hades", "rules":"Underworld, minerals, stones", "child":"Nico DiAngelo"},
         {"name":"Peresphone", "rules":"fruits", "child":None}
]
# here alpha is the list and Gods are each item in the list.so thats why name, child etc belong to Gods\

for Gods in alpha:
    print(Gods["name"], Gods["child"], end=".\n")


dict = {"count":[], "item":[]}
