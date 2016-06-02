import fresh_tomatoes
import media



he_died = media.Movie("He Died With A Felafel In His Hand (2001)",
					"A writer has to keep moving house",
					"https://images.duckduckgo.com/iu/?u=http%3A%2F%2Frowland-s-howard.com%2Fimg%2Fdiscography%2Ffelafel.jpg&f=1",
					"https://www.youtube.com/watch?v=xQFC00VVSBw")
alien = media.Movie("Alien (1979)",
					"An alien invades a space ship",
					"http://imgc.allpostersimages.com/images/P-473-488-90/56/5663/DGGUG00Z/posters/alien.jpg",
					"https://www.youtube.com/watch?v=LjLamj-b0I8")
aliens = media.Movie("Aliens (1986)",
					"A remote colony struggles to survive an alien threat",
					"https://uk.movieposter.com/posters/archive/main/63/MPW-31602",
					"https://www.youtube.com/watch?v=XKSQmYUaIyE")
terminator = media.Movie("The Terminator (1984)",
					"A cyborg is sent from the future to change history",
					"https://uk.movieposter.com/posters/archive/main/14/A70-7230",
					"https://www.youtube.com/watch?v=-fN82upbGPo")
toy_story = media.Movie("Toy Story (1995)", 
						"A story of a boy and his toys that come to life", 
						"https://uk.movieposter.com/posters/archive/main/15/A70-7642", 
						"https://www.youtube.com/watch?v=KYz2wyBy3kc")
avatar = media.Movie("Avatar (2009)", 
					"A marine on an alien planet", 
					"https://uk.movieposter.com/posters/archive/main/94/MPW-47064",
					"http://www.youtube.com/watch?v=5PSNL1qE6VY")

movies = [alien,aliens,avatar,he_died,terminator,toy_story,avatar]
fresh_tomatoes.open_movies_page(movies)
print(media.Movie.VALID_RATINGS)