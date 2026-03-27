# Blog API test cases

## TC_API_BLOG_001 = Access Blog page without authorisation

**Method:** GET
**Endpoint:** /blog
**Tool:** Postman

### Steps: 
1. Select GET as method and /blog route as URL
2. Under Headers, ensure there are no cookies
3. Click Send

### Expected Results:
- Status code: 401 unauthorised
- "Unauthorised" returned

### Actual Results:
- same as expected results

### Status:
- Pass


