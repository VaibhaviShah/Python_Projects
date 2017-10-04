import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story", "It is a story of a boy whose toys come to life", "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar", "A biologist visits an alien planet", "https://pmcdeadline2.files.wordpress.com/2013/12/avatar__131216143856.jpg", "https://www.youtube.com/watch?v=8V2IaMqFIVw")
exam = media.Movie("Exam", "How a CEO tests people to identify his successor", "https://upload.wikimedia.org/wikipedia/en/0/09/Exam_poster.jpg", "https://www.youtube.com/watch?v=bkdt2Sygew0")

movies = [toy_story, avatar, exam]
fresh_tomatoes.open_movies_page(movies)

