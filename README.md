# swift-req

`swift-req` is a simple command-line HTTP client for making fast and efficient API requests with minimal setup. It allows you to send GET, POST, PUT, DELETE, and PATCH requests with customizable headers, data, and verbosity.

## Features
- Support for HTTP methods: GET, POST, PUT, DELETE, PATCH.
- Easily add headers using -H.
- Send data with POST/PUT/PATCH requests using -d for JSON.
- Save response to a file with -o.
- Enable verbose output to get detailed information about the response.

## Quick example
```bash
swift-req -u https://www.example.com/api/data -m GET -v -o output.txt
```

## Installation

### Using python

1) **Clone or download the repository.**

2) **Install dependencies**
```bash
pip install -r requirements.txt
```

3) **Now you can run the application with python:**
```bash
python main.py
```

### Global installation (Windows)

Installing `swift-req` Globally
To use swift-req as a command in the terminal, you can install it globally. The following steps allow you to run swift-req from any location in your terminal without needing to specify python.

1) **Install Dependecies:**
- Open your terminal and navigate to the directory containing `requirements.txt`.
- Run the following command:
```bash
pip install -r requirements.txt
```

2) **Create a Directory**
- You can create a directory (folder) to store your swift-req files. For example:
```bash
mkdir C:\Users\yourusername\swift-req
```

- Move the scripts in this directory.

3) **Create a Batch file:**

- Open a text editor (e.g., Notepad).
- Paste the following content, replacing `C:\path\to\your\swift-req` with the actual path to your swift-req directory:

```bash
@echo off
python "C:\path\to\your\swift-req\main.py" %*
```

- Save the file as `swift-req.bat` in the same directory as your scripts.

4) **Add Directory to PATH:**
- Search for "Edit the system environment variables" in your Windows search bar.
- Click "Edit" under "System Properties".
- Under "System variables", find the "Path" variable and click "Edit".
- Click "New" and paste the path to your swift-req directory (e.g., C:\Users\yourusername\swift-req).
- Click "OK" on all open windows to save the changes.

## Documentation

### Syntax
```bash
swift-req -u <URL> [OPTIONS]
```

- `<URL>`: The address (URL) of the API endpoint you want to interact with.
- `[OPTIONS]`: Optional arguments to customize your request.

#### Simplest command
The most basic way to use swift-req is with just the URL of the API endpoint:
```bash
swift-req -u <URL>
```
This command will send a GET request to the specified URL and display the response content directly in your terminal.

##### Example:
```bash
swift-req -u https://jsonplaceholder.typicode.com/todos/1
```
**Note**: This basic command doesn't provide details about the response, such as status code or headers.

#### Using Additional Options

- **-m \<METHOD>:** Specify the HTTP method (GET, POST, PUT, DELETE, PATCH) for your request. Defaults to GET if not provided.

```bash
swift-req -u https://example.com -m DELETE
```

- **-H \<HEADERS>:** Add custom headers to your request. Useful for authentication or specifying data formats.

```bash
swift-req -u https://example.com -m POST -H "Authorization: Barer mysecrettoken" -H "Content-Type: application/json"
```

- **-d \<DATA>:** Send data (for POST, PUT, and PATCH methods) as a JSON string.

```bash
swift-req -u https://example.com -m POST -d '{\"data\": \"Hello world\"'
```

- **-o \<OUTPUT_FILE>:** Save the response to a file.

```bash
swift-req -u https://example.com -o response.txt
```

- **-v \<VERBOSE>:** Enable verbose output to get detailed information about the response, including status code, headers, and response body.

