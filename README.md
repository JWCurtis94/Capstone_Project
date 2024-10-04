# Wheel2Wheel (W2W)  
![Screenshot 2024-10-03 235729](https://github.com/user-attachments/assets/4bb7f986-41d0-4241-b1cc-8fec820b7ee4)

## Introduction
**Wheel2Wheel** This website is designed for a Formula 1 sim racing league, where users can sign up to become drivers, check out race results and standings, and explore FIA regulations. Built using Django and Bootstrap, it focuses on managing data, engaging users, and making form submissions easy. It also embraces modern web design with a clean, minimalist look. This project was created as part of my capstone, where I focused on learning full-stack development, Python, and deployment, bringing everything together in a functional and visually appealing way.

- **View live site here**: [Wheel2Wheel](https://w2w-791ab20c5eb9.herokuapp.com/)
- **For Admin access**: [W2W Admin](https://w2w-791ab20c5eb9.herokuapp.com/admin/)
  
---

## Overview
Wheel2Wheel is a hub for F1 sim racing enthusiasts to compete, track standings, and review race results. It serves multiple functions:
- **User Registration**: Users sign up and register their profiles, which includes setting up account details.
- **Race Results & Standings**: The site dynamically updates standings and race results based on input from admin.
- **FIA Page**: Information about league rules, regulations, and the FIA code is readily accessible.
- **Reaction Game**: Registered users can have fun testing their reactions.

---

## UX - User Experience

### Design Inspiration
The inspiration for the Wheel2Wheel website came from a mix of professional F1 websites and minimalist design principles. The aim was to create a sleek, functional site where content is king, supported by subtle animations and smooth transitions.

### Color Scheme
The site features a dark, minimalist theme with pops of red, yellow, and white against a dark background. I chose this theme as it ties in with the website logo, ensuring consistency across every page.

### Typography
The primary font for the website is **Poppins**, chosen for its modern, sleek style that pairs well with the overall design of the site. **sans-serif, Arial** is used for site fallback options.

---

## Features
### User Authentication
- Users can sign up and log in using Django-allauth. The login system supports email verification and password reset functionality.

### Race Results & Standings
- Standings and race results are updated regularly. They are displayed dynamically on the website and offer a clean, responsive design for viewing across devices. This feature is currently awaiting spreadsheet data from the league, so no data is being displayed at the moment. The issue will be resolved once I receive this information from the league owner.

### Reaction Game
- Registered users can have fun testing how quick their reactions are when the light turns green.

### FIA Page
- The FIA section provides in-depth details on the league rules and regulations, ensuring all participants are aware of the standards they must follow.

### Additional Features:
- **Responsive Design**: The site is fully responsive and adapts to various screen sizes, ensuring a seamless experience across mobile, tablet, and desktop devices.
- **Smooth Navigation**: Users enjoy smooth transitions and animations, enhancing the overall browsing experience.
- **Live Stream**: Users can watch the races live directly from the website when they are being shown on YouTube.
- **Footer Icons**: The footer contains links to both the Discord channel and the YouTube channel for easy external navigation.

---

## Future Features
- **Enhanced Driver Profiles**: I plan to give each driver a more personalized experience by expanding the profiles to include detailed stats, race history, and milestones. Drivers will be able to track their progress and show off their accomplishments throughout the season.
- **Community Forum**: I want to bring our racing community closer together, so we're planning to add a forum where users can discuss race strategies, share tips, and connect with other drivers and fans. It’s all about building a place for everyone to engage and grow.
- **In-Depth Race Analytics**: Implement advanced analytics for race results, including charts and graphs to display lap times, race positions, and comparison data between drivers. This will give users deeper insights into race performance.
- **Race Highlights and Replays**: Missed a race? No worries. In the near future, you’ll be able to catch race highlights or watch full replays directly from the site, so you never miss any action.
- **Improved Driver Recruitment**: I planning to make the "Become a Driver" form even better by including more information like your availability, practice sessions, and skill levels. This will make it easier for new drivers to join the team and for existing drivers to switch between full-time and reserve spots.
- **Reaction Game Leaderboard**: The reaction game will feature a leaderboard so users can see where they rank among other members' times.

---

## Technologies & Languages Used
- **HTML5, CSS3, JavaScript**
- **Python (Django Framework)**
- **Bootstrap** Front-end framework used to enhance responsiveness and styling, making it easy to implement forms, buttons, and other components.
- **Django-allauth** Enabled secure user authentication, registration, and email verification for a smooth login experience.
- **PostgreSQL** for database management
- **Heroku** for deployment

---

## Tools & Credits
- **Gitpod & GitHub**: Version control and repository hosting.
- **Figma**: For wireframing and design mockups.
- **Adobe Color**: For choosing and testing the website’s color palette.
- **Youtube**: for guidence in video format
- **FontAwesome**: Provided icons for visual elements, enhancing interactivity and design consistency.
- **Google Fonts**: Integrated fonts like "Poppins" to provide a consistent and professional typography throughout the site.
- **Lighthouse**: Used for performance, accessibility, and SEO testing, ensuring a fast and optimized user experience.
- **JSHint & W3C Validators**: Validated JavaScript, HTML, and CSS to ensure best practices were followed and eliminate errors or warnings.
- **Slack**: Used for team communication, allowing for quick discussions and collaboration.
- **Pexels**: Provided high-quality images for backgrounds, headers, and illustrations to add visual appeal to the site.
- **ChatGPT**: For providing AI support and assistance in solving complex coding issues, debugging, and help with spelling and grammar.
- **Tutor Support**: For providing guidance throughout the development process, helping solve difficult problems and improve the quality of the project.

---

## Testing
For detailed testing information, please refer to the [TESTING.md](./TESTING.md) file. All features were tested for usability, responsiveness, and accessibility across different devices and browsers.

---

### Heroku Deployment
The project is deployed on Heroku, which is connected to the GitHub repository.
