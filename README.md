# Arara 📄🦜

## Summary

Welcome to Arara - your interactive PDF assistant powered by OpenAI's cutting-edge language model! ChatPDF enables you to interact with your PDFs in a whole new way, extracting information, summarizing content, and much more.

 Below is a summary of the contents you can find in this README:

- **[Getting Started 🚀](#getting-started-🚀)**: Step-by-step instructions to get you up and running with the project.
    - **[Step 1: Obtain Your API Key 🔑](#step-1-obtain-your-api-key-🔑)**: Guidance on acquiring your API key to use the project.
    - **[Step 2: Set Your API Key 🛠️](#step-2-set-your-api-key-🛠️)**: Instructions for setting your API key.
    - **[Step 3: Install Dependencies 📦](#step-3-install-dependencies-📦)**: Details on installing required dependencies.
    - **[Step 4: Launch the Application 🌟](#step-4-launch-the-application-🌟)**: Guidance on starting the application.

- **[Features ✨](#features-✨)**: A list of the key features and capabilities of the project.

- **[How to Contribute 🤝](#how-to-contribute-🤝)**: Guidelines for contributing to the project, including how to fork the repository and submit a pull request.

- **[License 📝](#license-📝)**: Information about the project's licensing under the MIT License.

Click on the links above to jump to specific sections for more detailed information. Thank you for using and supporting this project! Let us know if you have any questions or feedback.

## Getting Started 🚀

### Step 1: Obtain Your API Key 🔑

To interact with the OpenAI model, you will need an API key. Follow these steps to obtain one:

1. Visit the [OpenAI website](https://openai.com).
2. Sign up for an account if you don't already have one.
3. Navigate to the API section and follow the instructions to generate your API key.

### Step 2: Set Your API Key 🛠️

Once you have your API key, you'll need to configure the application to use it. Create a new file with the name `key.txt`, add your OpenAI API key there. For example:

```txt
sk-r7QTNcbEeRBAub8quuJAT3BlbkFJQNnPTgSaUVvGhxxxx
```

Replace the placeholder key with your actual API key. Make sure this file is in the root folder of your project and it contains only your key.

### Step 3: Install Dependencies 📦

ChatPDF requires several dependencies to run. Install them using the provided `requirements.txt` file with the following command:

```bash
pip install -r requirements.txt
```

### Step 4: Launch the Application 🌟

With your API key set and dependencies installed, you're ready to start the application. Navigate to the root folder of the directory and run:

```bash
streamlit run app.py
```

The application should now be up and running on your local server. Open your web browser and go to the address indicated by Streamlit (usually `http://localhost:8501`) to start using Arara.

## Features ✨

ChatPDF comes with a plethora of features designed to make your interaction with PDF documents as smooth as possible:

- **Information Extraction**: Pull out key details or data from your PDF files.
- **Content Summarization**: Get concise summaries of lengthy documents.
- **Q&A with your PDF**: Ask questions and get answers based on the content of your PDFs.

## How to Contribute 🤝

We welcome contributions from the community to help improve this project. If you're interested in contributing, please follow the guidelines below:

1. **Fork the repository**: Create a fork of this repository to your GitHub account.

2. **Clone your fork**: Clone your fork to your local machine using `git clone`:

    ```shell
    git clone https://github.com/your-username/your-repository.git
    ```

3. **Create a branch**: Create a new branch for your contribution:

    ```shell
    git checkout -b your-branch-name
    ```

4. **Make your changes**: Implement your desired changes on your branch.

5. **Commit your changes**: Commit your changes with a descriptive commit message:

    ```shell
    git commit -m "Describe your changes"
    ```

6. **Push your changes**: Push your branch to your forked repository:

    ```shell
    git push origin your-branch-name
    ```

7. **Submit a pull request**: Once your changes are ready for review, open a pull request (PR) on GitHub. Include a clear description of your changes and any relevant information for the maintainers to review.

8. **Follow the coding standards and guidelines**: Ensure your code follows any coding standards and guidelines specified in the project.

9. **Participate in the review process**: Be open to feedback from maintainers and other contributors. Respond to comments and make adjustments to your code as needed.

10. **Stay respectful**: We aim to foster a welcoming and inclusive environment. Please be respectful in all interactions with other contributors and maintainers.

Thank you for your interest in contributing! We appreciate your time and effort in helping to improve this project. If you have any questions, feel free to reach out to the repository maintainers.

## License 📝

This project is licensed under the MIT License. This means you are free to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software, subject to the following conditions:

    The software is provided "as is," without any express or implied warranty of any kind.
    You must include the original copyright notice and the permission notice from the MIT License in all copies or substantial portions of the software.

You can find the full text of the MIT License in the LICENSE file in this repository. Please read the file for the complete terms and conditions. If you have any questions or concerns about the license, feel free to contact the repository maintainer.
