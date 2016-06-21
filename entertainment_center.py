# Lesson 3 : Make classes
# mini-project: movie website

import media
import fresh_tomatoes

deadpool = media.Movie('Deadpool',
		       	  'Wade Wilson is a former Special Forces operative who now works as a mercenary. His world comes crashing down when evil scientist Ajax tortures, disfigures and transforms him into Deadpool.',
                  'https://upload.wikimedia.org/wikipedia/en/4/46/Deadpool_poster.jpg',
		          'https://www.youtube.com/watch?v=ONHBaC-pfsk',
		          'Rating; R')

xmen = media.Movie('The X Men: Apocalypse',
				   'Apocalypse the most powerfull mutant of all comes to reclaim the world.',
                   'http://t3.gstatic.com/images?q=tbn:ANd9GcTOUtd-BQZW_VT8WrTaVzqfiV6YVC3tFxmKZwl0MFKLnb51xqtl',
		           'https://www.youtube.com/watch?v=Jer8XjMrUB4',
		           'Rating; PG-13')

captainamerica = media.Movie('Captain America: Civil War',
				   'Political pressure mounts to install a system of accountability when the actions of the Avengers lead to collateral damage. The new status quo deeply divides members of the team. Captain America believes superheroes should remain free to defend humanity without government interference.',
                   'http://blogs-images.forbes.com/markhughes/files/2016/04/Captain-America-Civil-War-banner-101.jpg',
		           'https://www.youtube.com/watch?v=dKrVegVI0Us',
		           'Rating; PG-13')

sucidesquad = media.Movie('Sucide Squad',
		       	  'Supervillains accept a secret government mission that will likely result in their deaths.',
                  'http://www.gstatic.com/tv/thumb/movieposters/11319046/p11319046_p_v8_ac.jpg',
		          'https://www.youtube.com/watch?v=CmRih_VtVAs',
		          'Rating; sci-fic')

warcraft = media.Movie('Warcraft',
		       	  'Fleeing their dying home to colonize another, fearsome orc warriors invade the peaceful realm of Azeroth.',
                  'http://t3.gstatic.com/images?q=tbn:ANd9GcTCzditN2MtHjUM51mMbNspnJ_NHPWYz3J8zQMoXPRtAeBTpTrf',
		          'https://www.youtube.com/watch?v=RhFMIRuHAL4',
		          'Rating; PG-13')

tmnt = media.Movie('Teenage Mutant Ninja Turtles: Out of the Shadows',
		       	  'The turtles spring into action to battle Shredder, mad scientist Baxter Stockman, Bebop, Rocksteady and the notorious Krang.',
                  'http://t3.gstatic.com/images?q=tbn:ANd9GcS8dZfotMxz99O6qLGsqiy68_WUtTZ6OFhoqlNEVrSQvVlqIB9P',
		          'https://www.youtube.com/watch?v=HeaugHGd1Kw',
		          'Rating; sci-fic')


movies = [deadpool, xmen, captainamerica, sucidesquad, warcraft, tmnt]
#uses list of movie instances as input to generate an HTML file and open it in the browser.
fresh_tomatoes.open_movies_page(movies)

