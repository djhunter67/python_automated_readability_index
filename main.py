from src.equation import ari_function, count_characters, count_sentences, count_words, quantify_ari


def main():
    """Main function."""

    filename = "test_text.txt"

    with open(filename, "r") as file:
        text = file.read()


    words = count_words(text)
    characters = count_characters(text)
    sentences = count_sentences(text)

    ari = ari_function(words, characters, sentences)

    print(f"The ARI for {filename} is {ari}.")
    print(f"This corresponds to a {quantify_ari(ari)} level of difficulty")
    print(f"that is suitable for an average person {ari_function(words, characters, sentences)} years old.") 

if __name__ == "__main__":
    main()