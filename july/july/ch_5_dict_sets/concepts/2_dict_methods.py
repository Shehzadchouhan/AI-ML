marks={
    "sheh":100,
    "rohan":200,
    "aman":23
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"sheh":50,"renu":20})
# print(marks)

print(marks.get("sheh"))
print(marks.get("Sheh2"))# gives none
print(marks("Sheh2")) #give error
