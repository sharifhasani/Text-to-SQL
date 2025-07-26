from langchain.callbacks.streamlit import StreamlitCallbackHandler
import streamlit as st
import os
import re
import pandas as pd
from sqlalchemy import create_engine, text
from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_community.chat_models import ChatCohere
 
 
def extract_sql_query(output):
    pattern = r'```sql(.*?)```'
    match = re.search(pattern, output, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None
 
def parse_result(raw_result):
    sql_query = extract_sql_query(raw_result)
    if sql_query:
        return sql_query
    return raw_result
 
 
st.set_page_config(page_title="Smart Database Assistant", layout="centered")

if "cohere_api_key" not in st.session_state or "db_url" not in st.session_state:
    st.title("🔧 تنظیمات اولیه فقط یک‌بار")
    with st.form("setup_form"):
        cohere_api_key = st.text_input("🔑 Cohere API Key", type="password")
        db_url = st.text_input(
            "🗄 Database Connection URL",
            value="postgresql+psycopg2://text2sql:text2sql@postgres:5432/netflix"
        )
        submitted = st.form_submit_button("💾 ذخیره")

        if submitted:
            if cohere_api_key and db_url:
                st.session_state.cohere_api_key = cohere_api_key
                st.session_state.db_url = db_url

                os.environ["COHERE_API_KEY"] = cohere_api_key

                st.rerun()
            else:
                st.warning("لطفاً هر دو فیلد را پر کنید.")
else:
    st.success("🎉 اطلاعات قبلاً وارد شده‌اند.")

    os.environ["COHERE_API_KEY"] = st.session_state.cohere_api_key
 
    st.title("💡 Connect RAG+LLM to Database")

    question = st.text_area("❓ Ask a question about your data", height=100)

    # Initialize session state for chat history
    if "history" not in st.session_state:
        st.session_state.history = []
    
    if st.button("💬 Ask"):
        try:
            engine = create_engine(st.session_state.db_url)
            db = SQLDatabase(engine)
            llm = ChatCohere(streaming=True)
    
            db_chain = SQLDatabaseChain.from_llm(
                llm=llm,
                db=db,
                return_direct=True,
                verbose=True,
                return_sql=True
            )
    
            st.subheader("✅ Answer in progress:")
            stream_placeholder = st.empty()
            stream_handler = StreamlitCallbackHandler(stream_placeholder)
    
            result = db_chain.invoke(
                question,
                config={"callbacks": [stream_handler]}
            )
    
            sql_query = parse_result(result["result"])
    
            # Append to history
            st.session_state.history.append({
                "question": question,
                "sql": sql_query,
                "result": None
            })
    
            if sql_query:
                with engine.connect() as connection:
                    query = text(sql_query)
                    result_df = pd.read_sql(query, connection)
                    st.session_state.history[-1]["result"] = result_df
    
        except Exception as e:
            st.error(f"❌ Error: {e}")
    
if "history" in st.session_state and st.session_state.history:
    st.sidebar.subheader("📜 Previous Questions")

    question_list = []
    index_to_history = {}
    for idx, entry in enumerate(reversed(st.session_state.history)):
        q_short = entry["question"][:50].strip().replace("\n", " ")
        label = f"Q{len(st.session_state.history) - idx}: {q_short}"
        question_list.append(label)
        index_to_history[label] = entry

    selected_label = st.sidebar.selectbox("🧾 Select a previous question", question_list)

    if selected_label:
        selected_entry = index_to_history[selected_label]
        st.sidebar.markdown("**🔍 Full Question:**")
        st.sidebar.markdown(selected_entry["question"])

        if selected_entry.get("sql"):
            st.sidebar.markdown("**🧠 SQL Query:**")
            st.sidebar.code(selected_entry["sql"], language="sql")

        if selected_entry.get("result") is not None:
            st.sidebar.markdown("**📊 Sample Result:**")
            st.sidebar.dataframe(selected_entry["result"].head(1))


