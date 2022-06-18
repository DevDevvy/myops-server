<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/devdevvy/repo_name">
    <img src="public/logo.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">MyOps</h3>

  <p align="center">
    Personal Tracking and Data Visualization for the professional who wants to optimize life and work. See how your sleep, exercise and other factors affect your productivity and mood.
    <br />
    <a href="https://github.com/devdevvy/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/devdevvy/repo_name">View Demo</a>
    ·
    <a href="https://github.com/devdevvy/repo_name/issues">Report Bug</a>
    ·
    <a href="https://github.com/devdevvy/repo_name/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

   In an increasingly isolating digital world, the need to keep tabs on our personal well being is becoming ever more prevalent. 
    <br/>
    This holds especially true for professionals like software developers who are often workig in a solitary environment. 
    MyOps allows users to track their own personal data in order to identify and track trends related to sleep, mood, and productivity among other things. 
    The hope is that through recognizing and identifying personal trends and patterns, 
    it will empower the user to identify negative trends in order to correct them, 
    or identify positive correlations in order to maximize personal health and perfomance. 
<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* [React.js](https://reactjs.org/)
* [Chart.js](https://www.chartjs.org/)
* [Django](https://www.djangoproject.com/)
* [Material UI](https://mui.com/)


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* npm
  ```sh
  npm install npm@latest -g
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/devdevvy/myops-server.git
   ```
2. Create virtual environment
   ```sh
   pipenv shell
   ```
3. Install requirements
   ```sh
   pipenv install -r requirements.txt
   ```
4. Create .env file in project root for secret key 
5. Run command for random secret key and paste key into .env file
  ```sh
   python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
   ```
6. Run makemigrations, migrate, and loaddata to set up server models and dummy data
7. Clone/Open [React client](github.com/devdevvy/myops-client)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Record and track personal performance and data
- [ ] Create tips related to moods (can be shared publically)
- [ ] Recorded datapoints
    - [ ] Sleep quality
    - [ ] Mood
    - [ ] Self-talk
    - [ ] Coping strategies
    - [ ] Productivity
    - [ ] And times related to:
        - [ ] Sleep
        - [ ] Work
        - [ ] Break
        - [ ] Learning
        - [ ] Exercise
        - [ ] Family
- [ ] Record personal journals for further data
- [ ] Change viewed timeline from 1 and 2 weeks, to months, up to a year's worth of data points
- [ ] Favorite other user tips to save in your home view
- [ ] Sort tips by associated mood
See the [open issues](https://github.com/devdevvy/myops-server/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Randall Thomas- [@twitter_handle](https://twitter.com/twitter_handle) - randallthomasmusic@gmail.com

Project Link: [https://github.com/devdevvy/myops-server](https://github.com/devdevvy/myops-server)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments
Dedicated...
* To my family for seeing more in me
* To my wife for supporting me
* To my teachers for believing in me
* To my peers for encouraging me
* To my friends for helping me
* To my dog for keeping me company the whole time


<p align="right">(<a href="#top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/devdevvy/myops-server.svg?style=for-the-badge
[contributors-url]: https://github.com/devdevvy/myops-server/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/devdevvy/myops-server.svg?style=for-the-badge
[forks-url]: https://github.com/devdevvy/myops-server/network/members
[stars-shield]: https://img.shields.io/github/stars/devdevvy/myops-server.svg?style=for-the-badge
[stars-url]: https://github.com/devdevvy/myops-server/stargazers
[issues-shield]: https://img.shields.io/github/issues/devdevvy/myops-server.svg?style=for-the-badge
[issues-url]: https://github.com/devdevvy/myops-server/issues
[license-shield]: https://img.shields.io/github/license/devdevvy/myops-server.svg?style=for-the-badge
[license-url]: https://github.com/devdevvy/myops-server/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/randall-thomas-music
[product-screenshot]: images/screenshot.png
