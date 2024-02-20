from openai import OpenAI
import re


client = OpenAI(api_key='api_key')
 
def generate_gpt_sql_query(user_input):
    """
    Generates an SQL query based on the user's input using GPT-4.

    :param user_input: The user's input describing what they are looking for in natural language.
    :return: A string containing the suggested SQL query.
    """

    context = ("You are an AI trained to understand a user's input, process it, and create the best SQL query for the input. "
           "The database contains a table named 'meals' with the following columns:\n"
           "- 'Meal Name'\n"
           "- 'Easy to cook'\n"
           "- 'Jain-friendly'\n"
           "- 'Tithi-friendly'\n"
           "- 'Healthy'\n"
           "- 'Tiffinable'\n"
           "- 'Tasty'.\n"
           "Each column has values inWhen formulating queries, consider these columns to retrieve relevant information."
          )

    # Combine the context with the user's input to form the prompt
    prompt = f"{context}\n\nUser: {user_input}\nAI:"

    try:  
        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": "You are an AI trained to understand a user's input, process it, and create the best SQL query for the input. "
           "The database contains a table named 'meals' with the following columns:\n"
           "- 'Meal Name'\n"
           "- 'Easy to cook'\n"
           "- 'Jain-friendly'\n"
           "- 'Tithi-friendly'\n"
           "- 'Healthy'\n"
           "- 'Tiffinable'\n"
           "- 'Tasty'.\n"
           "Each column has values When formulating queries, consider these columns to retrieve relevant information."
           "attributes need to be inside double quotes in the query" "and values of attributes are stored in 'yes' or 'no'."
           "use tiffinable attribute only when explicityly mentioned 'tiffin',"
           
           },
        {"role": "user", "content": user_input},
        ]
        )
        print("_______________________")

        # Extracting the latest response from the completion object
        if completion.choices[0].message.content:
            latest_response = completion.choices[0].message.content
        else:
            latest_response = "No response generated."
        
        sql_query = re.findall(r'```sql\n(.*?)\n```', latest_response, re.DOTALL)
        if sql_query:
            sql_query = sql_query[0]
        print(sql_query)
        print("hello_________________sql query baove this ")
        return sql_query

    except Exception as e:
        print(f"An error occurred: {e}")
        return "An error occurred during SQL query generation."

print(generate_gpt_sql_query("suggest breakfast meals"))
