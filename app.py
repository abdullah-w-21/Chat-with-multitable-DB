from langchain_community.utilities.sql_database import SQLDatabase
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, create_sql_query_chain
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()
# Loading DB
def load_db(db_name):
    db = SQLDatabase.from_uri(f"sqlite:///{db_name}")
    return db

# Send db to LLM to get SQL queries
def chain_create(db):
    llm = ChatGroq(model="mixtral-8x7b-32768", api_key=os.getenv("GROQ_API_KEY"))
    chain = create_sql_query_chain(llm, db)
    return chain

# This chain deals with explaining the retrieved output from running the query
def sql_infer(db, chain, user_question):
    sql_query = chain.invoke({"question": user_question})
    result = db.run(sql_query) #running query and getting result

    #streamlit display result & code
    st.code(sql_query)
    st.write(result)
    answer_prompt = PromptTemplate.from_template(
        """Given the following user question, corresponding SQL query, and SQL result, generate a proper reply to give to user

    Question: {question}
    SQL Query: {query}
    SQL Result: {result}
    Answer: """
    )

    llm_model = ChatGroq(model="mixtral-8x7b-32768", api_key=os.getenv("GROQ_API_KEY"))
    llm = LLMChain(llm=llm_model, prompt=answer_prompt)
    ans = llm(inputs={"question": user_question, "query": sql_query, "result": result})
    return ans["text"]

# Combining both chains to display in streamlit app
def main():
    st.set_page_config(page_icon="🚀", layout="wide", page_title="Database Chatapp")
    st.title("Chat with Multitable DB")

    col1, col2 = st.columns([2, 3])

    with col1:

        file_name = st.text_input("Enter name of a DB file")
        if st.button("Load DB"):

            db = load_db(file_name)

            st.subheader("Table Names")
            st.code(db.get_usable_table_names())

            st.subheader("Schemas")
            st.code(db.get_table_info())

    with col2:

        if file_name is not "":
            db = load_db(file_name)
            chain = chain_create(db)
            question = st.text_input("Write a question about the data", key="question")

            if st.button("Get Answer"):
                if question:
                    #failsafe mechanism retries 5 times
                    attempt = 0
                    max_attempts = 5
                    while attempt < max_attempts:
                        try:
                            out = sql_infer(db, chain, question)
                            st.subheader("Answer")
                            st.write(out)
                            break

                        except Exception as e:
                            st.error(e)
                            attempt += 1
                            st.error(
                                f"Attempt {attempt}/{max_attempts} failed. Retrying..."
                            )
                            if attempt == max_attempts:
                                st.error(
                                    "Unable to get the correct query, refresh app or try again later."
                                )
                            continue

# Call the main function
if __name__ == "__main__":
    main()