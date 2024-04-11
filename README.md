# AnimeReviewHub

## Introduction

AnimeReviewHub is a platform designed for anime enthusiasts to write and view reviews from multiple sites. It allows users to share their opinions on various anime series, edit and delete their own reviews, and discover reviews from other users.

### Links:
- **Deployed Site:** [AnimeReviewHub](https://www.animereviewhub.com)
- **Final Project Blog Article:** [AnimeReviewHub: Bringing Anime Reviews Together](https://medium.com/@maykay.fash/animereviewhub-fd82d90c9414)
- **Author(s) LinkedIn:** [Mayokun Fasasi](https://www.linkedin.com/in/mayokun-fasasi-9b239718b/)

## Installation

To run AnimeReviewHub locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/fasasimayokun/my-portfolio_project.git

2. Navigate to the project directory:
   ```bash
    cd AnimeReviewHub

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Set up the database:
    ```bash
   python manage.py migrate

5. Run the development server:
    ```bash
    python manage.py runserver
    Access the application at http://localhost:8000 in your web browser.

## Usage
Register for an account or log in if you already have one.
Explore the list of anime series available on the platform.
Click on a series to view its details and reviews from various sources.
Write your own review for a series by clicking on the "Write Review" button.
Edit or delete your reviews from the "My Reviews" section in your profile.
Contributing
Contributions to AnimeReviewHub are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request on GitHub.

## About the Project
AnimeReviewHub was inspired by the fragmented nature of anime reviews across various websites and forums. As an avid anime fan myself, I wanted to create a centralized platform where users could easily find and share reviews from multiple sources.

The technical challenge I set out to solve was creating a seamless user experience for browsing and writing reviews. I chose Django for its robustness and flexibility, and Bootstrap for its responsive design elements.

One of the key features of AnimeReviewHub is the ability for users to see not only reviews in one website to multiple wibsites and also to edit and delete their own reviews. Implementing this functionality required careful consideration of user permissions and data integrity.

Throughout the development process, I encountered challenges such as API so i had to extract data using beautiful soup and data synchronization issues. However, overcoming these obstacles allowed me to gain valuable experience in handling external data sources and using beautifulsoup.

Looking ahead, I envision expanding AnimeReviewHub with features like user recommendations, personalized content suggestions, and social sharing integrations. I'm excited to continue iterating on the project and making it even more valuable for anime enthusiasts worldwide.