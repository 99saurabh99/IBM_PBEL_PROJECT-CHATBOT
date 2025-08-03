# IBM_PBEL_PROJECT-CHATBOT
This Python-based chatbot is designed to recommend books to users by searching live data from the web using the Google Books API.
When a user interacts with the chatbot, it first prompts them to enter a genre, topic, or keyword related to the kind of books they are interested 
in—such as "mystery", "romance", "science fiction", or even specific themes like "psychology" or "productivity". Once the user provides a keyword,
the chatbot sends a request to the Google Books API, which is a free and reliable web service offered by Google that provides detailed information about millions of books available online.

The chatbot then processes the response it receives from the API, which includes details such as the book title, author(s), and sometimes even a short description.
It extracts the most relevant results and displays the top five books to the user, listing each one with its title and author.
This allows the user to instantly receive fresh and accurate book recommendations based on their interests, without the need for a pre-defined or static list of books.

After showing the recommendations, the chatbot asks the user if they would like to search for more books. If the user says yes, the process repeats;
if the user chooses to stop, the chatbot thanks them and ends the session. This loop allows for an ongoing and interactive conversation, making the chatbot feel responsive and helpful.
The use of live web data ensures that recommendations are always current and diverse.

Overall, this chatbot offers a simple but effective way for users to discover new books by connecting natural language input with real-time data from the web.
It is lightweight, easy to run, and a great example of combining Python with web APIs to build practical AI tools.
