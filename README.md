This Django application captures the following:
/* Created a customUser Model to achieve this
    setting is_active = False by default and can only be changed from admin portal
    */
1. User can register on the app (username, email, phone, password) 
2. Admin verify and approve user registration
3. admin dashboard should contain the number all users, verified user and users pending approval.



4. users should be able to login on the web using either of username or email along with the password and create task. (A task simply contains title, description and due_date)

/*
Achieved using Django Rest app and django_auth_token
*/

5. create Rest API for user to authenticate to the app using token authentication.
6. create another API endpoint that will list all the tasks created by the user.
