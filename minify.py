with open("comments.bf", "r") as f:
    program = f.read()
minified = ""
for i in program:
    if(i in [",",".","+","-","<",">","[","]"]):
        minified+=i
while("<>" in minified or "><" in minified or "+-" in minified or "-+" in minified):
    minified = minified.replace("<>", "").replace("><", "").replace("+-", "").replace("-+", "")
with open("minified.bf", "w") as f:
    f.write(minified+"\n")
