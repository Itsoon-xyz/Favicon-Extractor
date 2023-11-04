# Favicon extractor

### Installation

virtualenv .venv
source .venv/bin/activate
yay -S geckodriver

## To-do

- ~~"invalid url" error~~ corrected by bypassing 403 html status code
  - ~~https://chinaphonearena.com ==> invalid url cloudfare protection~~
  - ~~https://codepen.io ==> invalid url just not working~~
  - ~~https://tellonym.me ==> invalid url~~
  - ~~https://twitter.com ==> invalid url~~
  - [x] ~~to much time to checkUrl~~ fix
- [x] ~~to much time to https://caringbridge.org~~ fixed by waiting times
  - [x] ~~https://nimble.com ==> Message: Navigation timed out after 300000 ms~~
- [x] ~~"No connection adapters were found for 'data:,'"~~ fixed by Explicit Waits selenium
