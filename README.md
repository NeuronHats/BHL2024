# Tinder do pracy
# Jobber

- parsowanie PDF, summary AI dla pracodacy, auto wypelnianie formularza o szukanej pracy
- panel pracownika i pracodawcy
- dodawanie oferty przez pracodawce
- swipe left right


# TODO:
- [x] applications
- [x] login styles
- [x] register styles
- [x] recruiter panel
- [x] main page if no cards, show text "no more cards"
- [x] ai sumarizer
- [x] message "applied" when you swipe right
- [x] main instead of menu, home page
- [x] register "upload your CV" text
- [ ] embed register
- [ ] recruiter styling
- [ ] main page polish (buttons, more dense text)
- [ ] presentation
- [ ] one pager
- [ ] preparation for judges
- [ ] paid swipes (hehe)
- [x] cache openai invokations
- [ ] db for presentation






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
