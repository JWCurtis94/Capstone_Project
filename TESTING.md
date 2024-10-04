## Validation

### HTML Validation

For my HTML files I have used HTML W3C Validator to validate all of my HTML files.

I had to take a different approach to validate my HTML for this project since most of my pages are built using Jinja syntax, like {% extends "base.html" %} and {{ form|crispy }}, and many require user authentication. Using the website's URL with an HTML validator would throw errors due to the Jinja tags, so I followed this approach for every page:

- Using the deployed Heroku app link, I navigated to each individual page.
- Once on each page, I right-clicked and selected "View Page Source."
- This displayed the complete HTML code for the deployed page, which I copied by pressing CTRL+A - CTRL+C
- I then pasted the copied code into the W3C Validator’s validate by input option.
- After checking for errors and warnings, I fixed any issues, revalidated the code by repeating the process, and recorded the results.

![Screenshot 2024-10-03 142008](https://github.com/user-attachments/assets/c7655078-24a5-4eb3-88ca-0487cbe1673c)
![Screenshot 2024-10-03 141017](https://github.com/user-attachments/assets/3fe94e34-47d9-40b9-9556-043f6c9cc1ef)
![Screenshot 2024-10-03 140622](https://github.com/user-attachments/assets/d4be82c6-0a36-4184-843c-c0b2e51d62c9)
![Screenshot 2024-10-03 140329](https://github.com/user-attachments/assets/b668fcc8-d667-4f73-853e-fe29492f32f1)
![Screenshot 2024-10-03 140246](https://github.com/user-attachments/assets/24ef60d5-8389-4853-8594-adbc4b4887ab)
![Screenshot 2024-10-03 140157](https://github.com/user-attachments/assets/07573433-56fe-4648-b33a-e41f7353f468)
![Screenshot 2024-10-03 135848](https://github.com/user-attachments/assets/77e195df-c834-4032-a438-68cd2fc3e169)
![Screenshot 2024-10-03 134619](https://github.com/user-attachments/assets/323ed821-fde1-4718-bf18-c55ff2bc6c36)

All HTML pages were validated and received a 'No errors or warning to show' result as shown above.

### JavaScript Validation

I used JSHint to validate the JavaScript code I added to the project. You can see the results of the testing in the images below.

![Screenshot 2024-10-03 230830](https://github.com/user-attachments/assets/9fd45c09-bcde-4136-8b87-4965941b74e4)
![Screenshot 2024-10-03 230752](https://github.com/user-attachments/assets/0754b8d4-9dc2-4a57-a394-4b88353f42e2)
![Screenshot 2024-10-03 230634](https://github.com/user-attachments/assets/b9a6815d-ec70-4840-ba3c-6fabb02a12f1)
![Screenshot 2024-10-03 230545](https://github.com/user-attachments/assets/13915b77-dd17-4302-92a5-43f92f3d4c5e)

### Python Validation

I used the CI Python Linter to validate the Python files that I created or edited. This validation ensured that my code adhered to PEP8 standards. You can find the results in the images below.

![Screenshot 2024-10-03 231628](https://github.com/user-attachments/assets/5d29ef11-d87e-4d2a-babd-68f12b24375d)
![Screenshot 2024-10-03 231256](https://github.com/user-attachments/assets/ff8df2f4-3e39-4d2e-a147-892aedf69a19)
![Screenshot 2024-10-03 233930](https://github.com/user-attachments/assets/4cefed22-b45b-4fd1-b574-ed23408d591e)
![Screenshot 2024-10-03 233536](https://github.com/user-attachments/assets/802d28ff-a84b-44a7-93fe-54ad14291485)
![Screenshot 2024-10-03 233420](https://github.com/user-attachments/assets/f25e9235-2651-46d1-8af2-d77bacecfd9f)
![Screenshot 2024-10-03 232306](https://github.com/user-attachments/assets/54210ec3-ef92-4322-8b0f-f3d07bb540f5)
![Screenshot 2024-10-03 232211](https://github.com/user-attachments/assets/6248e04b-2f73-4e90-9ba8-398b34f3b05c)
![Screenshot 2024-10-03 232116](https://github.com/user-attachments/assets/db79ef6a-6f57-4c34-a298-f451875500af)
![Screenshot 2024-10-03 232018](https://github.com/user-attachments/assets/3d5cda50-1541-461d-9e20-18393c450979)
![Screenshot 2024-10-03 231833](https://github.com/user-attachments/assets/02f2b85e-3c85-4ce3-912c-95ef15e494dd)
![Screenshot 2024-10-03 231750](https://github.com/user-attachments/assets/f1355577-6ec9-4395-93d7-e74ebaedde4e)

### CSS Validation 

I used the W3C CSS Validator to check my CSS file. This helped ensure there were no errors or redundant lines of code. You can see the results in the images below.

![Screenshot 2024-10-03 150102](https://github.com/user-attachments/assets/21fc2b3a-2ab8-4871-89eb-47de8982b9e6)
![Screenshot 2024-10-03 144958](https://github.com/user-attachments/assets/eb3e6c5a-c4be-4e63-987f-a4e6dd0af847)
![Screenshot 2024-10-03 142227](https://github.com/user-attachments/assets/2158746f-85ff-4f4b-806d-c412d487035e)

### Lighthouse Scores

I used Lighthouse testing to evaluate the overall performance of my website. I made the decision to run the tests with all my browser extensions active and without using incognito mode. My goal was to get the most realistic user experience possible. Sure, I could have disabled extensions, closed all tabs, and achieved a higher score, but that wouldn’t reflect what a typical user might experience. You can see the results in the images below.

![Screenshot 2024-10-03 132801](https://github.com/user-attachments/assets/a8cbc56b-7116-4275-b4f2-5a53a9b1ab42)
![Screenshot 2024-10-03 132710](https://github.com/user-attachments/assets/e17b101a-7ece-4591-935c-c738007364cf)
![Screenshot 2024-10-03 132658](https://github.com/user-attachments/assets/890e7198-ab7c-4e65-b38d-14084bf71a12)
![Screenshot 2024-10-03 132809](https://github.com/user-attachments/assets/4584cd0a-c84e-42da-959c-910f00584697)

### Dev Tools/Real World Device Testing

I used Google Dev Tools to test the responsiveness of the site. All features displayed correctly across the different devices I tested. However, there were times when the page would load zoomed in or out on the simulated device. In those cases, I just clicked the 'W2W' logo to refresh the page, and everything would return to normal.

### Bugs  
  
As this was my first Django/Database project, most of the bugs I encountered were learning and teething issues. The bugs listed below are the ones that took me the longest to resolve or required assistance from Tutor Support, Google, YouTube, or AI tools like ChatGPT and Perplexity.

***1. Login/Registration Redirect Confusion***
What happened: After logging in or registering, some users found themselves on the wrong page or stuck in a loop.

How I fixed it: I updated the redirect paths so now, after logging in or registering, you’ll land exactly where you’re supposed to – whether that's the homepage or your dashboard.

***2. Navigation Bar Issues on Mobile***
What happened: On mobile, the navigation bar wasn’t always behaving, making it hard to access certain pages or links.

How I fixed it: I fine-tuned the CSS and JavaScript to make sure the nav bar works flawlessly on all devices, especially mobile. The 'Become A Driver' tab now only shows for logged-in users, as it should.

***3. Content Overlap on FIA Page***
What happened: On smaller screens, the text on the FIA page sometimes overlapped, making it hard to read the rules.

How I fixed it: I adjusted the layout with media queries so the text stays clear and readable on all screen sizes.
