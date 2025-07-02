from string import Template


name = "João Gabriel"
age = 24
height = 1.83
text = "Sou {name} e tenho {age} ano(s). Tenho {height:.1f} metros de altura."

format = text.format(name=name, age=age, height=height)
print(format)

template = Template("Meu nome é $name e minha idade é $age ano(s).")
print(template.substitute(name=name, age=age))
