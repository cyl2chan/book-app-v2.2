# Login API test cases

## TC_API_LOGIN_001 = Login with valid credentials

**Method:** POST
**Endpoint:** /login
**Tool:** Postman

### Steps:
1. Select POST as method and /login route as URL
2. In Body, select x-www-form-urlencoded
3. Enter "student@ryerson.ca" as "email"
4. Enter "secret" as "password"
5. Click Send

### Expected Results:
- Status code: 200
- Library Page returned
- Session cookie created

### Actual Results:
- same as expected results

### Status: 
- Pass


