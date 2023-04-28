import html
from bs4 import BeautifulSoup
import pandas as pd


def extract_words(book_name):
    # Read the HTML file
    with open(book_name, 'r', encoding='utf-8') as f:
        contents = f.read()
    
    # Convert HTML entities to their corresponding characters
    contents = html.unescape(contents)
    
    # Parse the HTML file with BeautifulSoup
    soup = BeautifulSoup(contents, "html.parser")
    
    # Extract the XML tags for each word
    words = soup.find_all("span")
    
    # Extract the lemma and definition for each word
    arm_words = []
    pos = []
    form = []
    translation = []
    
    for word in words:
        arm_word = word.text.strip()
        arm_words.append(arm_word)
        titles = word.get("titles")
        
        if titles:
            titles = titles.split("	")
            
            try:
                pos_form = titles[0].split()[1:]
            except:
                pass
            
            try:
                if str(pos_form[0]) == str(pos_form[0]).upper():
                    pos.append(pos_form[0])
            except:
                pos.append(None)
                pass
            
            try:
                translation.append(titles[-1].split(","))            
            except:
                translation.append(None)
                pass
            
            try:
                form.append(pos_form[1])
            except:
                form.append(None)
                pass
    
        else:
            pos.append(None)
            form.append(None)
            translation.append(None)
    
    # Modifying lists for better look
    for i in range(len(pos)):
        if pos[i] is not None:
            pos[i] = pos[i].replace('(', '').replace(')', '')
            
    for i in range(len(form)):
        if form[i] is not None:
            form[i] = form[i].replace('(', '').replace(')', '')


    # Create a dictionary with the lists
    data = {"word": arm_words, "pos": pos, "form": form, "translation": translation}

    # create a dataframe from the dictionary
    df = pd.DataFrame(data)
    
    return df

def remove_title(df, title_length):
    # Remove the title, drop the rows with none values
    df = df.drop(index=range(title_length))
    df = df.dropna(axis=0, thresh=2)
    
    return df

