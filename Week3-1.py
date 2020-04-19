'''
اكتبي لعبة تطبع اسم اللعبة أولاً
Numbers from 1 to 10
ثم تطلب من المستخدم أن يحزر الرقم
"Guess the number: "
إذا المستخدم لم يدخل الرقم الصحيح ستبقى اللعبة تسأله للأبد، إذا قام بإدخال الرقم الصحيح، يظهر للمستخدم:
"Great! You did it!"
لا تنسي أن تقومي بتخزين رقم من اختيارك ليكون هو الرقم الصحيح وتخزينه في متغير.
الرقم يجب أن يكون بين 1 و10
جربي الكود من خلال عمل run للملف على command prompt- terminal.
'''

print('Numbers from 1 to 10')
i=8
number=int(input("Guss the number : "))
while i!=number:
    number=int(input("Guss the number: "))
print("Great! You did it!")
