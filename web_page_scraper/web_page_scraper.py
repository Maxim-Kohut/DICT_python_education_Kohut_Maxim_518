from bs4 import BeautifulSoup  # bs4 libr, BS - class from bs4
import requests
import os
import string

# ------------------------------------------
def create_directory(dir_name):
    """
    this func make folder if it not already exists
    """
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)

# ------------------------------------------
def fix_title(bad_title):
    """
    delete bad symbol from file name and make it with underscores
    """
    for character in string.punctuation:
        bad_title = bad_title.replace(character, "")
    return bad_title.strip().replace(" ", "_")

# ------------------------------------------
def write_article_text(save_folder, title_text, article_text):
    """
    save article content into txt file with good name
    """
    file_name = fix_title(title_text) + ".txt"
    file_path = os.path.join(save_folder, file_name)
    with open(file_path, "w", encoding="utf-8") as text_file:
        text_file.write(article_text)

# ------------------------------------------
def download_articles_from_nature(total_pages, wanted_type):
    """
    download pages and find articles by type user give
    """
    base_address = "https://www.nature.com/nature/articles?sort=PubDate&year=2022"

    for current_page in range(1, total_pages + 1):
        current_url = f"{base_address}&page={current_page}"

        try:
            response = requests.get(current_url, timeout=10)
        except requests.exceptions.RequestException as e:
            print("Can't open page:", current_url, "| error:", e)
            continue

        if response.status_code != 200:
            print("page is broken or not exist:", current_url)
            continue  # go to next page if this is bad

        # parsing html with soup
        page_soup = BeautifulSoup(response.text, "html.parser")
        all_articles = page_soup.find_all("article")
        page_folder = f"Page_{current_page}"
        create_directory(page_folder)

        for one_article in all_articles:
            type_element = one_article.find("span", {"data-test": "article.type"})
            if not type_element or type_element.text.strip() != wanted_type:
                continue  # skip if not the type user want

            # find link for article
            link_element = one_article.find("a", {"data-track-action": "view article"})
            if not link_element:
                continue

            full_article_url = "https://www.nature.com" + link_element.get("href")

            try:
                article_response = requests.get(full_article_url, timeout=10)
            except requests.exceptions.RequestException as e:
                print("cant open article:", full_article_url, "| error:", e)
                continue

            if article_response.status_code != 200:
                print("article give bad status:", article_response.status_code)
                continue

            # parse full article page
            full_soup = BeautifulSoup(article_response.text, "html.parser")

            article_body = full_soup.find("div", {"class": "c-article-body"})
            if not article_body:
                # some articles is short type and have different html
                article_body = full_soup.find("div", {"class": "article-item__body"})

            title_tag = full_soup.find("title")
            final_title = title_tag.text.strip() if title_tag else "No_Title"
            final_text = article_body.text.strip() if article_body else "No_Content"

            write_article_text(page_folder, final_title, final_text)

# ------------------------------------------
def start_program():
    """
    entry point of script where user give input
    """
    try:
        how_many_pages = int(input("Enter how many pages to check: "))
        needed_type = input("Enter type of articles (News for exmpl): ")
        download_articles_from_nature(how_many_pages, needed_type)
        print("Check your folders")
    except ValueError:
        print("you must type number for page count")
    except requests.exceptions.RequestException as error:
        print("network or site problem:", error)

# ------------------------------------------
if __name__ == "__main__":
    start_program()
