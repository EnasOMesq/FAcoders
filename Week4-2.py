'''
المطلوب بهذا التحدي كتابة برنامج يقوم بالطلب من المستخدم (الأهل أو المعلمة) بإدخال اسم الطالب٫ فيعيد اسم الطالب بالإضافة إلى مجموع علاماته.
*أرجو كتابة رسالة الطلب كما هي في الأسفل
Enter student's name
علامات الطلاب وأسماؤهم مخزنة بداخل القوائم التالية٬ أرجو نسخها كما هي:
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
ملاحظة:
إذا أدخل المستخدم اسم غير موجود ستظهر له ملاحظة بأن الاسم غير مسجل٫ والمجموع صفر
مثال:
Enter student's name: Ayamn
Student is not recorded 0
مثال ٢:
Enter student's name: Sami
Sami 96
'''
s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
name =input("Enter student's name ")
if name in s1:
    print(name,sum(s1[1:]))
elif name in s2:
    print(name,sum(s2[1:]))
elif name in s3:
    print(name,sum(s3[1:]))
else:
    print("Student is not recorded 0")
