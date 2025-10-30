# Defining a function
def function_name():
    pass
# Calling a function
function_name()

def print_header():
    print("="*20)
    print("Student\nR\neport")
    print("="*20)

print_header()

def draw_square():
    """Draws a 5x5 square using asterisks."""
    # print("*****")
    # print("*****")
    # print("*****")
    # print("*****")
    # print("*****")
    for i in range(5):
        print("*****")

# Test it
draw_square()


def morning_routine():
    print("🌅 MORNING ROUTINE")
    print("7:00 AM - Wake up")
    print("7:30 AM - Breakfast")
    print("8:00 AM - Catch bus to school")

def school_schedule():
    print("🏫 SCHOOL SCHEDULE")
    print("1st period - Math")
    print("2nd period - Science") 
    print("3rd period - English")
    print("4th period - Python Programming!")

def after_school():
    print("🎯 AFTER SCHOOL")
    print("3:00 PM - Robotics Club")
    print("5:00 PM - Homework")
    print("7:00 PM - Video games")

def daily_routine():
    # Show the full day
    morning_routine()
    print()  # Empty line
    school_schedule() 
    print()  # Empty line
    after_school()
    
daily_routine()
    
    