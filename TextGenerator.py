# import openai
#
# # Apply for an API key from OpenAI

import openai
openai.api_key = "enter key here"

def generate_text(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    message = completion["choices"][0]["message"]["content"]
    return message

def generate_outline(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
        ]
    )
    message = completion["choices"][0]["message"]["content"]
    return message
# ex_1 = "In recent years, the Canadian government has been grappling with the issue of online content regulation. In 2021, the government introduced Bill C-11, an update to the Personal Information Protection and Electronic Documents Act (PIPEDA), which aims to regulate the collection, use, and disclosure of personal information in the digital realm. However, this bill has faced criticism for its potential to infringe upon freedom of speech and impose censorship on media.\n\nThe bill would give the Canadian Radio-television and Telecommunications Commission (CRTC) the power to regulate and block online content that is deemed harmful or offensive. While the goal of protecting Canadians from harmful content is important, the bill's broad language and vague definitions of \"harmful\" could lead to censorship of legitimate and important content.\n\nImagine a world where the government could control what you see and hear. Sounds like a dystopian novel, right? Unfortunately, this isn't just fiction. The proposed Bill C-11 in Canada is trying to censor the media, and it's more dangerous than you might think. Throughout history, censorship has been used to silence voices and control the narrative. Think of Nazi Germany, where books were burned and art was destroyed because it went against the regime's beliefs. Or even the more recent history of China, where the government censors the internet and social media, so the citizens can't access information that is deemed \"harmful.\" It's a slippery slope, and it's something that should concern us all. The proposed bill might not be as extreme, but it's a step in that direction. It could be used to silence dissenting voices and control the narrative. It's a dangerous precedent that could be set if we allow this to happen.\n\nTo make matters worse, the proposed bill could also have negative effects on artists, content creators, and the media industry. The bill would force platforms to remove content that violates copyright laws, but the criteria for what qualifies as a violation is vague and open to interpretation. This could result in overzealous censorship, where even fair use content might get taken down."
# ex_1 = "Berserk is also known for its unconventional storytelling approach, which sets it apart from many other anime series. The series uses a nonlinear narrative structure that jumps back and forth through time, providing glimpses into the past and the present of the story's characters. This approach to storytelling allows the series to explore the backstory of its characters, their motivations, and the world they inhabit, in a way that feels organic and natural. \nThe nonlinear storytelling approach in Berserk is not only intriguing, but it also helps to keep the audience engaged. The series has a way of making the viewer work to put the pieces of the story together, creating a sense of mystery and intrigue. This approach is a stark contrast to more conventional storytelling methods used in anime and allows for a more dynamic and engaging viewing experience. \nThis storytelling style has since been emulated by many other anime series. For example, Death Note, Steins;Gate, and Durarara!! all use a nonlinear narrative structure to tell their stories, just like Berserk. This approach has become increasingly popular in modern anime, and it's a testament to the impact that Berserk has had on the industry. Overall, Berserk has helped to redefine the way that anime tells its stories, and this is one of the key ways that it has influenced the medium. Its nonlinear narrative approach has inspired other anime series to take more risks with their storytelling and push the boundaries of what is considered acceptable. This has helped to create a new era of anime that is more complex, dynamic, and engaging, and it's all thanks to the trailblazing work of Berserk and its creator, Kentaro Miura."
ex_1 = "I'm going to start this video off with a statistic that I can absolutely not verify but odds are that if you've been a fan of anime manga manwa and so on over the last few years you've come in contact with at least one isakai and if you haven't for those of you who don't know isakai is just trapped in another world usually it starts with a protagonist getting absolutely railroaded by truck-kun or some kind of Otherworldly or just completely natural phenomena and they wake up as a hero in a separate World a few notable examples being Sword Art Online though that's more trapped in another world than reincarnated in another world konosuba re zero Devil is a part-timer but that one's isakai flipped on its head it's them coming over here not us going over there and the story is usually pretty cookie cutter main character dies or has something spectacular happen to them they're reborn in another world and they either live out the rest of their days there as a hero or Endeavor to complete some kind of task or usually defeat some kind of demon king which will then let them get home back to the world they belong in the main character will take up this mantle of hero and they will Garner all manner of allies and friends to their side to facilitate getting back home they are strong-willed usually kind extremely empathetic and above all else good but what if something happened to change that What if after everything our hero goes through all the trials and tribulations the deaths of friends the great battles against all manner of monsters and enemies the sacrifices that they make and the losses that they have to deal with What if after all of that they arrive home and everything they knew is gone there's nothing here for them but misery well Hero has returned or The Warriors return is that Hero has returned is a Korean manwa written by narak and illustrated by fungbak I'm definitely getting those names wrong and it starts out as I said like most isakai our young hero is whisked off to another world they're scared they're upset they manage to struggle through an entire year building up their strength moving past their fears and they go through an entire hero's journey driven by their kindness and empathy for the beings of that world all in the pursuit of getting home to his family who he loves and his friends who he misses and finally with the help of his adventuring party he takes down the demon king and is returned home eight months on from when he left"
# ex_outline="I. Introduction\n A. Definition of a first-person shooter \n B. The evolution of first-person shooters \n\n II. Rise of the FPS Genre \n A. The early years of first-person shooters B. Successful titles that shaped the genre\n\nIII. Microtransactions and Loot Boxes\nA. Introduction of in-game spending\nB. Problems with in-game spending\n\nIV. Scrutiny of the Industry\nA. Controversy and backlash\nB. Impact on the industry "
ex_outline="I. Introduction\nA. Definition of greed in the entertainment industry\nB. Overview of Kanye West's career and downfall\n\nII. Kanye West's Rise to Fame \nA. Early years in the rap industry \nB. Breakout success with The College Dropout\nC. Critical acclaim and commercial success with subsequent albums \n\nIII. Greed Takes Over \n\nA. Kanye's increasing obsession with fame and fortune \nB. Focus on self-promotion and publicity stunts \nC. Departure from musical authenticity \n\nV. Conclusion and impact on the Industry \nA. Reflection of a larger trend towards commercialization in music \nB. Discussion of the effects of greed on artistic integrity \nC. Call to action for artists and consumers to prioritize authentic, meaningful content"

