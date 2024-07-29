# a. הסר את הרווחים משני הצדדים של המחרוזת
str = " fun-day";
string = str.strip();
print(string);

# b. בדוק אם המחרוזת מכילה אותיות בלבד
str = "hello";
result = str.isalpha();
print(result);

# c. בדוק אם המחרוזת "777" מכילה מספרים בלבד
st = "777";
result = st.isdigit();
print(result);

# d. בדוק אם המחרוזת " " מכילה רווחים בלבד
string = " ";
result = string.isspace();
print(result);

# e. צור מחרוזת אחת מהרשימה
lst: list = ['A', 'P', 'P', 'L', 'E'];
result = ''.join(lst);
print(result);

# f. צור מחרוזת אחת עם '*' בין התווים מהרשימה
lst = ['A', 'P', 'P', 'L', 'E'];
result = '*'.join(lst);
print(result);

# g. בדוק אם האות ' ' מופיעה במילה ' ', תוך התעלמות מאותיות גדולות וקטנות
str = "hELLo Emma";
result = 'e' in str.lower();
print(result);

# h. קלוט מילה מהמשתמש וייצר רשימה של כל אות גדולה בלבד (התעלם ממספרים):
word = input("Enter a word: ");
result = [char.upper() for char in word if char.isalpha()];
print(result);







