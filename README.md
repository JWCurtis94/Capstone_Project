# Wheel2Wheel (W2W)  
![W2W Responsive Screenshot](path/to/your/screenshot.png)

## Introduction
**Wheel2Wheel** is a website designed for a Formula 1 sim racing league, where users can join as drivers, view race results and standings, and learn about FIA regulations. The project is built using Django and Bootstrap, with an emphasis on database management, user interaction, and form submission. It also showcases modern web design principles with a minimalist theme. This project was developed as part of a capstone project, focusing on learning full-stack development, UX design, and deployment.

- **View live site here**: [Wheel2Wheel](https://yourlivewebsite.com)
- **For Admin access**: [W2W Admin](https://youradminlink.com)
  
---

## Overview
Wheel2Wheel is a hub for F1 sim racing enthusiasts to compete, track standings, and review race results. It serves multiple functions:
- **User Registration**: Users sign up and register their profiles, which includes setting up account details.
- **Race Results & Standings**: The site dynamically updates standings and race results based on input from admin.
- **FIA Page**: Information about league rules, regulations, and the FIA code is readily accessible.
- **Become a Driver Form**: Registered users can apply to become drivers by submitting their racing stats and track performance images.

---

## UX - User Experience

### Design Inspiration
The inspiration for the Wheel2Wheel website came from a mix of professional F1 websites and minimalist design principles. The aim was to create a sleek, functional site where content is king, supported by subtle animations and smooth transitions.

### Color Scheme
The site features a dark, minimalist theme with pops of red, yellow, and white against a black background, embodying the thrilling and high-speed nature of F1 racing. This palette reflects the excitement and competition of the sport, while maintaining a clean, professional aesthetic.

| Section      | Color           | CSS Variable       |
|--------------|-----------------|--------------------|
| Nav Bar      | #FF0000 (Red)    | `--nav-color`      |
| Hero Section | #000000 (Black)  | `--hero-bg`        |
| Buttons      | #FFFF00 (Yellow) | `--button-color`   |

### Typography
The primary font for the website is **Montserrat**, chosen for its modern, sleek style that pairs well with the overall design of the site. **Roboto** is used for the body text, offering clean and easy readability across all devices.

---

## Features
### User Authentication
- Users can sign up and log in using Django-allauth. The login system supports email verification and password reset functionality.

### Race Results & Standings
- Standings and race results are updated regularly. These are displayed dynamically on the website and offer a clean, responsive design for viewing across devices.

### Become a Driver Form (Accessible to Logged-In Users Only)
- Registered users can apply to become drivers by submitting their EA ID, nationality, platform, and uploading Time Trial images for tracks including Monza 🇮🇹, Texas 🇺🇸, and Hungary 🇭🇺.

### FIA Page
- The FIA section provides in-depth details on the league rules and regulations, ensuring all participants are aware of the standards they must follow.

### Additional Features:
- **Responsive Design**: The site is fully responsive and adapts to various screen sizes, ensuring a seamless experience across mobile, tablet, and desktop devices.
- **Smooth Navigation**: Users enjoy smooth transitions and animations, enhancing the overall browsing experience.
- **Hero Section with Video**: The homepage features a hero section with a full-width video showcasing the racing league, drawing users in from the start.

---

## Technologies & Languages Used
- **HTML5, CSS3, JavaScript**
- **Python (Django Framework)**
- **Bootstrap**
- **Django-allauth**
- **Cloudinary** for media storage
- **PostgreSQL** for database management
- **Heroku** for deployment

---

## Tools & Programs
- **Git & GitHub**: Version control and repository hosting.
- **Figma**: For wireframing and design mockups.
- **Adobe Color**: For choosing and testing the website’s color palette.
- **WAVE**: Used to test and improve site accessibility.

---

## Testing
For detailed testing information, please refer to the [TESTING.md](./TESTING.md) file. All features were tested for usability, responsiveness, and accessibility across different devices and browsers.

---

## Deployment

### Heroku Deployment
The project is deployed on Heroku, which is connected to the GitHub repository. Every push to the main branch triggers an automatic deployment.

1. Set up a new Heroku app.
2. Configure environment variables such as `SECRET_KEY`, `DATABASE_URL`, and `CLOUDINARY_URL`.
3. Ensure the `Procfile` and `requirements.txt` are configured correctly for Heroku deployment.

### Clone Project
To clone this project, follow these steps:
1. Open the command line and navigate to the desired directory.
2. Run the command:
   ```bash
   git clone https://github.com/JWCurtis94/Capstone_Project.git
