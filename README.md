# Codeforces Submission Tool

This project provides an automated tool for submitting solutions to Codeforces problems using SeleniumBase.

## Features

- Automated login to Codeforces
- Submission of solutions to specified problems
- Configurable language selection
- Retrieval of submission results

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/asibhossen897/cf-submit.git
   cd cf-submit
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Codeforces credentials:
   ```
   CODEFORCES_USERNAME=your_username
   CODEFORCES_PASSWORD=your_password
   ```

## Usage

To submit a solution:

```
python cf-submit.py
```

This script will automatically:
1. Log in to Codeforces
2. Navigate to the specified problem
3. Submit the solution from the `solutions/main.cpp` file
4. Wait for and display the submission result

## Configuration

- `config.py`: Contains various configuration options, including language IDs and URLs.
- `utils.py`: Utility functions for file path management.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. Or discuss in the issues what you want to add. Also report any bugs you find.

## License

This project is open source and available under the [MIT License](LICENSE).

## Disclaimer

This tool is not officially affiliated with or endorsed by Codeforces. Use it responsibly and in accordance with Codeforces' terms of service.