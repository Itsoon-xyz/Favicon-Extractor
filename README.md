# Favicon extractor

## Compatibility :

### Parse html :

```html
<link rel="icon" href="path/to/icon.png" />

<link rel="shortcut icon" href="path/to/icon.png" />

<link rel="apple-touch-icon" href="path/to/icon.png" />

<link rel="apple-touch-icon-precomposed" href="path/to/icon.png" />

<link rel="fluid-icon" href="path/to/icon.png" />

<link rel="mask-icon" href="path/to/icon.png" />

<meta name="msapplication-TileImage" content="path/to/icon.png" />

<meta name="msapplication-square70x70logo" content="path/to/icon.png" />

<meta name="msapplication-square150x150logo" content="path/to/icon.png" />

<meta name="msapplication-square310x310logo" content="path/to/icon.png" />

<meta name="msapplication-wide310x150logo" content="path/to/icon.png" />
```

### Url search :

```txt
/favicon.ico
```

<meta name="msapplication-config" content="path/to/ieconfig.xml" />

<link rel="manifest" href="path/to/manifest.webmanifest" />

## Installation

### 1. Creating the virtual environment

```bash
virtualenv .venv
```

### 2. Activate the virtual environment created

```bash
source .venv/bin/activate
```

### 3. Install geckodriver

#### Arch linux

```bash
yay -S geckodriver
```

###### see [mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases)

### 4. Set up dependencies

```bash
pip install -r requirements.txt
```

## To do

- [ ] check_url more tests with different urls

add this to url search :

- `/apple-touch-icon.png`

- `/apple-touch-icon-precomposed.png`

- `/apple-touch-icon-57x57-precomposed.png`

- `/apple-touch-icon-57x57.png`

- `/apple-touch-icon-72x72-precomposed.png`

- `/apple-touch-icon-72x72.png`

- `/apple-touch-icon-114x114-precomposed.png`

- `/apple-touch-icon-114x114.png`

- `/apple-touch-icon-120x120-precomposed.png`

- `/apple-touch-icon-120x120.png`

- `/apple-touch-icon-144x144-precomposed.png`

- `/apple-touch-icon-144x144.png`

- `/apple-touch-icon-152x152-precomposed.png`

- `/apple-touch-icon-152x152.png`

- `/apple-touch-icon-180x180-precomposed.png`

- `/apple-touch-icon-180x180.png`
