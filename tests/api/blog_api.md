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


## TC_API_BLOG_002 = Add blog post

**Method:**  POST
**Endpoint:** /add
**Tool:** Postman

### Steps: 
1. Select POST as method and /add route as URL
2. Under Body, select x-www-form-urlencoded
3. Add "Never Finished" as "book_title", and "DG is the best!" as "content"
4. Under Script, select "Status code: code is 200" as snippet

### Expected results:
- the blog post with "Never Finished" as "book_title", and "DG is the best!" as "content" is added
- Status code: 200 ok

### Actual Results: 
- same as expected results

### Status: 
- Pass


## TC_API_BLOG_003 = Modify blog post

**Method:**  POST
**Endpoint:** /update
**Tool:** Postman

### Steps;
1. Select POST as method and /update route as URL
2. Under Body, select x-www-form-urlencoded
3. Add "Soon Finished" as "book_title", and "testing 123" as "content"
4. Under Script, select "Status code: code is 200" as snippet

### Expected results:
- the blog post is modified with "Soon Finished" as "book_title", and "testing 123" as "content"
- Status code: 200 ok

### Actual Results: 
- same as expected results

### Status: 
- Pass


## TC_API_BLOG_004 = Add comment 

**Method:**  POST
**Endpoint:** /<ent_id>/add-comment
**Tool:** Postman

### Steps;