ex_intro = "The world of Harry Potter is no stranger to controversy, and the upcoming video game Hogwarts Legacy is no exception. The game's connection to author JK Rowling, who has been accused of making hurtful and harmful comments about the trans community, has sparked intense debate about whether supporting the game is a transphobic act. Some argue that enjoying the game doesn't mean you support Rowling's views, while others contend that by supporting the game, you're contributing to a larger cultural context that perpetuates transphobia. In this video, I'll dive into both sides of the debate and argue that while playing the video game may not be inherently transphobic, it does contribute to a larger problem of normalizing and perpetuating harmful beliefs about trans people."

ex_outro = "The vanity of Logan Paul highlights the importance of humility and accountability in influencer culture. It's important for influencers to be humble, transparent and accountable for their actions, rather than being driven by vanity and a desire for fame."
drive_list=['Power', 'Money', 'Curiosity', 'Love', 'Murder', 'Life', 'Corruption', 'Greed', 'Creativity', 'Passion', 'Desire for love and connection:', 'Quest for identity and purpose:', 'Pursuit of power and success:', 'Fear of death and loss:', 'Need for redemption', 'Exploration of the unknown:', 'Coping with trauma and grief:', 'Building and maintaining relationships:', 'Coming of age:', 'Redemption and second chances:', 'Confronting the unknown:', 'Creativity and self-expression:', 'Persistence and determination:']


thumbnail_phrases = [
    "Unbelievable twist revealed",
    "Mind-blowing moments",
    "Cant believe this exists",
    "Unexpectedly brilliant",
    "A true game-changer",
    "Wait what just happened",
    "This will blow your mind",
    "The ultimate plot twist",
    "Surprisingly addictive",
    "You wont see this coming",
    "Shockingly good trust us",
    "More than meets the eye",
    "The most mind-bending experience",
    "Freddy is insane",
    "What were they thinking",
    "Now thats a problem",
    "Underrated masterpiece",
    "You need to watch this",
    "Fnaf unraveled",
    "Trippiest show ever",
    "Better than you think",
    "Outrageous",
    "Astounding discovery",
    "Tragic heartache",
    "Heartwarming tale",
    "Exhilarating quest",
    "Phenomenal skill",
    "Terrifying encounter",
    "Hilarious antics",
    "Devastating reveal",
    "Enthralling mystery",
    "Revolutionary idea",
    "Unforgettable scene",
    "Shocking event",
    "Captivating story",
    "Outrageous act",
    "Staggering feat",
    "Breathtaking view",
    "Electrifying moment",
    "Sensational twist",
    "Inspiring journey",
    "Triumphant tale",
    "Suspenseful mysteries that will keep you intrigued"
]