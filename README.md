# Chat-with-multitable-DB
Chat with relational database made with using Mixtral through Groq API.


# Python Chat with Multiple Table Database

This Python application enables users to interact with a database using a chat interface. It utilizes a combination of Streamlit for the frontend and various Python libraries for backend operations.

## Requirements

Ensure you have the following libraries installed:

- `langchain_community` for database operations
- `langchain_groq` for querying the database
- `langchain` for language processing tasks
- `dotenv` for managing environment variables
- `streamlit` for creating the frontend interface

You can install these libraries using pip:

```bash
pip install langchain_community langchain_groq langchain python-dotenv streamlit
```

## Usage

### Set Up Environment Variables

1. Create a `.env` file in your project directory.

2. Open the `.env` file and add your GROQ API key:

    ```env
    GROQ_API_KEY=your_api_key_here
    ```

### Run the Application

Execute the Python script containing your application code:

```bash
streamlit run app.py
```

## Interact with the Chat Interface

Once the application is running, you can interact with the chat interface. The chatbot will require the database name or you can connect your db in the code directly and disable that option.

## Functionality

- **Chat Interface**: Users can communicate with the application through a simple chat interface provided by Streamlit.

- **Database Querying**: The application interacts with a database using the provided GROQ API key. Users can ask questions or perform operations on the database through natural language queries.

- **Multiple Table Database Support**: The application is designed to work with databases containing multiple tables. It can handle complex queries involving multiple tables and provide meaningful results to the users.

## Development

- **LLM Chains**: The application utilizes Mixtral LLM chains for processing user queries and executing database operations. Two chains are created: one for generating queries and another for executing them and explaining the results.

- **Frontend Interface**: Streamlit is used for creating the frontend interface of the application. It provides a simple yet effective way to build interactive web applications with Python.


Feel free to contribute to the project by submitting bug fixes, enhancements, or new features through pull requests.

