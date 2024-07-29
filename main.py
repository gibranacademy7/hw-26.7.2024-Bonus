# יבוא הקובץ כולו בשמו הרגיל
import my_function;
my_function.print_stars();

# ייבוא הקובץ כולו בשם מקוצר של mf
import my_function as mf;
mf.print_stars();


# יבוא רק הפונקציה print_stars באמצעות from
from my_function import print_stars;
print_stars();


