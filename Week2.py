'''
اكتبي لعبة تطبع اسم اللعبة أولاًكتبي برنامج يقوم بالطلب من المستخدم بإدخال رقم
"Enter a number: "
ثم يعيد له إن كان الرقم زوجي
"Number is even"
إذا كان فردي
"Number is odd"
اكتبي البرنامج في Atom وجربيه في بايثون على عدة أرقام.
'''
number=float(input("Enter a number : "))
if number%2==0:
    print("Number is even")
else:
    print("Number is odd")
