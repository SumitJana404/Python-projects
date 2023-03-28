import pywhatkit as pw

txt=input("Enter Your text here :")

pw.text_to_handwriting(txt,"demo.png",[0,0,138])
print("end")