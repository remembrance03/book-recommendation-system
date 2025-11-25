import sqlite3

books = [
    #harry potter series
    ("Harry Potter and the Philosopher's Stone","Fantasy","J.K. Rowling",
     "A young boy discovers he is a wizard and attends Hogwarts where he uncovers the mystery of the Philosopher’s Stone."),
    ("Harry Potter and the Chamber of Secrets","Fantasy","J.K. Rowling",
     "Harry faces the reopened Chamber of Secrets and confronts a dark force within Hogwarts."),
    ("Harry Potter and the Prisoner of Azkaban","Fantasy","J.K. Rowling",
     "Harry learns that a dangerous escaped prisoner may be connected to his past."),
    ("Harry Potter and the Goblet of Fire","Fantasy","J.K. Rowling",
     "Harry is unexpectedly entered into the Triwizard Tournament and must survive deadly magical challenges."),
    ("Harry Potter and the Order of the Phoenix","Fantasy","J.K. Rowling",
     "Harry forms Dumbledore’s Army as the Ministry denies the return of Voldemort."),
    ("Harry Potter and the Half-Blood Prince","Fantasy","J.K. Rowling",
     "Harry discovers Voldemort’s past while learning from a mysterious textbook belonging to the Half-Blood Prince."),
    ("Harry Potter and the Deathly Hallows","Fantasy","J.K. Rowling",
     "Harry, Ron, and Hermione embark on a quest to destroy Voldemort’s Horcruxes."),
    
    #william shakespeare
    ("Romeo and Juliet","Tragedy","William Shakespeare",
     "A story of two young lovers whose deaths reconcile their feuding families."),
    ("Hamlet","Tragedy","William Shakespeare",
     "Prince Hamlet seeks revenge after the murder of his father by his uncle."),
    ("Macbeth","Tragedy","William Shakespeare",
     "A Scottish nobleman becomes king through murder but faces guilt and downfall."),
    ("Othello","Tragedy","William Shakespeare",
     "A respected general is manipulated into jealousy with tragic consequences."),
    ("Julius Caesar","Historical Drama","William Shakespeare",
     "The events around Caesar’s assassination and the political conflict that follows."),
    ("A Midsummer Night's Dream","Comedy","William Shakespeare",
     "A comedic mix of romance, magic, and misunderstandings in a mystical forest."),
    ("The Tempest","Romantic Drama","William Shakespeare",
     "Prospero uses magic to restore justice after being betrayed and exiled."),
    ("King Lear","Tragedy","William Shakespeare",
     "An aging king divides his kingdom among his daughters leading to betrayal and madness."),
    ("Much Ado About Nothing","Comedy","William Shakespeare",
     "A comedic tale of love, deception, and playful misunderstandings."),
    ("Twelfth Night","Comedy","William Shakespeare",
     "A shipwrecked woman disguises herself as a man leading to romantic confusion."),
    
    #jane austen
    ("Pride and Prejudice","Romance","Jane Austen",
     "Elizabeth Bennet navigates issues of class, marriage, and misunderstandings with Mr. Darcy."),
    ("Sense and Sensibility","Romance","Jane Austen",
     "Two sisters face contrasting romantic challenges in society after their father’s death."),
    ("Emma","Romance","Jane Austen",
     "A well-meaning young woman plays matchmaker but complicates the lives around her."),
    ("Mansfield Park","Romance","Jane Austen",
     "Fanny Price grows up in a wealthy household and faces moral and romantic dilemmas."),
    ("Northanger Abbey","Romance","Jane Austen",
     "A young woman’s imagination shaped by gothic novels leads to humorous misunderstandings."),
    ("Persuasion","Romance","Jane Austen",
     "Anne Elliot gets a second chance at love eight years after being persuaded to refuse a proposal."),
    ("Lady Susan","Drama","Jane Austen",
     "A cunning widow manipulates society and romance to secure her future."),
    
    #john green
    ("The Fault in Our Stars","Young Adult Romance","John Green",
     "Two teens with cancer fall in love and search for meaning beyond their illness."),
    ("Looking for Alaska","Young Adult Fiction","John Green",
     "A teen at boarding school forms deep friendships until a tragic event changes everything."),
    ("Paper Towns","Young Adult Fiction","John Green",
     "A boy searches for a missing girl while discovering the difference between fantasy and reality."),
    ("An Abundance of Katherines","Young Adult Fiction","John Green",
     "A former child prodigy goes on a road trip after his 19th breakup with a girl named Katherine."),
    ("Turtles All the Way Down","Young Adult Fiction","John Green",
     "A girl with OCD navigates friendship, mental health, and a missing billionaire mystery."),
    ("Will Grayson, Will Grayson","Young Adult Fiction","John Green & David Levithan",
     "Two boys with the same name cross paths changing the direction of their lives."),

     #mystery
    ("Gone Girl", "Mystery", "Gillian Flynn", 
     "A woman goes missing on her wedding anniversary, revealing dark secrets about her marriage."),
    ("The Girl with the Dragon Tattoo", "Mystery", "Stieg Larsson", 
     "A journalist and a hacker investigate a wealthy family’s decades-old disappearance."),
    ("Big Little Lies", "Mystery", "Liane Moriarty",
      "Secrets and lies unravel in a small town leading to murder and intrigue."),
    ("Sherlock Holmes: A Study in Scarlet", "Mystery", "Arthur Conan Doyle",
      "Detective Sherlock Holmes investigates a mysterious murder with his partner Dr. Watson."),
    ("The Hound of the Baskervilles", "Mystery", "Arthur Conan Doyle", "Sherlock Holmes faces a legendary beast terrorizing a wealthy family on the moors."),
    ("And Then There Were None", "Mystery", "Agatha Christie",
      "Ten strangers trapped on an island are killed one by one as secrets surface."),
    ("Murder on the Orient Express", "Mystery", "Agatha Christie",
      "Detective Hercule Poirot investigates a murder on a luxurious train with many suspects."),
    ("The Da Vinci Code", "Thriller", "Dan Brown",
      "A symbologist uncovers a religious conspiracy while solving a series of mysterious codes."),
    ("Angels & Demons", "Thriller", "Dan Brown",
      "A physicist uncovers a secret society plotting destruction in the Vatican."),
    ("The Silent Patient", "Thriller", "Alex Michaelides",
      "A woman stops speaking after murdering her husband, and a psychologist tries to uncover her motive."),
    ("Before I Go to Sleep", "Thriller", "S.J. Watson",
      "A woman with amnesia struggles to piece together her memories and uncovers shocking truths."),
    ("In the Woods", "Mystery", "Tana French",
      "A detective investigates a child’s murder while confronting his own past trauma."),
    ("The Reversal", "Thriller", "Michael Connelly",
      "A lawyer reopens a high-profile case with unforeseen twists and courtroom drama."),
    ("I Am Watching You", "Thriller", "Teresa Driscoll",
      "A missing person case reveals unexpected secrets and dangerous lies."),
    ("Shutter Island", "Thriller", "Dennis Lehane",
      "A U.S. Marshal investigates a psychiatric facility on an isolated island with shocking revelations.")
]

#connectingggggggg
conn = sqlite3.connect("books.db")
cursor = conn.cursor()

#data insertion
cursor.executemany(
    "INSERT INTO books (title, genre, author, summary) VALUES (?, ?, ?, ?)", 
    books #varible that has books stored as tuples
)

conn.commit()
conn.close()

print("Books inserted successfully!")
