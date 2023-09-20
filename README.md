BDC Dance Class Finder
This Python script, dance_class_finder.py, allows users to find dance classes offered by Broadway Dance Center (BDC) based on their preferred dance style, teacher preference, or day preference.

Motivation
I created this project with two primary motivations:

Hands-On Learning of Data Scraping
One of the main motivations behind this project was to gain hands-on experience in web scraping and data extraction. By building this script, I had the opportunity to learn how to fetch and parse data from a real website (BDC's schedule page) using Python libraries like requests and BeautifulSoup. It was a valuable learning experience that enhanced my skills in data acquisition and manipulation.

Simplifying Dance Class Scheduling
Beyond the learning aspect, this project serves a practical purpose. I intend to expand upon this initial script to create a comprehensive platform that combines schedules from various dance schools across New York City. This platform aims to simplify the process of finding dance classes without the need for cross-checking multiple sources.

Key Features (Planned)
Teacher-Based Search: Many dance instructors teach at multiple locations. Users can easily find classes by their preferred teacher, regardless of where they are teaching on a given day.

Day-Based Search: Users can search for classes by their preferred day of the week, making it convenient to plan their dance schedules.

Comprehensive Listings: The platform will aggregate schedules from different schools, providing a centralized resource for dancers in NYC.

Easy Navigation: The user interface will be intuitive, allowing dancers to quickly find classes that match their preferences.

This script represents the first step in the realization of this broader vision. As I continue to develop and expand this project, I look forward to making dance class scheduling more accessible and convenient for the dance community in NYC.

How to Use
Install the necessary libraries:

Copy code
pip install requests beautifulsoup4
Run the script:

Copy code
python dance_class_finder.py
Follow the prompts to select your preferred dance style, teacher preference (if applicable), and day preference (if applicable).

The script will then scrape BDC's schedule page for the relevant information and display the class options based on your selections.

Supported Dance Styles
Ballet
Contemporary
Hip-Hop / Street Styles
Jazz
Tap
Theater
Other (Alternative Styles)

Notes
Make sure you have an active internet connection to run this script as it fetches data from the BDC website.

The script may prompt an "Index out of range" error if you enter an invalid teacher or day preference. Please ensure your input matches the available options.

For dance styles not listed as "main styles" on the BDC website, you will be directed to the "Other (Alternative Styles)" section to find class options.

