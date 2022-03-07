
Milestone 3

Emily Carpenter

Ryan Young

Guanbo Bian	

Team #2 - BIT 


FIRST TEST: 

Use case name

    Verify that we don’t return courses that the user has already taken

Description

    Test the input list against the return list 

Pre-conditions

    User has submitted classes that they have already taken 

Test steps

    1. Navigate to course list page

    2. Select list of classes taken

    3. Click submit button  

    4. Return results page 

    5. Verify that there are no duplicates in the input list and the output list. 

Expected result

    User should be shown classes they have no taken previously 

Actual result

    If the user has taken 1300, it returns 1300. 

Status (Pass/Fail)

    Fail

Post-conditions

    User has selects courses that they have already taken and submits them properly. 





SECOND TEST:

Use case name

    Verify that is you select a course for a review that it will return the right   course with the correct review

Description

    Test the reviews page on our Flask site

Pre-conditions

    User has to select the course(s) they want to a review on

Test steps

    1. Navigate to reviews page

    2. Select the box of the class they want a review from

    3. Click submit

Expected result

    User should see the reviews for all the courses that they selected

Actual result

    The user will see reviews for the courses that they selected

Status (Pass/Fail)

    Pass

Notes

    N/A

Post-conditions

    User has selects courses that they want reviews on and now has the requested reviews





THIRD TEST: 

Use case name

    Verify that we return a course that the user is eligible to take. 

Description

    Once a user has submitted the list of courses they have taken, we need to make sure that the courses that are returned/suggested to them are classes that they are actually eligible to take. 

Pre-conditions

    The user has submitted classes that they have already taken or are currently taking. 

Test steps

    1. Navigate to course list page

    2. Select list of classes taken

    3. Click submit button  

    4. Return results page 

    5. Check courses returned. 

Expected result

    The user should be shown classes they have not taken previously and are eligible to take now. 

Actual result

    If 1300, 2824, 3022, 3702, and 2820 have been taken, it returns 2270.  

Status (Pass/Fail)

    Pass

Post-conditions

    User has selects courses that they have already taken and submits them properly. 




