TOEFL_timer
=======
A simple pure python script of a timer for TOEFL speaking/writing preparation.

# Usage
py toefl_timer.py ([time by sec] | [question type][question number][optional:special time code])...

1.Question type
type     |  code
---------|:--------:
Speaking | s
Writing  | w

2.Question number
type                  | value range
----------------------|:-------------:
Speaking              |   1-6
Integrated Writing    |   1
Independent Writing   |   2

3.Special time code
Reading time for integrated problems : 'r'
Skip preparation time : 's'

# Example
* Simple timer for 30 seconds
> `py toefl_timer.py 30`
* Speaking problem no.1
> `py toefl_timer.py s1`
* Speaking problem no.1 without preparation time (useful for group studying)
> `py toefl_timer.py s1s`
* Integrated writing
> `py toefl_timer.py w2`
* Multiple timer in a row (useful for group studying)
> `py toefl_timer.py s1 s1s s1s s1s`

# Raw-data : time limits of TOEFL speaking/writing in problem numbers

Number of problem  |Type name of problem| Reading time | Preparation time | Answering time
-------------------|--------------------|:------------:|:----------------:|:---------------:
Speaking 1-2       |Independent speaking| none         | 15 seconds       | 45 seconds
Speaking 3-4       |Integrated speaking | 50 seconds   | 30 seconds       | 60 seconds
Speaking 5-6       |Integrated speaking | none         | 20 seconds       | 60 seconds
Writing 1          |Integrated writing  | 3 minutes    | none             | 20 minutes
Writing 2          |Independent writing | none         | none             | 30 minutes

Good luck with your test.