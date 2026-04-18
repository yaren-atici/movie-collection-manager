from collection import MovieCollection

def main():
    collection = MovieCollection()

    while True:
        print("\n--- Movie Collection Manager ---")
        print("1. Add movie")
        print("2. View movies")
        print("3. Search by title")
        print("4. Filter by genre")
        print("5. Show statistics")
        print("6. Show top movies")
        print("7. Multi-search")
        print("8. Reference vs Copy demo")
        print("0. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            title = input("Title: ")
            genre = input("Genre: ")
            year = int(input("Year: "))
            rating = float(input("Rating: "))

            collection.add_movie(
                title=title,
                genre=genre,
                year=year,
                rating=rating
            )

        elif choice == "2":
            collection.view_movies()

        elif choice == "3":
            title = input("Enter title: ")
            print(collection.search_by_title(title))

        elif choice == "4":
            genre = input("Enter genre: ")
            results = collection.filter_by_genre(genre)
            for m in results:
                print(m)

        elif choice == "5":
            print(collection.get_statistics())

        elif choice == "6":
            for m in collection.top_movies():
                print(m)

        elif choice == "7":
            titles = input("Enter titles separated by comma: ").split(",")
            results = collection.search_multiple_titles(*titles)
            for m in results:
                print(m)

        elif choice == "8":
            collection.reference_vs_copy_demo()

        elif choice == "0":
            break

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()