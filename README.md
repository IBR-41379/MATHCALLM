# MATHCALLM
A persistent agent for Solving Math Problems

## Overview
This project leverages various AI and data processing libraries to build an advanced application. It includes functionalities for language processing, data manipulation, and interaction with AI models.

## Installation

To install the required libraries, run the following command:

```python
!pip install openai pandas requests chainlit autogen
```

## Configuration

The application uses a configuration file ([`appc.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fmnt%2Fc%2FProgrammingInGeneral%2FNLP%2FTest%20stuff%2Fappc.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/mnt/c/ProgrammingInGeneral/NLP/Test stuff/appc.py")) to set up the necessary parameters for the AI models. Below is an example configuration:

```python
config_list = [
    {
        "

model

": "gpt-3.5-turbo-16k",
        "api_key": "your_api_key_here"
    }
]

llm_config = {
    "timeout": 600,
    "seed": 42,
    "config_list": config_list,
}
```

Replace `"your_api_key_here"` with your actual API key.

## Usage

1. Ensure all dependencies are installed.
2. Configure the [`appc.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fmnt%2Fc%2FProgrammingInGeneral%2FNLP%2FTest%20stuff%2Fappc.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D "/mnt/c/ProgrammingInGeneral/NLP/Test stuff/appc.py") file with your API keys and desired settings.
3. Run the application using your preferred method (e.g., Jupyter Notebook, Python script).

## Libraries Used

- **openai**: For interacting with OpenAI's API.
- **pandas**: For data manipulation and analysis.
- **chainlit**: For creating interactive applications.
- **autogen**: For automatic code generation.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## Contact

For any questions or inquiries, please contact Sayandeep Dey at sayandeep369@gmail.com.

---
