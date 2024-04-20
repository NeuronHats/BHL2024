# Tinder do pracy

- parsowanie PDF, summary AI dla pracodacy, auto wypelnianie formularza o szukanej pracy
- panel pracownika i pracodawcy
- dodawanie oferty przez pracodawce
- swipe left right


# TODO:
- [x] applications
- [ ] login styles
- [ ] register styles
- [x] recruiter panel
- [x] main page if no cards, show text "no more cards"
- [x] ai sumarizer
- [ ] message "applied" when you swipe right
- [ ] main page polish (buttons, more dense text)
- [ ] embed register
- [ ] presentation
- [ ] one pager
- [ ] preparation for judges
- [ ] paid swipes (hehe)
- [ ] main instead of menu, home page






# TMP

        <p>
            {{ form.education_text.label }}<br>
            {{ form.education_text(size=32) }}
        </p>
        <p>
            {{ form.education_level.label }}<br>
            {{ form.education_level(size=32) }}
        </p>
        <p>
            {{ form.experience_text.label }}<br>
            {{ form.experience_text(size=32) }}
        </p>
        <p>
            {{ form.experience_years.label }}<br>
            {{ form.experience_years(size=32) }}
        </p>
        <p>
            {{ form.technologies_text.label }}<br>
            {{ form.technologies_text(size=32) }}
        </p>
        <p>
            {{ form.soft_skills_text.label }}<br>
            {{ form.soft_skills_text(size=32) }}
        </p>
