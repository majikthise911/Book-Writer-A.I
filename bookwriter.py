import TextGenerator as tg  # Assuming tg is a module containing generate_text

# Generate book concept and outline


chapter_count = 1  # You can change this to the desired number of chapters
chapter_segments = 6  # Adjust this based on your desired chapter length (3000 words / 500 words per segment)
training_data = '''
I. Chapter 1
A. Explanation of the butterfly effect and how it relates to kindness
B. Definition of kindness
C. Importance of kindness in daily life

II. Chapter 2
A. Introduction of the barista
B. The stranger’s coffee
C. The stranger’s reaction
D. The ripple effect on the stranger’s day and the days of those he interacts with

III. Chapter 3
A. Introduction of the teacher
B. The student’s story
C. The teacher’s response
D. The impact on the student’s life and future

IV. Chapter 4
A. Introduction of the neighbor
B. The act of kindness
C. The ripple effect on the neighborhood and community
D. The sense of community that is created

V. Chapter 5
A. Introduction of the busy executive
B. The encounter with a homeless man
C. The decision to take action
D. The creation of the executive’s own ripple effect

VI. Chapter 6
A. Introduction of the stranger
B. The act of kindness that changes a life
C. The unexpected connection with the giver
D. The transformation in the stranger’s life
'''

# Generate book concept
BookConcept = tg.generate_text("Generate a unique and compelling book concept.")

# Generate book outline based on the number of chapters
outline_prompt = f"Create a detailed book outline chapter by chapter for a book based on {BookConcept}, with {chapter_count} chapters. Each Chapter should have it's own part in the outline. There should not be more parts than their are chapters. Use the following training data as a reference:\n{training_data}"
BookOutline = tg.generate_text(outline_prompt)

def create_sentence(num_chapters, BookOutline):
    chapters = ', '.join([f"chapter {i}" for i in range(1, num_chapters + 1)])
    sentence = f"rewrite this outline to have {num_chapters} chapters, {chapters}. only return the outline:\n{BookOutline}"
    return sentence

# Example usage:

prompt=(create_sentence(chapter_count, BookOutline))
BookOutline = tg.generate_text(prompt)

print(BookOutline)

# Generate chapters


chapters = []

for chapter_num in range(1, chapter_count + 1):
    chapter_parts = []

    # Generate chapter segments
    for segment in range(1, chapter_segments + 1):
        if segment == 1:
            prompt = f"Write the first 500 words of Chapter {chapter_num}: [Chapter{chapter_num}Title], based on the concept {BookConcept} and the outline {BookOutline}."
        else:
            prev_segment_text = chapter_parts[-1]
            prompt = f"Continue the story from {prev_segment_text} and write the next 500 words of Chapter {chapter_num}: [Chapter{chapter_num}Title]."

        segment_text = tg.generate_text(prompt)
        chapter_parts.append(segment_text)
        print(chapter_parts[-1])
    # Combine chapter segments into a single chapter
    full_chapter = " ".join(chapter_parts)
    chapters.append(full_chapter)

print("generating conclusion")

chapter_summaries=[]

def split_into_segments(text, max_segment_length):
    segments = []
    words = text.split()

    current_segment = []
    current_segment_length = 0

    for word in words:
        word_length = len(word)

        if current_segment_length + word_length + 1 <= max_segment_length:
            current_segment.append(word)
            current_segment_length += word_length + 1
        else:
            segments.append(" ".join(current_segment))
            current_segment = [word]
            current_segment_length = word_length + 1

    if current_segment:
        segments.append(" ".join(current_segment))

    return segments


for chapter_num, chapter in enumerate(chapters, start=1):

    chapter_parts = split_into_segments(chapter, 8000)
    chapter_index=[]
    for chapter_num_2, chapter_2 in enumerate(chapter_parts, start=1):

        summary = tg.generate_text(f"Write a concise summary of this: {chapter_2}")
        chapter_index.append(summary)
    combined_string = " ".join(chapter_index)
    summary = tg.generate_text(f"Write a concise summary of Chapter {chapter_num}: {combined_string}")
    chapter_summaries.append(summary)

# for chapter_num, chapter in enumerate(chapters, start=1):
#     summary = tg.generate_text(f"Write a concise summary of Chapter {chapter_num}: {chapter}")
#     chapter_parts = split_into_segments(chapter, 8000)
#     chapter_summaries.append(summary)




# Combine the chapter summaries
chapter_summaries_joined = "\n ".join(chapter_summaries)

# Divide the chapter_summaries text into relatively even segments of up to 1500 characters
chapter_summaries_parts = split_into_segments(chapter_summaries_joined, 8000)

def create_condensed_summary(summaries_list):
    condensed_summaries = []
    for summary in summaries_list:
        condensed_summary = tg.generate_text(f"Write an even more concise summary for: {summary}")
        condensed_summaries.append(condensed_summary)
    return condensed_summaries


# Join and summarize the smaller parts iteratively until the result is less than 1500 characters
while len(" ".join(chapter_summaries_parts)) > 8000:
    print("rewriting summary")
    chapter_summaries_parts = create_condensed_summary(chapter_summaries_parts)

chapter_summaries_joined = "; ".join(chapter_summaries_parts)



# Generate book conclusion
BookConclusion = tg.generate_text(f"Write a satisfying conclusion for the book with the concept {BookConcept}, the outline {BookOutline}, and the summaries of the story developed so far: {chapter_summaries_joined}. Tie up all loose ends and leave a lasting impression on the reader.")

# Generate epilogue (optional)
BookEpilogue = tg.generate_text(f"Write an epilogue that provides a glimpse into the characters' lives or the world after the events of the book, based on the concept {BookConcept}, the outline {BookOutline}, and the summaries of the story developed: {chapter_summaries_joined}, and the conclusion {BookConclusion}.")

chapters.append(BookConclusion)
chapters.append(BookEpilogue)
