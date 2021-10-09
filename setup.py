
from distutils.core import setup
setup(
  name = 'bbfy',         # How you named your package folder (MyLib)
  packages = ['bbfy'],   # Chose the same as "name"
  version = '0.2',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'A simple API made with Python to consume Spotify API for my personal use',   # Give a short description about your library
  author = 'David Pedroza Segoviano (Bubu)',                   # Type in your name
  author_email = 'david.pedroza.segoviano@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/BubuDavid/Bubufy',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/BubuDavid/Bubufy/archive/refs/tags/v0.2.tar.gz',    # I explain this later on
  keywords = ['Python', 'SpotifyAPI'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',
          'pytz',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.6',      #Specify which pyhton versions that you want to support
  ],
)