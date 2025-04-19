import streamlit as st
from google.genai import Client
import requests
from bs4 import BeautifulSoup
import os
import dotenv

dotenv.load_dotenv()

client = Client(api_key=os.getenv("GEMINI_API_KEY"))

def str_to_ui(ui_str):
    """
    Convert a dictionary to a Streamlit UI.
    """
    globals_ = globals()
    globals_['st'] = st
    globals_['ui_dict'] = ui_str
    globals_['str_to_ui'] = str_to_ui
    globals_['web_search'] = web_search
    globals_['inference_gemini'] = inference_gemini
    exec(ui_str, globals_)
    return ui_str


def search_google_get_urls(query, num_results=5):
    """Fetch news articles related to the query."""
    url =  f"https://www.google.com/search?q={query}&tbm=nws"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        articles = []
        articles = soup.find_all('a', href=True)
        urls = []
        for article in articles:
            href = article['href']
            if 'url?q=' in href and not 'webcache' in href:
                url = href.split('url?q=')[1].split('&')[0]
                if url not in urls:
                    urls.append(url)
            if len(urls) >= num_results:
                break
        return urls
    else:
        print(f"Error fetching search results: {response.status_code}")
        return []


def get_related_articles(query, num_results=5):
    """Fetch related articles for each query."""
    urls = search_google_get_urls(query, num_results=num_results)
    print(urls)
    articles = []
    for url in urls:
        try:
            res = requests.get(url, timeout=5)
            if res.status_code != 200:
                continue
            soup = BeautifulSoup(res.text, 'html.parser')
            paragraphs = soup.find_all('p')
            content = ' '.join([p.get_text() for p in paragraphs])
            articles.append({"url": url, "content": content[:2000]})
        except Exception as e:
            continue
    articles = articles[:num_results]
    return "\n\n".join([f"{article['url']}\n{article['content']}" for article in articles])


def inference_gemini(prompt):
    """
    Get a response from the Gemini API.
    """
    try:
        response = client.models.generate_content(
            # model="gemini-2.5-flash-preview-04-17",
            model="gemini-2.0-flash",
            contents=prompt,
        )
        return response.text
    except Exception as e:
        st.error(f"Error: {e}")
        return None

def web_search(query):
    """
    Perform a web search and return the results.
    """
    try:
        articles = get_related_articles(query, num_results=5)
        with st.expander(f"Searched Articles related to `{query}`"):
            st.write("Related Articles:")
            st.markdown(articles)
        return articles
    except Exception as e:
        st.error(f"Error: {e}")
        return str(e)


def generate_ui(response: str):
    """
    Generate a Streamlit UI from Gemini API response.
    """
    try:
        if response.startswith("Error:"):
            st.error(response)
            return None
        response = response.replace("```python", "").replace("```", "").strip()
        return str_to_ui(response)
    except Exception as e:
        st.error(f"Error: {e}")
        return None
