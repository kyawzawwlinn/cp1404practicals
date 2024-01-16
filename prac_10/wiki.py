import wikipedia


def search_wikipedia():
    while True:
        query = input("Enter a page title or search phrase (or just enter to quit): ")
        if query == '':
            break

        try:
            page = wikipedia.page(query, auto_suggest=False)
            print("\nPage Title:", page.title)
            print("\nSummary:", page.summary)
            print("\nURL:", page.url)
        except wikipedia.DisambiguationError as e:
            print("Disambiguation error. Please be more specific or choose from the following options:\n")
            for option in e.options:
                print(option)
        except wikipedia.PageError:
            print("Page not found. Please try a different search term.")
        except Exception as e:
            print("An error occurred: ", str(e))

        print("\n")


if __name__ == "__main__":
    search_wikipedia()
