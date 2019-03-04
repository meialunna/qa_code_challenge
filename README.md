# QA Engineer Code Challenge

* I used xpaths as element locators due to its high flexibility. I assigned them to variables to be able to reuse them and avoid duplicate code.

* For the **New post test** I created two tests - one that uploads an image from url and another one that uploads the image from the device using the image path.
 I couldn't make relative path work so I used an absolute path for the image.
 
    Although it was not necessary, I extracted all verifications into separate methods, because in the new post test both test cases shared the same verification.
     
    And even though other tests didn't, I wanted to stay consistent.
    
    To verify that the image was uploaded I used *'Upload complete'* popup as a verification anchor. 
    
    And there were no good way of verifying if the correct image was uploaded, so I was using image element within expected parent block.

* For the **Random mode test** I could've used more dynamic way of choosing the option because theoretically we should've tested all options and hardcoding the value in the test case is a bad practice. 

**Tools used** : 
* Selenium Webdriver
* Chrome
* Python

Let me know for any additional questions.
