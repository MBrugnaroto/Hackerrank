### Plus Minus

**Task**

Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

**Example**

- s = '12:01:00PM'
Return '12:01:00'.

- s = '12:01:00AM'
Return '00:01:00'.

**Function Description**

timeConversion has the following parameter(s):

string s: a time in 12 hour format

**Input Format**

A single string  that represents a time in 12-hour clock format (i.e.: hh:mm:ssAM or hh:mm:ssPM).

**Constraints**

All input times are valid

**Output Format**

A single string  that represents a time in 24-hour clock format (i.e.: hh:mm:ss or hh:mm:ss).