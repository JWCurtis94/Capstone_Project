# 🏎️ W2W F1 Sim Racing League

## 🚦 About

**W2W (Wheel-to-Wheel) F1 Sim Racing League** is a comprehensive web application developed using Django, designed to manage and organize virtual Formula 1 simulation racing events. The platform caters to F1 sim racing enthusiasts, offering features like registration, live standings, race results, and user profiles. Through dynamic features and an intuitive user experience, the website aims to provide a fully immersive and engaging space for racers to track performance, join races, and engage with the W2W community.

---

## 🎨 UX Design

The design focuses on a **minimalist** and **dark-themed** aesthetic, emphasizing simplicity and ease of navigation. Inspired by the energy and colors of F1 racing, the color scheme is a bold combination of **red**, **yellow**, **white**, and **black**. Key features include:

- **Hero video** on the homepage to engage users immediately.
- **Smooth scrolling** for seamless transitions between sections.
- **Elegant typography** for clarity and aesthetics.
- **Consistent navigation bar** and **footer** with Discord and YouTube icons for social engagement.

---

## 🚀 Features

- **User Authentication**: Secure registration, login, and email confirmation using Django-Allauth.
- **Profile Management**: Users can update personal information, including email and username.
- **Race Standings**: Dynamic standings page that reflects real-time race results and rankings.
- **Incident Reporting**: Allows users to submit tickets for race incidents, handled through custom models like `IncidentTicket`.
- **FIA Information Page**: Displays the official W2W racing rules and regulations.
- **Responsive Design**: Optimized for various devices, including mobile and desktop.
- **Media Uploads**: Integrated media upload system for race screenshots and content sharing.
- **Smooth Animations**: Subtle animations and transitions improve interactivity and the user experience.

---

## 🛠️ Technologies Used

- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript (with modern CSS features for animations)
- **Task Queue**: Celery with Redis (for managing notifications and background tasks)
- **File Storage**: Django FileField for handling media uploads
- **Frontend Libraries**: Bootstrap for responsiveness, Font Awesome for icons

---

## 🐛 Bug Fixes and Issues Solved

- **Registration Bugs**: Fixed issues with form validation and email confirmation not triggering on specific devices.
- **CSS Responsiveness**: Corrected display issues on smaller screens where elements overlapped.
- **Race Standings Calculation**: Addressed a bug in race standings where ties were not handled correctly.
- **Dynamic URLs**: Mapped URLs for the 'About' page and corrected it to link to the correct view.
- **Incident Ticket Submission**: Solved a problem where users were unable to submit incident reports due to model field errors.
- **Smooth Animations**: Improved the performance of scroll-based animations, especially on mobile browsers.
- **Database Migrations**: Fixed inconsistencies with PostgreSQL migrations related to the `RaceResult` and `IncidentTicket` models.

---

## 🔧 Testing

The project has undergone extensive testing for:

- **Responsiveness**: Verified across multiple devices (desktop, tablet, mobile).
- **Browser Compatibility**: Tested on Chrome, Firefox, and Safari.
- **Form Validation**: Ensured proper validation for registration and login forms.
- **Unit Testing**: Performed unit tests for critical functionalities (race result calculations, user authentication, etc.).
- **Performance**: Improved load times with image optimization and lazy loading for media-heavy sections (tested with Google Lighthouse).

---

## 📚 User Stories

The project development followed an agile approach, with the GitHub Project Board tracking tasks and milestones. User stories were focused on creating an immersive and easy-to-use platform for sim racing enthusiasts, prioritizing the following features:

- Users should be able to **register and verify accounts** easily.
- Standings should reflect **real-time race results** with minimal delay.
- The website must be **easy to navigate** on mobile devices.
- A robust incident reporting system should be in place to ensure fairness.

Below are some screenshots showing the project's progress:
![Screenshot 2024-09-16 133041](https://github.com/user-attachments/assets/9c40bf9b-6e04-4efa-8d1c-d735fa1c5bdb)
![Screenshot 2024-09-16 133820](https://github.com/user-attachments/assets/c4f7b45d-d369-4c4b-b8f4-f1d017a13795)

---

## ✈️ Usage

- **Homepage**: Provides an introduction to the W2W league, featuring a F1 reaction test game and quick links to key sections.
- **User Registration**: New users can sign up with fields like username, email, date of birth, and password confirmation, with email verification.
- **Standings**: Displays real-time race results and driver standings.
- **Login/Profile**: Users can log in to view and manage their profiles, update information, and track personal stats.
- **FIA Page**: Contains league rules and FIA regulatory information for participants.
- **Live Stream**: A page that allows users to watch the races live, directly from the website.

---

## 🔮 Future Features

- **Live Race Tracking**: Integrating a live tracking feature to display ongoing race progress.
- **Enhanced User Profiles**: Allow users to upload avatars and customize personal bios.
- **Race Calendar**: A comprehensive race scheduling feature, complete with notifications for upcoming events.
- **Advanced Analytics**: Detailed performance breakdowns, race-by-race analytics, and data visualization for drivers.

---

## 💻 Resources

- **Balsamiq**: Used for wireframing during the initial design phase.
- **Git & GitHub**: Git for version control and GitHub for repository hosting and collaboration.
- **Google Fonts**: Customized fonts for a professional look.
- **Google Chrome Dev Tools**: For inspecting and troubleshooting design and layout issues.
- **Google Lighthouse**: Ensured high performance, accessibility, and best practices.
- **Favicon Generator**: For website branding.
- **W3C Validators**: Ensured valid HTML and CSS across the project.
- **Stack Overflow**: For resolving various technical queries.
- **Pexels**: Sourced royalty-free images.
- **ChatGPT**: Assisted in troubleshooting bugs, providing guidance on complex functionality and spelling.

## 📝 Footer Note

- **High Injection Count During Project**: During this project, I encountered unusually high injection counts when committing changes, reaching up to 40,000 injections at times. Initially, both my tutors and I were unsure of the cause. Toward the end of the project, we discovered that the issue was related to an extra static folder containing a large number of files and subdirectories, which I had mistakenly assumed was generated by Django. After identifying and removing the unnecessary folder, the injection counts returned to normal.
