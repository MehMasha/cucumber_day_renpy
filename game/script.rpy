# Определение персонажей игры.
define me = Character('MehMasha', color="#c8ffc8")

# Игра начинается здесь:
label start:

    "Каждую вторую субботу июля в Суздале проводится праздник Огурца"

    "И в этом году я решила его посетить"

    scene bg suzdal

    show me idle

    me "Ура! Наконец-то я приехала в Суздаль!"

    me "Осталось только найти сам музей Деревянного зодчества..."

    show me idle at right
    show map suzdal:
        xalign 0.0
        yalign 0.0
    with Dissolve(0.5)

    me "Надо посмотреть на эту карту и запомнить путь до музея..."
    
    hide map suzdal
    with Dissolve(0.5)

    menu:
        "Куда свернуть на первом повороте?..."
        "Направо":
            jump bad_turn1
        "Налево":
            me "Отлично, я на верном пути"
    
    menu:
        "Куда свернуть на втором повороте?..."
        "Налево":
            jump bad_turn2
        "Никуда, идем прямо":
            me "Идем до следующего перекрестка..."

    menu:
        "Куда пойти на третьем повороте?..."
        "Направо":
            me "Отлично, я на верном пути"
        "Налево":
            jump bad_turn2
        "Прямо":
            jump bad_turn3

    menu:
        "Куда свернуть на четвертом повороте?..."
        "Прямо":
            jump bad_turn4
        "Направо":
            me "Уже близко"

    menu:
        "Финальный перекресток..."
        "Направо":
            me "Кажется, я добралась"
        "Налево":
            jump bad_turn5
        "Прямо":
            jump bad_turn5

    jump mdz

label bad_turn1:
    "Я оказалась обратно в Москве без огурцов"
    jump bad_ending

label bad_turn2:
    "Я свернула не туда и угодила в открытый канализационный люк"
    jump bad_ending

label bad_turn3:
    "Я попала в толпу последователей помидоров, которые меня ими закидали"
    jump bad_ending

label bad_turn4:
    "Я подскользнулась на банановой кожуре и погибла"
    jump bad_ending

label bad_turn5:
    "Утонула в реке Каменке"
    jump bad_ending

label bad_ending:
    hide me idle
    hide bg suzdal
    "{b} Плохая концовка {/b}"
    return




# # Declare characters used by this game.
# define s = Character(_("Sylvie"), color="#c8ffc8")
# define m = Character(_("Me"), color="#c8c8ff")

# # This is a variable that is True if you've compared a VN to a book, and False
# # otherwise.
# default book = False

# # The game starts here.
# label start:

#     # Start by playing some music.
#     play music "illurock.opus"

#     scene bg lecturehall
#     with fade

#     "It's only when I hear the sounds of shuffling feet and supplies being put away that I realize that the lecture's over."

#     "Professor Eileen's lectures are usually interesting, but today I just couldn't concentrate on it."

#     "I've had a lot of other thoughts on my mind...thoughts that culminate in a question."

#     "It's a question that I've been meaning to ask a certain someone."

#     scene bg uni
#     with fade

#     "When we come out of the university, I spot her right away."

#     show sylvie green normal
#     with dissolve

#     "I've known Sylvie since we were kids. She's got a big heart and she's always been a good friend to me."

#     "But recently... I've felt that I want something more."

#     "More than just talking, more than just walking home together when our classes end."

#     menu:

#         "As soon as she catches my eye, I decide..."

#         "To ask her right away.":

#             jump rightaway

#         "To ask her later.":

#             jump later


# label rightaway:

#     show sylvie green smile

#     s "Hi there! How was class?"

#     m "Good..."

#     "I can't bring myself to admit that it all went in one ear and out the other."

#     m "Are you going home now? Wanna walk back with me?"

#     s "Sure!"

#     scene bg meadow
#     with fade

#     "After a short while, we reach the meadows just outside the neighborhood where we both live."

#     "It's a scenic view I've grown used to. Autumn is especially beautiful here."

