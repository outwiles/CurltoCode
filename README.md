<div align="center">
<img src="assets/logo.png" alt="CurlToCode" width="420">
<h1>CurlToCode</h1>
<p>Universal cURL-to-code converter</p>
</div>

CurlToCode converts a cURL command into ready-to-use request code for multiple programming languages and request formats. It parses the request method, URL, headers, cookies, authentication, form data, and body, then generates an equivalent representation.

## Features

- Interactive terminal interface
- 32 output targets
- cURL method and URL parsing
- Header and request-body handling
- Basic cookie and authentication handling
- Cross-platform Python implementation
- Works locally without a hosted service

## Output targets

1. Python Requests
2. Python http.client
3. Python Requests
4. Go net/http
5. Ruby Net::HTTP
6. PHP Guzzle
7. PHP cURL
8. C# HttpClient
9. Java HttpClient
10. Node.js http
11. JavaScript Axios
12. JavaScript Fetch
13. TypeScript Fetch
14. Python aiohttp
15. Elixir Req
16. JavaScript jQuery
17. Java OkHttp
18. C# RestSharp
19. C++ libcurl
20. C libcurl
21. Rust reqwest
22. Kotlin OkHttp
23. Swift URLSession
24. Dart http
25. R httr2
26. Lua LuaSocket
27. Perl HTTP::Tiny
28. PowerShell
29. Wget
30. Bash curl
31. Raw HTTP
32. JSON

## Requirements

- Python 3.9 or newer
- pip
- Git is recommended for cloning the repository

## Installation

### Windows

```powershell
git clone <YOUR_REPOSITORY_URL>
cd CurlToCode
py -m pip install -r requirements.txt
py main.py
```

### Linux

```bash
git clone <YOUR_REPOSITORY_URL>
cd CurlToCode
python3 -m pip install -r requirements.txt
python3 main.py
```

### macOS

```bash
git clone <YOUR_REPOSITORY_URL>
cd CurlToCode
python3 -m pip install -r requirements.txt
python3 main.py
```

### Termux

```bash
pkg update
pkg install python git
git clone <YOUR_REPOSITORY_URL>
cd CurlToCode
python -m pip install -r requirements.txt
python main.py
```

### Android / PyDroid

Install Python 3 and pip through your Python environment, copy or clone the project, open its directory, install the requirements, and run `main.py`.

```bash
python -m pip install -r requirements.txt
python main.py
```

If your Android Python environment does not provide a normal terminal, the converter logic still works as a standard Python module, while terminal-specific banner rendering depends on terminal support.

## Usage

Start the program:

```bash
python main.py
```

Choose an output target, then paste a cURL command such as:

```bash
curl 'https://example.com/api' -H 'Accept: application/json' -H 'Authorization: Bearer TOKEN' -d 'name=Aashu'
```

The generated code is printed directly in the terminal.

## How it works

1. The parser tokenizes the supplied cURL command.
2. Request options are normalized into one internal request structure.
3. The selected generator converts that structure into the requested language or format.
4. The result is printed locally.

CurlToCode does not need to send the original request to a remote conversion server.

## Project structure

```text
CurlToCode/
├── assets/
│   └── logo.png
├── curl_to_code/
│   ├── __init__.py
│   ├── core.py
│   └── generators.py
├── main.py
├── requirements.txt
├── README.md
└── LICENSE
```

## Troubleshooting

### cfonts is missing

```bash
python -m pip install -r requirements.txt
```

On macOS or Linux:

```bash
python3 -m pip install -r requirements.txt
```

### Python is not recognized on Windows

Try:

```powershell
py --version
```

Then:

```powershell
py -m pip install -r requirements.txt
py main.py
```

### Terminal styling looks different

The converter remains functional without relying on terminal styling. Different terminals may render ANSI escape sequences and cfonts output differently.

## License

This project is released under the MIT License. See `LICENSE` for the complete license text.

## Credits

Created and maintained by **Aashu**.
