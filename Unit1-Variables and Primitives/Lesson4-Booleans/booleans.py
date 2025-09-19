# Lesson 4: Booleans - Truth Checker

# Part 1: Creating boolean variables directly
is_sunny = True
is_raining = False
has_homework = True
# Part 2: Student information for testing
student_name = "Maria"
student_age = 17
student_grade = 85
student_gpa = 3.2
has_late_assignment = False
absent_days = 3
# Part 3: Boolean checks from comparisons - Age related
is_adult = student_age >= 18
print(f"Is Adult: {is_adult}")

# student_age = 10
is_teenager = 13 <= student_age <=19
print(f"Is Teenager: {is_teenager}")

can_drive = student_age >= 16
print(f"Can Drive: {can_drive}")

can_vote = student_age >= 18
print(f"Can Vote: {can_vote}")
# Part 4: Boolean checks from comparisons - Academic  
is_passing = student_grade >= 70
has_good_gpa = student_gpa >= 3.0
needs_parent_contact = has_late_assignment or student_grade < 70
needs_parent_contact = has_late_assignment or not(is_passing)

print(f"Needs Parent Contact: {needs_parent_contact}")
# Part 5: String-based boolean checks
has_long_name = len(student_name) > 5
print(f"Long Name: {has_long_name}")
name_starts_with_m = student_name[0] == "M"

# Part 6: Attendance and behavior

# Part 7: Complex boolean combinations
eligible_for_honors = is_passing and student_gpa >= 3.5
print(f"Eligible for Honors:{eligible_for_honors}")

model_student = is_passing and not has_late_assignment and absent_days <= 2
print(f"Model Student: {model_student}")

# Part 8: Truthiness examples
# - Try bool() with: empty string "", zero 0, non-empty string "hello", positive number