#     "When we were children, we played in these meadows a lot, so they're full of memories."

#     m "Hey... Umm..."

#     show sylvie green smile
#     with dissolve

#     "She turns to me and smiles. She looks so welcoming that I feel my nervousness melt away."

#     "I'll ask her...!"

#     m "Ummm... Will you..."

#     m "Will you be my artist for a visual novel?"

#     show sylvie green surprised

#     "Silence."

#     "She looks so shocked that I begin to fear the worst. But then..."

#     show sylvie green smile

#     menu:

#         s "Sure, but what's a \"visual novel?\""

#         "It's a videogame.":
#             jump game

#         "It's an interactive book.":
#             jump book


# label game:

#     m "It's a kind of videogame you can play on your computer or a console."

#     m "Visual novels tell a story with pictures and music."

#     m "Sometimes, you also get to make choices that affect the outcome of the story."

#     s "So it's like those choose-your-adventure books?"

#     m "Exactly! I've got lots of different ideas that I think would work."

#     m "And I thought maybe you could help me...since I know how you like to draw."

#     m "It'd be hard for me to make a visual novel alone."

#     show sylvie green normal

#     s "Well, sure! I can try. I just hope I don't disappoint you."

#     m "You know you could never disappoint me, Sylvie."

#     jump marry


# label book:

#     $ book = True

#     m "It's like an interactive book that you can read on a computer or a console."

#     show sylvie green surprised

#     s "Interactive?"

#     m "You can make choices that lead to different events and endings in the story."

#     s "So where does the \"visual\" part come in?"

#     m "Visual novels have pictures and even music, sound effects, and sometimes voice acting to go along with the text."

#     show sylvie green smile

#     s "I see! That certainly sounds like fun. I actually used to make webcomics way back when, so I've got lots of story ideas."

#     m "That's great! So...would you be interested in working with me as an artist?"

#     s "I'd love to!"

#     jump marry

# label marry:

#     scene black
#     with dissolve

#     "And so, we become a visual novel creating duo."

#     scene bg club
#     with dissolve

#     "Over the years, we make lots of games and have a lot of fun making them."

#     if book:

#         "Our first game is based on one of Sylvie's ideas, but afterwards I get to come up with stories of my own, too."

#     "We take turns coming up with stories and characters and support each other to make some great games!"

#     "And one day..."

#     show sylvie blue normal
#     with dissolve

#     s "Hey..."

#     m "Yes?"

#     show sylvie blue giggle

#     s "Will you marry me?"

#     m "What? Where did this come from?"

#     show sylvie blue surprised

#     s "Come on, how long have we been dating?"

#     m "A while..."

#     show sylvie blue smile

#     s "These last few years we've been making visual novels together, spending time together, helping each other..."

#     s "I've gotten to know you and care about you better than anyone else. And I think the same goes for you, right?"

#     m "Sylvie..."

#     show sylvie blue giggle

#     s "But I know you're the indecisive type. If I held back, who knows when you'd propose?"

#     show sylvie blue normal

#     s "So will you marry me?"

#     m "Of course I will! I've actually been meaning to propose, honest!"

#     s "I know, I know."

#     m "I guess... I was too worried about timing. I wanted to ask the right question at the right time."

#     show sylvie blue giggle

#     s "You worry too much. If only this were a visual novel and I could pick an option to give you more courage!"

#     scene black
#     with dissolve

#     "We get married shortly after that."

#     "Our visual novel duo lives on even after we're married...and I try my best to be more decisive."

#     "Together, we live happily ever after even now."

#     "{b}Good Ending{/b}."

#     return

# label later:

#     "I can't get up the nerve to ask right now. With a gulp, I decide to ask her later."

#     scene black
#     with dissolve

#     "But I'm an indecisive person."

#     "I couldn't ask her that day and I end up never being able to ask her."

#     "I guess I'll never know the answer to my question now..."

#     "{b}Bad Ending{/b}."

#     return
