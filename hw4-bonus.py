import random;

def lost_city():
    # רשימה של ערים לבחירה אקראית
    cities = ["New York", "Los Angeles", "London", "Paris", "Tokyo",\
              "Berlin", "Sydney", "Madrid", "Moscow", "Toronto"];

    # בחירת עיר אקראית מהרשימה והפיכתה לאותיות גדולות (למניעת בעיות רגיסטר)
    city = random.choice(cities).upper();  # הפונקציה random.choice בוחרת עיר אחת אקראית מהרשימה

    # יצירת התצוגה הראשונית של שם העיר עם קווים תחתונים במקום אותיות
    city_display = ''.join(['_' if char.isalpha() else char for char in city]);
    # מחליפים כל אות בתו _ וכל תו שאינו אות נשאר כפי שהוא

    # רשימת האותיות שניחשו השחקנים
    guessed_letters = [];   ### guessed_letters מאחסנת את האותיות שניחשו השחקנים.

    # ספירת מספר הניחושים
    attempts = 0;

    # הודעת פתיחה ותצוגת העיר בהתחלה
    print("Welcome to Lost City!");
    print(f"The city is: {city_display}");

    # לולאה שתרוץ עד שכל האותיות ינחשו נכון
    while '_' in city_display:
        # בקשת ניחוש מהשחקן
        guess = input("Guess a letter: ").upper();
        attempts += 1;

        # בדיקה אם האות כבר ניחשה בעבר
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again!");
            continue

        # הוספת האות לרשימת האותיות שניחשו
        guessed_letters.append(guess);

        # אם האות קיימת בשם העיר
        if guess in city:
            # עדכון תצוגת העיר עם האותות הנכונות שניחשו
            city_display = ''.join(
                [char if char in guessed_letters else '_' if char.isalpha() else char for char in city]);
            print(f"Good guess! The city is: {city_display}");
        else:
            # הודעה שהאות לא קיימת בעיר
            print("This letter does`nt exist, try again!");
            print(f"The city is: {city_display}");

    # הודעה על סיום המשחק ומספר הניחושים
    print(f"Congratulations! You've found the city {city} in {attempts} attempts.");


# קריאה לפונקציה להתחלת המשחק
lost_city();
