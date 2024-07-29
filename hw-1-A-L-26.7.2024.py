name_address = "Wisam Gibran Nof Hagalil"

# a. הדפסת אורך המחרוזת
print(len(name_address));

# b. הדפסת המחרוזת באותיות גדולות
print(name_address.upper());

# c. הדפסת המחרוזת באותיות קטנות
print(name_address.lower());

# d. בדיקת אם המחרוזת מתחילה בשם הפרטי
print(name_address.startswith("Wisam"));

# e. בדיקת אם המחרוזת מסתיימת בעיר המגורים
print(name_address.endswith("Nof Hagalil"));

# f. פירוק המחרוזת לרשימה
split_list = name_address.split();
print(split_list);

# g. הפיכת הרווחים לכוכביות ואז פירוק המחרוזת מחדש
starred_string = name_address.replace(" ", "*");
starred_list = starred_string.split("*");
print(starred_list);

# h. הדפסת המחרוזת במרכז של 50 תווים, עטופה בתו "="
centered_string = name_address.center(50, "=");
print(centered_string);

# i. הדפסת המחרוזת מהתו ה-4 ועד הסוף
print(name_address[3:]);

# j. הדפסת המחרוזת מתחילתה ועד לתו ה-4 (כולל)
print(name_address[:4]);

# k. הדפסת כל התווים הזוגיים במחרוזת
print(name_address[::2]);

# l. דאג שכל מילה במחרוזת תתחיל באות גדולה
print(name_address.title());
