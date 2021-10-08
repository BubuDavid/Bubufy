<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h3 align="center">Bubufy!</h3>

  <p align="center">
    A simple API object that helps me to consume Spotify API data, and helps me with other projects.
    <br />
    <a href="https://github.com/BubuDavid/Bubufy.git"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    ·
    <a href="https://github.com/BubuDavid/Bubufy.git/issues">Report Bug</a>
    ·
    <a href="https://github.com/BubuDavid/Bubufy.git/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
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
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

I am currently working on a project based on the Spotify API consume, so I decided to create my own api object to make my life easier C: This is completely personalized to my needs and I will update it when I need it.



<!-- GETTING STARTED -->
## Getting Started

If you want to try it, you need a virtual environment with Python 3.9+ and pip installed in your computer.

### Prerequisites

As I said above you will need Python 3.9+ and pip3 installed in your computer, also you will need to install some libraries, to do that you will need to download the project and run a pip command as you will see on the installation section.

### Installation

1. Get a free API Key and Secret at [Spotify for Devs!](https://developer.spotify.com/dashboard/applications) `Strong recommendation, set a Callback URI`
2. Install the library
   ```sh
  	 pip install bbfy
	 ```
3. Store you keys and Callback URI in a .env or another kind of secret file
  ```sh
		SPOTIFY_CLIENT_ID=your actual client_id
		SPOTIFY_CLIENT_SECRET=your actual client_secret
		SPOTIFY_CALLBACK_URI=your actual callback_uri
  ```
4. You are Ready


<!-- USAGE EXAMPLES -->
## Usage

For now you can only recolect users info, the top tracks or artists for this user and the recently played tracks.And it is optimized to use with `Flask` and `Django`, I will use *Flask* on this next steps:

1. Create a bubufy instance with your respective keys:
```python
bubufy = Bubufy(client_id, client_secret, callback_uri)
```
2. Get the authorization url and go to give access to use the API
```python
auth_url = bubufy.get_auth_url()
```
You can access to this url through a button in your Flask, an example of this would be
```python
@app.route('/route_name')
def method_name():
	context = {
		'auth_url': auth_url,
	}
	return render_template('template_name.html', **context)
```
And on your HTML could be something like:
'''HTML
<a href="{{ auth_url }}">Hi! Authorize me!</a>
'''

4. Give the app access, get the code from the redirect url and set the token with the following methods:
```python
@app.route('/callback_uri')
def callback_name():
	code = require.args.get('code')
	bubufy.set_code_for_token(code)
	bubufy.set_token()
	return redirect(url_for(index)) # This for security or better UX
```
5. And now you have a functional api in the `bubufy` object, you can make some things with it, for example, let's print the username in our page (Don't forget this is a flask project):
```python
@app.route('/username')
def username_route():
	username = bubufy.get_user_data()['display_name']
	return username
```
You can make other things, I will soon update the documentation.

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/BubuDavid/Bubufy.git/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Hi there! You want to contribute! Let me now how with your PR!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

David (Bubu) - [@DBubu73](https://twitter.com/DBubu73) - david.pedroza.segoviano@gmail.com

Project Link: [https://github.com/BubuDavid/Bubufy](https://github.com/BubuDavid/Bubufy)






<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/BubuDavid/Bubufy.svg?style=for-the-badge
[contributors-url]: https://github.com/BubuDavid/Bubufy.git/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/BubuDavid/Bubufy.svg?style=for-the-badge
[forks-url]: https://github.com/BubuDavid/Bubufy.git/network/members
[stars-shield]: https://img.shields.io/github/stars/BubuDavid/Bubufy.svg?style=for-the-badge
[stars-url]: https://github.com/BubuDavid/Bubufy.git/stargazers
[issues-shield]: https://img.shields.io/github/issues/BubuDavid/Bubufy.svg?style=for-the-badge
[issues-url]: https://github.com/BubuDavid/Bubufy.git/issues
[license-shield]: https://img.shields.io/github/license/BubuDavid/Bubufy.svg?style=for-the-badge
[license-url]: https://github.com/BubuDavid/Bubufy.git/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/davidpedrozasegoviano/
[product-screenshot]: static/images/screenshot.png
