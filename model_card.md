# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

VibeFind
---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

It is designed to recomend songs based on user preferences/ profile with more weight on the mood and energy of the song and some weight on genre, tempo, ect.

The Assuptions it makes about the user is based on the profile of the user .

This is more for classroom exploration since currently this only has one profile in the program.
---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

---

## 4. Data  

Describe the dataset the model uses.  

The recommender uses a small catalog of 18 songs stored in the project data file. Each song includes basic metadata such as title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The catalog includes a mix of genres and moods, including pop, lofi, rock, ambient, jazz, folk, reggae, house, classical, hip hop, country, and disco.

The dataset is i small and curated for classroom use, so it does not represent the full diversity of real-world music listening. 
---

## 5. Strengths  

Where does your system seem to work well  

This recommender works best for users whose taste is clear and fairly consistent. It does a good job picking songs that match a specific mood, energy level, and genre at the same time. For example, a user who likes upbeat pop songs with high energy should receive strong, sensible recommendations because those qualities are explicitly weighted in the scoring logic.

The system also performs well when the user’s preferences are straightforward and the catalog contains obvious matches. In those cases, the recommendations feel intuitive because the model is easy to explain: it can point to why a song was chosen based on mood, genre, energy, and a few other features.

It is especially useful as a simple classroom example of how recommender systems turn human preferences into a ranked list of suggestions.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

The logic rewards “what the user already likes” very strongly, which can reduce exploration and make the recommendations feel repetitive.So the system tends to keep recommending more songs from the same narrow cluster.

In addition the dataset is is small and uneven across genres and moods, so some styles may be over-represented simply because they fit the profile better
---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

I evaluated the system by running it against several example user profiles and comparing the top recommendations to what seemed reasonable for each profile. The results were checked by looking at whether the recommended songs matched the intended mood, genre, and energy profile.

The main profiles tested were:

- High-Energy Pop: this profile was expected to favor bright, upbeat pop songs with strong energy, and the system did return songs that fit that pattern.
- Chill Lofi: this profile was expected to prefer calm, low-energy, acoustic-feeling tracks, and the recommender produced softer, more relaxed options.
- Deep Intense Rock: this profile was expected to prioritize dramatic, high-intensity tracks, and the top results reflected that preference.
- Adversarial Conflicted: this profile combined a sad mood with a very high energy target to test whether the scoring logic would behave in a strange or inconsistent way. The system still produced ranked results, but this case showed that the model can be sensitive to conflicting preferences.

Overall, the evaluation showed that the recommender is interpretable and works well for clear profiles, but it can also surface edge cases where the logic feels overly rigid or simplistic.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

I would improve the model by making it more interactive by allowing the user to define their music profile. I would also add a feature that would introduce a exploritory feature to the profile. where a user can decide whether they want the app to introduce them to new music that is different to their preferences.

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  

i learned that there are many things to take into consideration when designing a music recommender and that one has to make desisions about how you want the algorithem to be and what do you want it to priorities. This will inevitably cause bias and based on the goal of the program this may be a good or bad thing.
It is less about finding one perfect formula and more about making thoughtful design choices. Small changes in the weighting of features such as mood, genre, and energy can strongly change the results. A system can seem objective while still reflecting bias, because the rules it follows are shaped by the preferences and assumptions of the designer building the program.
