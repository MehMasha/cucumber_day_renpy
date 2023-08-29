define cashier = Character("Кассир", color="#b54848")
define sc = Character("Звук со сцены", color="#b54848")
label mdz:
    $ money = 0
    scene bg mdz:
        zoom 1.5
    show me idle at right
    me "Ура! Надо купить билет!"
    "Иду к кассе музея..."
    show me idle at left
    with Dissolve(.5)
    pause 0.5
    show cashier angry at right
    with Dissolve(.5)

    cashier "Стой! Без билета не пущу!"
    me "Я и хочу купить билет!"
    cashier "Так покупай! С тебя 600 рублей!"
    show me sad 
    me "Как? Да у меня всего с собой 600 рублей"
    cashier "Ну так давай их сюда"
    "Я с печалью отдала кассиру все свои деньги и получила заветный билет"

    hide cashier angry
    show me sad at center
    with Dissolve(0.5)

    "Уже позже я узнала, что это был просто жестокий перекуп, который наглым образом обманул меня на деньги"
    "Мне повезло, что он продал мне хотя бы реальный билет и я спокойно зашла внутрь"

    "Внутри мое внимание привлекли три места"

    $ seen_places = {
        "kacheli": False,
        "shops": False,
        "scena": False,
    }

    jump in_mdz


label in_mdz:
    show me idle at left
    hide person1 stay
    hide person2 stay
    hide person3 stay
    hide person4 stay
    menu:
        "Что же выбрать?"
        "Сцена":
            jump scena 
        "Качели":
            jump kacheli
        "Ярмарка":
            jump shops
        "Выход в город":
            jump exit_mdz

label scena:
    if seen_places['scena']:
        "Хм, здесь ничего нового не появилось"
        jump in_mdz

    "На сцене я услышала рассказы про то, как древние Суздальцы готовили малосольные огурцы"

    sc "...и для этого они добавляли в тазик соль, чеснок и укроп"
    
    me "Интересненько..."

    "Подумала я и пошла дальше"

    $ seen_places['scena'] = True
    jump in_mdz


label kacheli:
    if seen_places['kacheli']:
        "Хм, здесь ничего нового не появилось"
        jump in_mdz


    "На качели качались дети и взрослые, человек, который отвечал за
    этот атракцион"
    "делал это с таким энтузиазмом, что во все стороны летели ботинки, шапки, монетки и сумки"
    "Один десятюнчик приземлился рядом со мной, но человек, который его выронил, крикнул мне: \'Забирай!\'"
    menu:
        "Рискнуть своей жизнью и подобрать монетку?"
        "Да":
            $ seen_places['kacheli'] = True
            $ money = money + 1
            "Уворачиваясь от летающих предметов, я как ниндзя схватила эту монетку и убежала на свое старое место"
        "Нет":
            me "Не, пожалуй, я не хочу получить ботинком по голове..."
    jump in_mdz

label shops:
    if seen_places['shops']:
        "Хм, здесь ничего нового не появилось"
        jump in_mdz

    "Здесь было огромное количество разных магазинчиков"
    "Вот магазин с кружками, вот с магнитиками, вот с берестой"
    "И тут я увидела ее..."
    "ПАЛАТКУ С ОГУРЦАМИ"
    menu:
        "Встаем в очередь?"
        "Да":

            jump in_queue
            jump in_mdz

        "Нет":
            jump in_mdz


label in_queue:
    show me idle:
        xalign 0.0
        yalign 1.0
    show person1 stay:
        xalign 0.25
        yalign 1.0
        zoom 0.85
    show person2 stay:
        xalign 0.5
        yalign 1.0
        zoom 0.8
    show person3 stay:
        xalign 0.75
        yalign 1.0
    show person4 stay:
        xalign 1.0
        yalign 1.0
        zoom 0.9

    "Жду..."
    pause 1.0

    show me idle:
        xalign 0.25
        yalign 1.0
    show person1 stay:
        xalign 0.5
        yalign 1.0
        zoom 0.85
    show person2 stay:
        xalign 0.75
        yalign 1.0
        zoom 0.8
    show person3 stay:
        xalign 1.0
        yalign 1.0
    hide person4 stay
    with Dissolve(1.0)

    menu:
        "Может, ну его?"
        "Валим":
            jump in_mdz
        "Я получу этот огурец!":
            "Очередь двигалась очень медленно..."

    pause 1.5

    show me idle:
        xalign 0.5
        yalign 1.0
    show person1 stay:
        xalign 0.75
        yalign 1.0
        zoom 0.85
    show person2 stay:
        xalign 1.0
        yalign 1.0
        zoom 0.8
    hide person3 stay
    with Dissolve(1.0)

    menu:
        "Может, ну его, а то совсем долго?"
        "Валим":
            jump in_mdz
        "Я получу этот огурец любой ценой!":
            "Очередь двигалась очень медленно..."

    pause 2.0

    show me idle:
        xalign 0.75
        yalign 1.0
    show person1 stay:
        xalign 1.0
        yalign 1.0
        zoom 0.85
    hide person2 stay
    with Dissolve(1.0)

    menu:
        "Я больше не могууууууу"
        "Валим":
            jump in_mdz
        "Я остаюсь!":
            "Очередь двигалась еще медленнее..."

    pause 2.5

    show me idle:
        xalign 1.0
        yalign 1.0
    hide person1 stay
    with Dissolve(1.0)

    "\"Огурцы закончились\" - именно эту табличку повесили прямо перед моим лицом"
    "На прилавке одиноко лежал десятюнчик - сдача, которую не забрал последний покупатель"
    "Его я и подобрала"
    $ money = money + 1
    $ seen_places['shops'] = True



label exit_mdz:
    "exit"